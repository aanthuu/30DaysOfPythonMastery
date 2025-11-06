Day 4 — Dictionaries & counting

Problem: Word frequency: return top k most frequent words from a text (case insensitive).
Concepts: dict, collections.Counter, sorting by value, tie-breakers.
Hint: Use Counter.most_common(k) or sort by (-count, word).
Difficulty: Easy–Medium
Extension: Ignore stop words and punctuation.

solution :

## 🧠 **Day 4 — Dictionaries & Counting**

### 📝 **Problem**

Given a block of text, return the **top `k` most frequent words** (case insensitive).
For example,

> Input: `"Hello world hello everyone this world is beautiful"`, `k = 2`
> Output: `['hello', 'world']`

---

### 🎯 **Concepts Covered**

* **Dictionaries** — to store and update word counts.
* **collections.Counter** — to simplify frequency counting.
* **Sorting by values** — to find the most frequent words.
* **List handling** — to extract final results.

---

### 🧩 **Theory / Approach**

1. **Convert text to lowercase**

   * Ensures words like “Hello” and “hello” are treated the same.

   ```python
   text.lower()
   ```

2. **Split the text into words**

   * Using `.split()` separates words by spaces.

   ```python
   words = text.lower().split()
   ```

3. **Count the frequency of each word**

   * The `Counter` class from the `collections` module automatically counts how many times each word appears.

   ```python
   from collections import Counter
   count = Counter(words)
   ```

4. **Find the top K most common words**

   * `Counter.most_common(k)` returns a list of tuples:
     e.g. `[('hello', 2), ('world', 2)]`

   ```python
   most_common = count.most_common(k)
   ```

5. **Extract only the words from the tuples**

   * We use a simple loop to get the words alone.

   ```python
   result = []
   for word, freq in most_common:
       result.append(word)
   ```

6. **Return the result list**

   * The final output is a list of the top K frequent words.




### 🧠 **Key Learning Points**

* `collections.Counter` simplifies word frequency problems.
* Dictionaries and sorting are fundamental tools for analyzing data.
* Always normalize text (lowercase + remove punctuation) for consistent results.
* You can extend this to ignore **stopwords** (like *“the, is, of”*) for real-world NLP tasks.

