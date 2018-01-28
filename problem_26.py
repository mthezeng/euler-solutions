import progressbar
from copy import deepcopy

def division_algorithm(n):
    """elementary school division algorithm
    returns a boolean for whether 1/n is a repeating decimal or a terminating one
    also returns the length of the decimal (or the repeating sequence of the decimal)

    >>> division_algorithm(2)
    (False, 1)
    >>> division_algorithm(3)
    (True, 1)
    >>> division_algorithm(6)
    (True, 1)
    >>> division_algorithm(7)
    (True, 6)
    >>> division_algorithm(8)
    (False, 3)
    >>> division_algorithm(9)
    (True, 1)
    >>> division_algorithm(99)
    (True, 2)
    >>> division_algorithm(121)
    (True, 22)
    >>> division_algorithm(958)
    (True, 239)
    >>> division_algorithm(999)
    (True, 3)
    """
    assert n < 1000
    decimals = []
    dividend = 1
    divisor = n
    counter = 0
    repeating, repeating_length = False, 0
    while dividend != 0 and not repeating:
        dividend = dividend * 10
        #print(dividend,divisor,dividend // divisor)
        decimals.append(dividend // divisor)
        dividend = dividend % divisor
        counter += 1
        repeating, repeating_length = is_repeating(decimals)
    if repeating:
        counter = repeating_length
    return repeating, counter

def is_repeating(decimals):
    decs = deepcopy(decimals)
    while len(decs) > 4:
        if decs[0:len(decs)//2] == decs[len(decs)//2:]:
            #print(decs)
            if len(decs)//2 == 3 and decs[0] == decs[-1]:
                return True, 1
            elif len(decs)//2 == 4:
                return True, 2
            else:
                return True, len(decs)//2
        del decs[0]
    return False, 0

bar = progressbar.ProgressBar()
prev_max = 0
max_index = 0
current = 0
repeating_decimal = False
for i in bar(range(2,1000)):
    repeating_decimal, current = division_algorithm(i)
    if repeating_decimal and current > prev_max:
        prev_max = current
        max_index = i
print('1/{0} has a repeating decimal length {1}'.format(max_index, prev_max))
