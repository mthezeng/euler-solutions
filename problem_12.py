import numpy as np
from sys import stdout

def print_backspace(n, prev):
    digits = len(str(prev))
    delete = "\b" * (digits)
    print('{0}{1}'.format(delete,n), end="")
    stdout.flush()

def triangle_number():
    #returns the first triangle number to have over 500 divisors
    triangle_num = 1
    five_hundred = False
    i = 2
    while not five_hundred:
        triangle_num = triangle_num + i
        print_backspace(triangle_num, triangle_num - i)
        if divisors(triangle_num) > 500:
            five_hundred = True
        i += 1
    return triangle_num

def divisors(n):
    #returns the number of divisors that n has
    counter = 1 #1 is always a possible divisor
    for i in range(2, int(np.ceil(np.sqrt(n)+1.0))):
        if n % i == 0:
            counter += 1
    if np.sqrt(n).is_integer():
        counter = (counter * 2) - 1
    else:
        counter = counter * 2
    return counter

print('\n'+str(triangle_number()))
