import numpy as np
import string

def names_scores(names):
    scores = np.array([])
    pos = 1
    for a in names:
        s = 0
        for x in range(len(a)):
            s += string.ascii_uppercase.index(a[x]) + 1
        s = s * pos
        scores = np.append(scores,s)
        #print(scores)
        pos += 1
    return np.sum(scores)

names_list = np.genfromtxt('p022_names.txt', dtype='str', delimiter='","')
names_list = np.sort(names_list)
print(names_list)
print(names_scores(names_list))
