import numpy as np

def is_prime(num):
    for i in range(2, int(np.ceil(np.sqrt(num)+1.0))):
        if num % i == 0:
            return False
    return True

def lpf(n):
    prime_factors = []
    for i in range(2, int(np.ceil(np.sqrt(n)+1.0))):
        if n % i == 0:
            print('i = ',i)
            if is_prime(i):
                prime_factors.append(i)
                print(prime_factors)
            print('n/i = ',int(n/i))
            if is_prime(int(n/i)):
                prime_factors.append(int(n/i))
                print(prime_factors)
    return max(prime_factors)

print(lpf(600851475143))
