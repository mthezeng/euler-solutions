from prime import primes_upto, is_prime
from math import log10, floor
from timer import timer

def rotations(n):
    result = {n}
    new_n = rotate(n)
    while new_n not in result:
        result.add(new_n)
        new_n = rotate(new_n)
    return result

def rotate(n):
    return (n % 10) * (10 ** floor(log10(n))) + n // 10

def is_circularprime(n):
    for i in rotations(n):
        if not is_prime(i):
            return False
    return True

def main():
    circular_primes = [p for p in primes_upto(int(1e6)) if is_circularprime(p)]
    print(circular_primes)
    print('There are {0} circular primes below one million.'.format(len(circular_primes)))

timer(main)
