from math import factorial
from functools import reduce
import time

def find_pos(pos,index,index_list):
    # half-recursive, half-iterative solution
    if index == 0:
        index_list.append(0)
        return index_list
    else:
        counter = 0
        new_pos = pos
        while new_pos < 1000000:
            pos = new_pos
            new_pos += factorial(index)
            counter += 1
        index_list.append(counter)
        find_pos(pos,index-1, index_list)
    return index_list

def find_pos_iter():
    # fully iterative solution
    index_list = []
    i = 9
    pos = 0
    while i:
        counter = 0
        new_pos = pos
        while new_pos < 1000000:
            pos = new_pos
            new_pos += factorial(i)
            counter += 1
        index_list.append(counter)
        i -= 1
    index_list.append(0)
    return index_list

def create_permutation(factorial_list):
    # with thanks to Teemu for showing me how to use the reduce function
    nums = list(range(10))
    result = []
    for n in factorial_list:
        result.append(nums.pop(n-1))
    result_string = reduce(lambda i, j: str(i) + str(j), result, '')
    return int(result_string)

# half-recursive, half-iterative solution
t = time.time()
print(create_permutation(find_pos(0,9,[])))
print('Executed in {0} seconds.'.format(time.time() - t))

# fully iterative solution
t = time.time()
print(create_permutation(find_pos_iter()))
print('Executed in {0} seconds.'.format(time.time() - t))
