from collections import Counter


def top_k_words(text, k):
    words = text.lower().split()
    count = Counter(words)
    most_common = count.most_common(k)
    result = []
    for word, freq in most_common:
        result.append(word)
    return result


text = "apple orange banana apple orange apple"
k = 2
print(f"Top {k} most frequent words are {top_k_words(text, k)}")
