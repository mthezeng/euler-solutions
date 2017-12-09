"""Attribution:
I owe a lot of thanks to Red Blob Games for their awesome
instructional pages about pathfinding:
https://www.redblobgames.com/pathfinding/grids/graphs.html
https://www.redblobgames.com/pathfinding/a-star/implementation.html"""

import numpy as np
from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.costs = np.genfromtxt('triangle.txt', dtype="int", delimiter=['\n', ' ']).T
        self.nodes = []
        counter = 0
        for r in range(15):
            for c in range(r):
                self.nodes.append([r, c, self.costs[counter]])
                counter += 1
        self.finalcounter = counter

    def neighbors(self, node):
        directions = [[1, 0], [1,1]]
        result = []
        for d in directions:
            result.append([node[0] + d[0], node[1] + d[1]])
        if result[0][0] > 15 or result[1][0] > 15:
            return [[16,1, self.finalconter]]
        else:
            return result

    def cost(from_node, to_node):
        #returns cost of moving to to_node
        return self.nodes[np.where(self.nodes[,0:2] == to_node)][2]

def breadth_first_search1(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start)
    came_from = []
    cost_so_far = 75

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        print("Visiting {0}".format(current))
        for next in graph.neighbors(current):
            new_cost = cost_so_far + graph.cost(next)
            if graph.cost(next) :
                frontier.put(next)
                came_from.append(next)

the_graph = Graph()
breadth_first_search1(the_graph, [1,1], [16,1])
