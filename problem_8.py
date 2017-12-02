import numpy as np
from copy import deepcopy

def build():
    x = np.genfromtxt('num.txt',dtype="str",delimiter="\n").flatten()
    x = list(map(int,"".join(x)))
    return x

def thirteen_runs(num_string):
    #throws out thirteen runs that contain zero
    runs_list = []
    current_run = []
    for n in num_string:
        if n != 0:
            if len(current_run) < 13:
                current_run.append(n)
            else:
                #print('Before: ',runs_list)
                runs_list.append(deepcopy(current_run))
                del current_run[0]
                current_run.append(n)
                #print('After: ',runs_list)
        else:
            if len(current_run) == 13:
                #print('Before: ',runs_list)
                runs_list.append(deepcopy(current_run))
                #print('After: ',runs_list)
            current_run = []
    return runs_list

def find_largest_product(list_of_runs):
    products_list = []
    current_run_list = list_of_runs[0]
    for i in range(len(list_of_runs)):
        current_run_list = list_of_runs[i]
        product = 1
        for n in current_run_list:
            product = product * n
        products_list.append(deepcopy(product))
        #print(products_list)
    return max(products_list)


num = build()
runs = thirteen_runs(num)
print(find_largest_product(runs))
