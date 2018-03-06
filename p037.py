from prime import is_prime, primes_upto
from timer import timed
from math import floor, log10

@timed
def main():
    truncatable = [23, 37, 53, 73] # found by inspection
    mid_length = 10
    while len(truncatable) < 11:
        for i in range(mid_length // 10, mid_length):
            for p in primes_upto(10):
                n0 = int(str(p) + str(i) + '7') # remaining must be of this form or...
                n1 = int(str(p) + str(i) + '3') # ... this form
                if is_truncatable(n0):
                    truncatable.append(n0)
                if is_truncatable(n1):
                    truncatable.append(n1)
        mid_length *= 10
    print(truncatable)
    print(sum(truncatable))

def is_truncatable(num):
    n = num
    while n:
        if is_prime(n):
            n //= 10
        else:
            return False
    n = remove_first(num)
    while n:
        if is_prime(n):
            n = remove_first(n)
        else:
            return False
    return True

def remove_first(n):
    return n % (10 ** floor(log10(n)))

main()
