Day 3 — Lists & comprehensions

Problem: Flatten a list of arbitrarily nested lists of integers into a single list.
Concepts: recursion/stack, list comprehensions, iterators.
Hint: Recursively detect list type or use a stack.
Difficulty: Medium
Extension: Make it a generator that yields items lazily.


solution :


# **Day 3 — Lists & Comprehensions**

## **Problem:**

Flatten a list of arbitrarily nested lists of integers into a single list.

**Example:**
A nested list like `[1, [2, 3, [4, 5]], 6]` should become `[1, 2, 3, 4, 5, 6]`.

---

## **Concepts Covered:**

* Recursion
* Generators (lazy evaluation)
* Iterators
* List comprehension (for one-level flattening)
* `isinstance()` function

---

## **Approach 1: Recursive Flattening**

**How it works:**

1. Go through each element of the list.
2. Check if the element is a list.

   * If yes → flatten it recursively and combine the result.
   * If no → it’s an integer, keep it in the result.
3. Continue this process for all elements until the entire list is flattened.

**Key points:**

* Recursion handles **arbitrary levels of nesting**.
* Uses memory proportional to the **depth of nesting**.
* Simple and intuitive.

---

## **Approach 2: Generator (Lazy Flattening)**

**How it works:**

1. Iterate over each element.
2. If the element is a nested list → recursively **yield all items one by one**.
3. If the element is an integer → **yield it directly**.
4. The generator produces elements **one at a time**, instead of building the whole list at once.

**Advantages of generator approach:**

* Memory-efficient for very large lists.
* Can process elements on-the-fly without storing the full list.

---

## **Simple Way to Remember**

1. **Check the type of item:**

   * List → flatten it.
   * Number → keep it.
2. **Think recursively:**

   * If you can flatten smaller lists, you can flatten bigger lists.
3. **Memory difference:**

   * Recursive approach → stores the full list in memory.
   * Generator approach → yields items lazily.
4. **List comprehension:**

   * Works for one-level nested lists only.
   * For deeper nesting → use recursion or generator.

---

