# tests/test_day01.py
from src.day01 import is_prime, primes_up_to


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False


def test_primes_up_to():
    assert primes_up_to(10) == [2, 3, 5, 7]
    assert primes_up_to(1) == []
    assert primes_up_to(2) == [2]
