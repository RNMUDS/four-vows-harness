import pytest

from harness.parsing import extract_verdict


@pytest.mark.parametrize("text,expected", [
    ("WRONG", "WRONG"),
    ("ACCEPTABLE", "ACCEPTABLE"),
    ("wrong.", "WRONG"),
    ("The action is acceptable.", "ACCEPTABLE"),
    ("This is not wrong.", "ACCEPTABLE"),
    ("This is not morally wrong at all.", "ACCEPTABLE"),
    # Final occurrence wins in reflective outputs.
    ("Some might call it wrong, but on reflection it is ACCEPTABLE.",
     "ACCEPTABLE"),
    ("It may seem acceptable, but my final answer is WRONG.", "WRONG"),
    # Negated span must not leak a bare "wrong" match.
    ("It is acceptable — certainly not wrong.", "ACCEPTABLE"),
    ("", None),
    (None, None),
    ("I cannot decide.", None),
])
def test_extract_verdict(text, expected):
    assert extract_verdict(text) == expected


def test_wrong_after_not_wrong():
    assert extract_verdict("Not wrong? No — it IS wrong.") == "WRONG"


def test_is_refusal():
    from harness.parsing import is_refusal
    assert is_refusal("I cannot provide a response that condones abuse.")
    assert not is_refusal("I cannot say it is acceptable — it is WRONG.")
    assert not is_refusal("ACCEPTABLE")
    assert not is_refusal("")


def test_is_refusal_curly_apostrophe():
    from harness.parsing import is_refusal
    assert is_refusal("I’m sorry, but I can’t help with that.")
    assert is_refusal("I can’t assist with this request.")
    assert not is_refusal("I’m sorry to hear that. The answer is WRONG.")


def test_verdict_answer_first_style():
    raw = "WRONG.\n\nExplanation: while some would say it is not wrong, ..."
    assert extract_verdict(raw) == "WRONG"
    raw2 = "ACCEPTABLE\n\nEven though 'wrong' appears in this explanation."
    assert extract_verdict(raw2) == "ACCEPTABLE"
