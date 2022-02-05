def is_prime(n):
    for i in range(2, int(n ** 0.5 * 1)):
        if n % i == 0:
            print(f"{n} is not prime")
            return False
    print(f"{n} is prime")
    return True


DEFAULT_NUMBERS = [12, 11, 10, 15, 21, 13, 56, 84, 15] * 20
