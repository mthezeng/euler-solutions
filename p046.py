from timer import timed
from prime import is_prime, primes_upto

def odd_composite(n):
    return n % 2 != 0 and not is_prime(n)

def check_conjecture(n):
    if not odd_composite(n):
        return True # claim is vacuously true
    for p in primes_upto(n):
        i = 1
        while p + 2*(i**2) < n:
            i += 1
        if p + 2*(i**2) == n:
            #print('{0} + 2*({1}**2) == {2}'.format(p, i, n))
            return True
    return False

@timed
def main():
    # inefficient; runs in ~4.5 seconds
    done = False
    num = 3
    while check_conjecture(num):
        num += 2
    print(num)

main()
