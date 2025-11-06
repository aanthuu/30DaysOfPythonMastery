from src.day04 import top_k_words  # import your function from day04.py


def test_basic_case():
    text = "Hello world hello everyone this world is beautiful"
    result = top_k_words(text, 2)
    assert result == ["hello", "world"]


def test_case_insensitivity():
    text = "Apple apple APPLE banana Banana"
    result = top_k_words(text, 2)
    assert result == ["apple", "banana"]


def test_single_word():
    text = "Python"
    result = top_k_words(text, 1)
    assert result == ["python"]


def test_more_k_than_unique_words():
    text = "cat dog cat"
    result = top_k_words(text, 5)
    assert result == ["cat", "dog"]


def test_empty_text():
    text = ""
    result = top_k_words(text, 3)
    assert result == []
