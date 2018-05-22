from itertools import permutations
from functools import reduce
from timer import timer

def fits_property(n):
    """
    >>> fits_property(1406357289)
    True
    >>> fits_property(1234567890)
    False
    """
    primes = [2,3,5,7,11,13,17]
    bounds = [1,4]
    n_str = str(n)
    for p in primes:
        if int(n_str[bounds[0]:bounds[1]]) % p != 0:
            return False
        else:
            bounds[0] += 1
            bounds[1] += 1
    return True

def substring_divisibility():
    # ugly brute force check, avg runtime: 21 seconds
    digits = '1234567890'
    p = permutations(digits)
    for i in p:
        current = int(reduce(lambda x, y: str(x) + str(y), i, ''))
        if fits_property(current):
            yield current

def main():
    with_property = list(substring_divisibility())
    print(with_property)
    print(sum(with_property))

timer(main)
