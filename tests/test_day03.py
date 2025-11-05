from src.day03 import flatten


def test_flatten_basic():
    nested_list = [1, [2, 2, [3, 4, 5]], 6]
    expected = [1, 2, 2, 3, 4, 5, 6]
    assert flatten(nested_list) == expected


def test_flatten_empty():
    nested_list = []
    expected = []
    assert flatten(nested_list) == expected


def test_flatten_single_level():
    nested_list = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    assert flatten(nested_list) == expected


def test_flatten_deeply_nested():
    nested_list = [[[[1]]], 2, [[3, [4]]]]
    expected = [1, 2, 3, 4]
    assert flatten(nested_list) == expected


def test_flatten_only_nested_lists():
    nested_list = [[[[[1, 2]]]], [[3]], [4]]
    expected = [1, 2, 3, 4]
    assert flatten(nested_list) == expected
