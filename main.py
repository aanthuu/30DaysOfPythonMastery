from src.day01 import is_prime, primes_up_to


def main():
    print("Prime NUmber Checker")
    n = int(input("Enter the number to check"))
    if is_prime(n):
        print(f"The number {n} is a prime number")

    else:
        print(f"The number {n} is Not a prime number")

    print(f"prime numbers upto {n}")
    print(f"Result : {primes_up_to(n)}")


if __name__ == "__main__":
    main()
