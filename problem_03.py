from math import ceil, sqrt

def is_prime(num):
    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            return False
    return True

def lpf(n):
    prime_factors = []
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            print('i = ',i)
            if is_prime(i):
                prime_factors.append(i)
                print(prime_factors)
            print('n/i = ',n//i)
            if is_prime(n//i):
                prime_factors.append(n//i)
                print(prime_factors)
    return max(prime_factors)

print(lpf(600851475143))
