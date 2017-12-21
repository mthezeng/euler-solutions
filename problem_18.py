"""
INCOMPLETE.

Attribution:
I owe a lot of thanks to Red Blob Games for their awesome
instructional pages about pathfinding:
https://www.redblobgames.com/pathfinding/grids/graphs.html
https://www.redblobgames.com/pathfinding/a-star/implementation.html
"""

import numpy as np
from queue import Queue

class Graph:
    def __init__(self):
        #self.costs = np.genfromtxt('triangle.txt', dtype="int", delimiter=['\n', ' ']).T
        self.nodes = []
        for r in range(15):
            for c in range(r):
                self.nodes.append([r, c])

    def neighbors(self, node):
        directions = [[1, 0], [1,1]]
        result = []
        for d in directions:
            result.append([node[0] + d[0], node[1] + d[1]])
        if result[0][0] > 15 or result[1][0] > 15:
            return [[16,1]]
        else:
            return result

    """def cost(self, from_node, to_node):
        #returns cost of moving to to_node
        return self.nodes[np.where(self.nodes[,0:2] == to_node)][2]"""

def breadth_first_search1(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    visited = []

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        print("Visiting {0}".format(current))
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
            visited.append(next)

the_graph = Graph()
breadth_first_search1(the_graph, [1,1], [16,1])
