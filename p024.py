from math import factorial
from functools import reduce
from timer import timed

def find_pos():
    index_list = []
    pos = 0
    for i in range(9, -1, -1):
        counter = 0
        new_pos = pos
        while new_pos < 1000000:
            pos = new_pos
            new_pos += factorial(i)
            counter += 1
        index_list.append(counter)
    return index_list

@timed
def create_permutation(factorial_list):
    # with thanks to Teemu for showing me how to use the reduce function
    nums = list(range(10))
    result = []
    for n in factorial_list:
        result.append(nums.pop(n-1))
    result_string = reduce(lambda i, j: str(i) + str(j), result, '')
    return int(result_string)

print(create_permutation(find_pos()))
