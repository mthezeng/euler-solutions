"""
Acknowledgements:
I owe a lot of thanks to Red Blob Games for their awesome
instructional pages about pathfinding:
https://www.redblobgames.com/pathfinding/grids/graphs.html
https://www.redblobgames.com/pathfinding/a-star/implementation.html

This implementation uses Dijkstra's algorithm, but I think it still has to
go through every possible path, so we'll need to do some tweaking for heavy
duty triangles, like the one in Problem 67 of Project Euler.
"""

from queue import PriorityQueue
from copy import deepcopy
from timer import timed

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
        self.costs.append([0]) # cost of 0 for the final (16,1) node

    def neighbors(self, node):
        directions = [[1, 0], [1,1]]
        result = []
        for d in directions:
            result.append((node[0] + d[0], node[1] + d[1]))
        if result[0][0] > 15 or result[1][0] > 15:
            return [(16,1)]
        else:
            return result

    def cost(self, to_node):
        #returns cost associated with moving away from to_node
        return self.costs[to_node[0] - 1][to_node[1] - 1]

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

        #print("Visiting {0}".format(current))
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)
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
    path.append(start)
    path.reverse()
    return path

@timed
def main():
    the_graph = Graph()
    dijkstra_nodes, dijkstra_costs = dijkstra(the_graph, (1,1), (16,1))
    nodes_visited = reconstruct_path(dijkstra_nodes, (1,1), (16,1))
    print('Maximum path had a sum of: {0}'.format(dijkstra_costs[(16,1)]))
    print('The path taken was: {0}'.format(nodes_visited))

main()
