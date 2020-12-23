#!/usr/env/bin python
# Sun 10 Nov 2019 07:12:51 PM WAT
# Babaibeji

from collections import defaultdict

net = defaultdict(list)

graph = {'A': ['D', 'E', 'C'],
        'B': ['D', 'E', 'A'],
        'C': ['D', 'C', 'A'],
        'D': ['C', 'E'],
        'E': ['D','C','A']
        }
        
# dynamically add nodes and children
def add_nodes_and_edges(node, child):
    net[node].append(child)

def bfs_traverse(graph, start):
  queue_of_nodes = [start]
  traversed = []

  while queue_of_nodes:

    nodes = queue_of_nodes.pop(0)
    if nodes not in traversed:
      traversed.append(nodes)
    
      for neighbours in graph[nodes]:
        queue_of_nodes.append(neighbours)
        print(queue_of_nodes)
  print(f'Successfully traversed tree')
  return traversed

#bfs_traverse(graph, 'A')

def shortest_path(graph, start, end):
  queue = [[start]]
  explored = []
  
  if start == end:
  	return f'Found out path: start => end'
  
  while queue:
    path = queue.pop(0)
    node = path[-1]

    if node not in explored:
      neighbours = graph[node]

      for neighbour in neighbours:
      	#create path
        new_path = list(path)
        #update path with latest neighbour
        new_path.append(neighbour)
        queue.append(new_path)

        if neighbour == end:
          return f'Found path at {new_path}!'
      explored.append(node)
  return f'Path doesn\'t exist'

add_nodes_and_edges(0, 1)
add_nodes_and_edges(0, 2)
add_nodes_and_edges(1, 2)
add_nodes_and_edges(2, 0)
add_nodes_and_edges(2, 3)
add_nodes_and_edges(3, 3)
#print(shortest_path(graph, 'B', 'A'))
print(bfs_traverse(graph, 'A'))
