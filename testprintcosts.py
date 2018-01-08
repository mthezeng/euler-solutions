from copy import deepcopy

costsfile = open('triangle.txt')
costs = []
for r in range(15):
    current_row = []
    for c in range(0,r+1):
        seek_position = c * 3
        for r_temp in range(0,r+1):
            seek_position += 3 * r_temp
        costsfile.seek(seek_position)
        current_row.append(int(costsfile.read(2)))
    costs.append(deepcopy(current_row))
print(costs)

"""
import numpy as np

costs = np.genfromtxt('triangle.txt', dtype='int')
print(costs)
#self.costs = np.genfromtxt('triangle.txt', dtype="int", delimiter=['\n', ' ']).T


return self.nodes[np.where(self.nodes[,0:2] == to_node)][2]
"""
