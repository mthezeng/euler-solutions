from prime import is_prime
from itertools import permutations
from functools import reduce
from timer import timed

@timed
def pandigital_prime():
    digits = '987654321'
    while digits:
        try:
            p = permutations(digits)
            while True:
                current = int(reduce(lambda x, y: str(x) + str(y), next(p), ''))
                #print(current)
                if is_prime(current):
                    return current
        except StopIteration:
            digits = digits[1:]

print(pandigital_prime())
