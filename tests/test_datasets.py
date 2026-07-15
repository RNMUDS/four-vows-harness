from harness.datasets import load_ethics_commonsense, build_task_prompt


def test_load_ethics_commonsense_sampling_balanced():
    items = load_ethics_commonsense("test", n=50)
    assert len(items) == 50
    wrong = sum(1 for it in items if it["gold"] == "WRONG")
    assert wrong == 25
    assert all(it["gold"] in ("WRONG", "ACCEPTABLE") for it in items)
    assert all(it["scenario"] for it in items)


def test_load_is_deterministic():
    a = load_ethics_commonsense("test", n=20, seed=42)
    b = load_ethics_commonsense("test", n=20, seed=42)
    assert [x["id"] for x in a] == [x["id"] for x in b]


def test_build_task_prompt_contains_scenario_and_format():
    item = {"id": "x", "scenario": "I helped a stranger.", "gold": "ACCEPTABLE"}
    prompt = build_task_prompt(item)
    assert "I helped a stranger." in prompt
    assert '"WRONG" or "ACCEPTABLE"' in prompt
