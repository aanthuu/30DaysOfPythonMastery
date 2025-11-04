from src.day02 import reverse_words


from src.day02 import reverse_words


def test_reverse_words():
    assert reverse_words("I love Python") == "I evol nohtyP"
    assert reverse_words("hello") == "olleh"
    assert reverse_words("") == ""
    assert reverse_words("  hello   world  ") == "olleh dlrow"
    assert reverse_words("Ananthu Rocks") == "uhtnanA skcoR"
