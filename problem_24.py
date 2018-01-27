from math import factorial
from functools import reduce

def find_pos(pos,index,index_list):
    counter = 0
    if index == 0:
        index_list.append(counter)
        return pos
    new_pos = pos
    while new_pos < 1000000:
        pos = new_pos
        new_pos += factorial(index)
        counter += 1
    index_list.append(counter)
    pos = find_pos(pos,index-1,index_list)
    return index_list

def create_permutation(factorial_list):
    #factorial_list = [3, 7, 7, 3, 6, 2, 3, 2, 2]
    nums = list(range(10))
    result = []
    for n in factorial_list:
        result.append(nums.pop(n-1))
    result_string = reduce(lambda i, j: str(i) + str(j), result, '')
    return int(result_string)

print(create_permutation(find_pos(0,9,[])))
