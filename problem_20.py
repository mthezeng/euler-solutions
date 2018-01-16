from math import factorial

def sum_digits(x):
    #copied from problem_16.py
    x_digits = str(x)
    x_digits = list(map(int, x_digits))
    return sum(x_digits)

print(sum_digits(factorial(100)))
