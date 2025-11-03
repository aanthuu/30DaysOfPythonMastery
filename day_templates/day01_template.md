Day 1 — Python basics + control flow

Problem: Implement is_prime(n) and a function primes_up_to(n) returning primes ≤ n.
Concepts: loops, conditionals, functions, time complexity.
Hint: Trial division; optimize by checking up to sqrt(n).
Difficulty: Easy
Extension: Sieve of Eratosthenes.

solution :

### 🔹 **Definition**

A **prime number** is a number **greater than 1** that has **no divisors other than 1 and itself**.

In other words:

* You **cannot divide it evenly** by any other number (no remainder = evenly divides).
* Only 1 and the number itself divide it exactly.

---

### 🔹 **Examples**

| Number | Divisible by | Prime or Not? | Why                    |
| :----- | :----------- | :------------ | :--------------------- |
| 2      | 1, 2         | ✅ Prime       | only 1 and 2 divide it |
| 3      | 1, 3         | ✅ Prime       | only 1 and 3 divide it |
| 4      | 1, 2, 4      | ❌ Not prime   | divisible by 2         |
| 5      | 1, 5         | ✅ Prime       | only 1 and 5 divide it |
| 6      | 1, 2, 3, 6   | ❌ Not prime   | divisible by 2 and 3   |
| 7      | 1, 7         | ✅ Prime       | only 1 and 7 divide it |

---

### 🔹 **First few prime numbers**

👉 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, …

> Note:
>
> * 2 is the **only even prime number**.
> * Every other even number can be divided by 2, so they’re not prime.

---

### 🔹 **Non-prime numbers**

Numbers that are **not prime** and **greater than 1** are called **composite numbers**
(e.g., 4, 6, 8, 9, 10, 12, 15…)

---

### 🔹 **Quick way to check (logic)**

For a number `n`:

1. If `n <= 1` → not prime
2. Check if it’s divisible by any number between `2` and `√n`
3. If divisible → not prime
4. Else → prime ✅