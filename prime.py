def is_prime(n):
    """
    Check if a number is prime
    """
    from math import ceil, sqrt
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def prime_gen(n):
    """
    A generator that yields n prime numbers
    """
    from numpy import mod
    l = [2, 3]
    yield 2
    yield 3
    i = 3
    while len(l) < n:
        if not 0 in mod(i, l):
            l.append(i)
            yield i
        i += 2

def primes_upto(n):
    """Sieve of Eratosthenes"""
    """
    returns a list of all primes below n
    """
    from math import ceil, sqrt
    #n is exclusive
    primes = set(range(2, n))
    for i in range(2, ceil(sqrt(n))):
        primes = primes - set(range(2*i, n, i))
    return primes


def prime_factors(n):
    factors = []
    num = n
    for p in primes(n):
        while num % p == 0:
            num = num // p
            factors.append(p)
    return factors


def main():
    from p007 import primes
    user_n = int(input('n: '))
    print(prime_factors(user_n))


if __name__ == "__main__":
    main()
