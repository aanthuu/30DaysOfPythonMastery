import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def primes_up_to(n: int) -> list:
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes
