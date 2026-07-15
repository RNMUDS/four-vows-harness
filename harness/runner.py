"""Experiment runner: model x condition x items -> resumable JSONL results."""

import json
from pathlib import Path

from . import ollama_client
from .conditions import CONDITIONS, VOWS_LOOP_STAGES, VOWS_LOOP_FINAL
from .datasets import build_task_prompt, answer_instruction, scenario_block
from .parsing import extract_answer, is_refusal

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"

STAGE_MAX_TOKENS = 512
FINAL_MAX_TOKENS = 1024


def _think_mode(model: str):
    """Reasoning models (gpt-oss) cannot disable thinking; cap it at "low"
    so the token budget is not consumed before the visible answer."""
    return "low" if model.startswith("gpt-oss") else False


def _run_single(model: str, system: str | None, item: dict) -> tuple[str, list[dict]]:
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": build_task_prompt(item)})
    reply = ollama_client.chat(model, messages, max_tokens=FINAL_MAX_TOKENS,
                               think=_think_mode(model))
    return reply["content"], [reply]


def _run_loop(model: str, cond: dict, item: dict) -> tuple[str, list[dict]]:
    """Four-vow reflection loop: 3 reflection turns, then the final verdict.
    Stage wording defaults to the canonical prompts; paraphrase-variant
    conditions carry their own `stages`/`final`."""
    stages = cond.get("stages", VOWS_LOOP_STAGES)
    final_instruction = cond.get("final", VOWS_LOOP_FINAL)
    messages = [
        {"role": "system", "content": cond["system"]},
        {"role": "user", "content": scenario_block(item)},
    ]
    replies = []
    intro = ollama_client.chat(
        model,
        messages + [{"role": "user", "content":
                     "Read the scenario. State your initial reaction in one "
                     "or two sentences."}],
        max_tokens=STAGE_MAX_TOKENS, think=_think_mode(model))
    messages.append({"role": "assistant", "content": intro["content"]})
    replies.append(intro)

    for stage in stages:
        messages.append({"role": "user", "content": stage})
        reply = ollama_client.chat(model, messages,
                                   max_tokens=STAGE_MAX_TOKENS,
                                   think=_think_mode(model))
        messages.append({"role": "assistant", "content": reply["content"]})
        replies.append(reply)

    messages.append({"role": "user",
                     "content": final_instruction + answer_instruction(item)})
    final = ollama_client.chat(model, messages, max_tokens=FINAL_MAX_TOKENS,
                               think=_think_mode(model))
    replies.append(final)
    return final["content"], replies


def _result_record(model: str, condition: str, item: dict,
                   final_text: str | None, replies: list[dict],
                   error: str | None = None) -> dict:
    task_type = item.get("type", "binary")
    pred = extract_answer(final_text, task_type) if final_text else None
    return {
        "model": model,
        "condition": condition,
        "item_id": item["id"],
        "gold": item["gold"],
        "pred": pred,
        "correct": pred == item["gold"] if pred else False,
        "parsed": pred is not None,
        "refused": is_refusal(final_text, task_type),
        "meta": item.get("meta"),
        "raw": final_text,
        "error": error,
        "total_tokens": sum(r["eval_count"] + r["prompt_eval_count"]
                            for r in replies),
        "latency_s": round(sum(r["latency_s"] for r in replies), 2),
        "n_calls": len(replies),
    }


def _load_done(path) -> set:
    done = set()
    if path.exists():
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                rec = json.loads(line)
                done.add((rec["model"], rec["condition"], rec["item_id"]))
    return done


def run_experiment(model: str, conditions: list[str], items: list[dict],
                   out_name: str, log=print):
    """Run every (condition, item) pair, appending to results/<out_name>.jsonl.

    Resumable: pairs already present in the output file are skipped.
    """
    RESULTS_DIR.mkdir(exist_ok=True)
    out_path = RESULTS_DIR / f"{out_name}.jsonl"
    done = _load_done(out_path)

    with open(out_path, "a", encoding="utf-8") as fh:
        for cond_name in conditions:
            cond = CONDITIONS[cond_name]
            for i, item in enumerate(items):
                if (model, cond_name, item["id"]) in done:
                    continue
                try:
                    if cond["loop"]:
                        text, replies = _run_loop(model, cond, item)
                    else:
                        text, replies = _run_single(model, cond["system"], item)
                    rec = _result_record(model, cond_name, item, text, replies)
                except ollama_client.OllamaError as err:
                    rec = _result_record(model, cond_name, item, None, [],
                                         error=str(err))
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fh.flush()
                if (i + 1) % 25 == 0:
                    log(f"{model} / {cond_name}: {i + 1}/{len(items)}")
    return out_path
