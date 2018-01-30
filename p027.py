from math import sqrt, ceil
from timer import timer

def is_prime(num):
    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            return False
    return True

def quadratic_primes(a, b):
    # returns the number of primes created by consecutive values of n for n^2 + an + b
    n = 0
    while n*n + a*n + b >= 0 and is_prime(n*n + a*n + b):
        n += 1
    return n

def brute_force():
    prev_max = 0
    prev_max_loc = (0,0)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            current = quadratic_primes(a, b)
            if current > prev_max:
                prev_max = current
                prev_max_loc = (a,b)
    return prev_max_loc[0], prev_max_loc[1], prev_max

def main():
    a_result, b_result, primes_length = brute_force()
    print('The product of {0} and {1} is {2}'.format(a_result, b_result, a_result * b_result))
    print('{0} primes were generated.'.format(primes_length))

timer(main)
