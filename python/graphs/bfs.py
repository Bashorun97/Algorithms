#!/usr/env/bin python
from collections import defaultdict

net = defaultdict(list)

graph = {'A': ['B', 'E', 'C'],
        'B': ['D', 'E', 'A'],
        'E': ['D', 'B', 'A'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'F': ['C'],
        'G': ['C']
        }


# dynamically add nodes and children
def add_nodes_and_edges(node, child):
    net[node].append(child)

# all the nodes of a graph
def bfs_traverse(graph, start):

    #keep track of all visited nodes
    explored = []

    # keep track of unvisited nodes
    queue = [start]

    # keep looping until there are no node in the queue
    while queue:

        #pop first node from queue
        node = queue.pop(0)
        
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
            
            for neighbour in neighbours:
                queue.append(neighbour)
            
    print('Successfully traversed graph')
    return explored

def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return 'found out'

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]
            print(node)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                print(new_path)
        
                if neighbour == goal:
                    return new_path
                
            explored.append(node)

    return 'no connecting passage found'

add_nodes_and_edges(0, 1)
add_nodes_and_edges(0, 2)
add_nodes_and_edges(1, 2)
add_nodes_and_edges(2, 0)
add_nodes_and_edges(2, 3)
add_nodes_and_edges(3, 3)

#print(bfs_traverse(graph, 'A'))
print(bfs_shortest_path(graph, 'G', 'D'))
