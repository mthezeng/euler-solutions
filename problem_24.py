from math import factorial
from functools import reduce

def find_pos(pos,index,index_list):
    counter = 0
    if index == 0:
        index_list.append(counter)
        return index_list
    new_pos = pos
    while new_pos < 1000000:
        pos = new_pos
        new_pos += factorial(index)
        counter += 1
    index_list.append(counter)
    find_pos(pos,index-1,index_list)
    return index_list

def create_permutation(factorial_list):
    # with thanks to Teemu for showing me how to use the reduce function
    nums = list(range(10))
    result = []
    for n in factorial_list:
        result.append(nums.pop(n-1))
    result_string = reduce(lambda i, j: str(i) + str(j), result, '')
    return int(result_string)

print(create_permutation(find_pos(0,9,[])))
