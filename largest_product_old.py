import numpy as np

def build():
    x = np.genfromtxt('num.txt',dtype="str",delimiter="\n").flatten()
    x = list(map(int,"".join(x)))
    return x

def thirteen_runs(num_string):
    #throws out thirteen runs that contain zero
    runs_list = []
    current_run = []
    for n in num_string[:39]:
        if n != 0:
            if len(current_run) < 13:
                current_run.append(n)
            else:
                runs_list.append(current_run)
                current_run.pop(0)
        else:
            if len(current_run) == 13:
                runs_list.append(current_run)
            current_run = []
    return runs_list

def find_largest_product(list_of_runs):
    products_list = []
    for i in range(len(list_of_runs)):
        current_run_list = list_of_runs[i]
        product = 1
        for n in current_run_list:
            product = product * n
        products_list.append(product)
    return max(products_list)


num = build()
runs = thirteen_runs(num)
print(find_largest_product(runs))
