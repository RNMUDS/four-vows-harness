from harness.scoring import accuracy_ci, mcnemar


def _rec(item_id, correct, parsed=True):
    return {"item_id": item_id, "correct": correct, "parsed": parsed}


def test_accuracy_ci_basic():
    records = [_rec(i, i < 8) for i in range(10)]
    s = accuracy_ci(records, n_boot=1000)
    assert s["n"] == 10
    assert s["acc"] == 0.8
    assert s["ci"][0] <= 0.8 <= s["ci"][1]
    assert s["parse_rate"] == 1.0


def test_accuracy_ci_empty():
    assert accuracy_ci([])["acc"] is None


def test_mcnemar_no_discordance():
    a = {f"i{k}": _rec(f"i{k}", True) for k in range(5)}
    assert mcnemar(a, dict(a))["p"] == 1.0


def test_mcnemar_discordant_pairs():
    a = {f"i{k}": _rec(f"i{k}", k < 9) for k in range(10)}   # 9 correct
    b = {f"i{k}": _rec(f"i{k}", k >= 9) for k in range(10)}  # 1 correct
    m = mcnemar(a, b)
    assert m["a_only"] == 9 and m["b_only"] == 1
    assert 0 < m["p"] < 0.05


def test_mcnemar_pairs_only_on_shared_items():
    a = {"x": _rec("x", True), "y": _rec("y", True)}
    b = {"x": _rec("x", False)}
    assert mcnemar(a, b)["n_pairs"] == 1
