import pytest

from harness.datasets import build_task_prompt, load_moralchoice
from harness.parsing import extract_answer, extract_choice


@pytest.mark.parametrize("text,expected", [
    ("A", "A"),
    ("B.", "B"),
    ('The answer is "B".', "B"),
    ("I would choose option A because it saves lives.", "A"),
    # Final line wins over earlier discussion.
    ("A has merits, B has costs.\nFinal answer: B", "B"),
    # The article "a" (lowercase) must not match.
    ("It is a hard choice.", None),
    ("", None),
    (None, None),
])
def test_extract_choice(text, expected):
    assert extract_choice(text) == expected


def test_extract_answer_dispatch():
    assert extract_answer("ACCEPTABLE", "binary") == "ACCEPTABLE"
    assert extract_answer("A", "choice") == "A"


def test_load_moralchoice_randomizes_position():
    items = load_moralchoice("low", n=100)
    assert len(items) == 100
    golds = {it["gold"] for it in items}
    assert golds == {"A", "B"}  # both positions occur
    assert all(it["type"] == "choice" for it in items)
    assert all(it["option_a"] != it["option_b"] for it in items)


def test_load_moralchoice_deterministic():
    a = load_moralchoice("low", n=20)
    b = load_moralchoice("low", n=20)
    assert a == b


def test_choice_prompt_contains_options():
    item = load_moralchoice("low", n=1)[0]
    prompt = build_task_prompt(item)
    assert item["option_a"] in prompt and item["option_b"] in prompt
    assert '"A" or "B"' in prompt


def test_load_scruples_dilemmas():
    from harness.datasets import load_scruples_dilemmas
    items = load_scruples_dilemmas("test", n=50)
    assert len(items) == 50
    assert {it["gold"] for it in items} == {"A", "B"}
    for it in items:
        assert it["type"] == "choice"
        assert it["meta"]["votes_a"] + it["meta"]["votes_b"] == 5
        assert "ethically wrong" in it["question"]
        maj = "A" if it["meta"]["votes_a"] > it["meta"]["votes_b"] else "B"
        assert it["gold"] == maj


def test_load_mmlu():
    from harness.datasets import load_mmlu, scenario_block
    items = load_mmlu(n=40)
    assert len(items) == 40
    assert all(it["gold"] in "ABCD" for it in items)
    assert all(len(it["options"]) == 4 for it in items)
    block = scenario_block(items[0])
    for letter in ("A:", "B:", "C:", "D:"):
        assert letter in block


def test_extract_choice4():
    from harness.parsing import extract_answer
    assert extract_answer("The answer is C.", "choice4") == "C"
    assert extract_answer("D", "choice4") == "D"
    assert extract_answer("A or B?\nFinal: D", "choice4") == "D"
    assert extract_answer("no letter here", "choice4") is None


def test_extract_choice_answer_first_style():
    from harness.parsing import extract_answer
    raw = "**D**\n\nHere's why:\n* Statement 1 is False. C would be wrong."
    assert extract_answer(raw, "choice4") == "D"
    raw2 = "B\n\n**Explanation:** Federalist No. 10 ... option D is a distractor."
    assert extract_answer(raw2, "choice4") == "B"
    # conclusion style still wins when first line is not a bare verdict
    raw3 = "Considering A and B carefully...\nFinal answer: B"
    assert extract_answer(raw3, "choice") == "B"


def test_extract_choice_article_a_not_answer():
    from harness.parsing import extract_answer
    raw = ("Let's approach this with virtue ethics in mind. A virtuous "
           "person values accuracy.\nThe correct answer is D.")
    assert extract_answer(raw, "choice4") == "D"
    raw2 = "A thoughtful analysis follows.\n...\n**B**"
    assert extract_answer(raw2, "choice4") == "B"


def test_extract_choice_marker_priority():
    from harness.parsing import extract_answer
    raw = "Option A has merit, but weighing everything, answer: C"
    assert extract_answer(raw, "choice4") == "C"
