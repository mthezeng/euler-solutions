import numpy as np

def build():
    x = np.genfromtxt('num.txt',dtype="str",delimiter="\n").flatten()
    x = list(map(int,"".join(x)))
    return x

def thirteen_runs(num):
    


num = build()
runs = thirteen_runs(num)
print(find_largest_product(runs))
