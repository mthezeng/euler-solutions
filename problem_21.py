from math import ceil
from math import sqrt

def find_divisors(n):
    divs = [1]
    for i in range(2,ceil(sqrt(n))):
        if n % i == 0 and i != n:
            divs.append(i)
            divs.append(int(n/i))
    return divs

def amicable():
    amicable_numbers = []
    for a in range(1, 10000):
        b = sum(find_divisors(a))
        if sum(find_divisors(b)) == a and a != b:
            if a not in amicable_numbers or b not in amicable_numbers:
                amicable_numbers.append(a)
                amicable_numbers.append(b)
                print(amicable_numbers)
    return sum(amicable_numbers)

print(amicable())
