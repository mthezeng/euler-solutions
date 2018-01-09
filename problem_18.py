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
from queue import PriorityQueue
from copy import deepcopy

class Graph:
    def __init__(self):
        self.costsfile = open('triangle.txt')
        self.costs = []
        for r in range(15):
            current_row = []
            for c in range(0,r+1):
                seek_position = c * 3
                for r_temp in range(0,r+1):
                    seek_position += 3 * r_temp
                self.costsfile.seek(seek_position)
                current_row.append(int(self.costsfile.read(2)))
            self.costs.append(deepcopy(current_row))
        self.costs.append([0])
        print(self.costs)

        self.nodes = []
        for r in range(1,16):
            for c in range(r):
                self.nodes.append((r, c)) # (r, c) is a tuple

    def neighbors(self, node):
        directions = [[1, 0], [1,1]]
        result = []
        for d in directions:
            result.append((node[0] + d[0], node[1] + d[1]))
        if result[0][0] > 15 or result[1][0] > 15:
            return [(16,1)]
        else:
            return result

    def find_parents(self, node): #not sure if needed
        directions = [[-1, -1], [-1, 0]]
        if node[1] == node[0]:
            del directions[1] #only one parent if node is on very right
        elif node[1] == 1:
            del directions[0] #only one parent if node is on very left
        result = []
        for d in directions:
            result.append((node[0] + d[0], node[1] + d[1]))
        return result

    def cost(self, to_node):
        #returns cost associated with moving away from to_node
        print(to_node)
        print(to_node[0] - 1)
        print(to_node[1] - 1)
        return self.costs[to_node[0] - 1][to_node[1] - 1]

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

def dijkstra(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, -75)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 75

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        print("Visiting {0}".format(current))
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)
            #print('Cost is: {0}'.format(new_cost - cost_so_far[current]))
            if next not in cost_so_far or new_cost > cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = 0 - new_cost
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

the_graph = Graph()
#breadth_first_search1(the_graph, (1,1), (16,1))
dijkstra = dijkstra(the_graph, (1,1), (16,1))
nodes_visited = reconstruct_path(dijkstra[0], (1,1), (16,1))
print(dijkstra[1][(16,1)])
print(nodes_visited)
