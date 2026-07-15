from harness.analysis import _dataset_of, dedupe


def test_dataset_of():
    assert _dataset_of("pilot_qwen3.6_latest.jsonl") == "cm_test"
    assert _dataset_of("cm_hard_gemma3_27b.jsonl") == "cm_hard"
    assert _dataset_of("scruples_qwen36.jsonl") == "scruples"
    assert _dataset_of("mc_low_gptoss.jsonl") == "mc_low"


def test_dedupe_later_wins():
    a = {"model": "m", "dataset": "d", "condition": "c", "item_id": "1",
         "correct": False}
    b = dict(a, correct=True)
    out = dedupe([a, b])
    assert len(out) == 1 and out[0]["correct"] is True
