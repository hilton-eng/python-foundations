"""Exercise 1: avoid the mutable default trap."""


def safe_append(item, items=None):
       """Append item to items and return the list.

    If items is not given, start from a new empty list on every call.
    """
    if items is None:
        items = []
    items.append(item)
    return items


def test_independent_lists():
    first = safe_append("a")
    second = safe_append("b")
    assert first == ["a"], first
    assert second == ["b"], second
    assert first is not second


def test_uses_given_list():
    mine = ["x"]
    result = safe_append("y", mine)
    assert result == ["x", "y"], result
    assert result is mine


test_independent_lists()
test_uses_given_list()
print("all tests passed")
