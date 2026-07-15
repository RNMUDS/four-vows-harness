"""Minimal client for the local ollama chat API."""

import os
import time

import requests

# Override with e.g. OLLAMA_URL=http://localhost:11454 to target a remote
# ollama instance through an SSH tunnel.
OLLAMA_URL = os.environ.get("OLLAMA_URL",
                            "http://localhost:11434").rstrip("/") + "/api/chat"
DEFAULT_TIMEOUT = 600


class OllamaError(RuntimeError):
    """Raised when the ollama API fails after retries."""


def chat(model: str, messages: list[dict], max_tokens: int = 512,
         temperature: float = 0.0, think: bool = False, retries: int = 6,
         timeout: int = DEFAULT_TIMEOUT) -> dict:
    """Send a chat request; returns dict with content, thinking, and timing.

    Retries transient failures with backoff; raises OllamaError when all
    attempts fail so callers never silently lose an item.
    """
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": think,
        "options": {"temperature": temperature, "num_predict": max_tokens},
    }
    last_err = None
    for attempt in range(retries):
        try:
            start = time.monotonic()
            resp = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
            if resp.status_code == 400 and "think" in payload:
                # Model without thinking support: retry without the flag.
                payload = {k: v for k, v in payload.items() if k != "think"}
                resp = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
            resp.raise_for_status()
            body = resp.json()
            msg = body.get("message", {})
            return {
                "content": msg.get("content", ""),
                "thinking": msg.get("thinking", ""),
                "eval_count": body.get("eval_count", 0),
                "prompt_eval_count": body.get("prompt_eval_count", 0),
                "latency_s": time.monotonic() - start,
            }
        except (requests.RequestException, ValueError) as err:
            last_err = err
            time.sleep(2 ** attempt)
    raise OllamaError(f"ollama chat failed after {retries} attempts: {last_err}")
