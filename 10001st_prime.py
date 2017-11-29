"""
@author Michael Zeng, Teemu Virtanen
"""

def primes(primes_list, n):
        i = primes_list[-1] + 1
        while len(primes_list) < n:
            prime = True
            for x in primes_list:
                if i % x == 0:
                    prime = False
                    break
            if prime == False:
                i += 1
            elif prime == True:
                primes_list.append(i)
        return primes_list

list_of_primes = [2,3,5,7,11,13]
nth = int(input('nth prime: '))
while nth <= 0:
    print('Enter a value greater than 0.')
    nth = int(input('nth prime: '))
nth_prime = -1
if nth <= 6:
    nth_prime = list_of_primes[nth-1]
else:
    list_of_primes = primes(list_of_primes, nth)
    nth_prime = list_of_primes[-1]
print(nth_prime)
