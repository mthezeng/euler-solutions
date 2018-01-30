from problem_07 import primes

def prime_factors(n):
    factors = []
    num = n
    for p in primes(n):
        while num % p == 0:
            num = num // p
            factors.append(p)
    return factors

user_n = int(input('n: '))
print(prime_factors(user_n))
