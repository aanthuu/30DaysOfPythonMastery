def reverse_words(sentence):
    words = sentence.split()
    reversed_list = []  # store reversed words
    for word in words:
        reversed_list.append(word[::-1])
    return " ".join(reversed_list)
