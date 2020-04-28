'use strict';

var graph = {'A':['D', 'E', 'C'], 'B':['D', 'E', 'A'],
'C':['D', 'C', 'A'], 'D':['C', 'E'], 'E':['D', 'C', 'A']};


function bfsTraverse (graph, start) {
  let nodeQueues = [start];
  let traversed = [];

  while(nodeQueues) {
    let node = nodeQueues.shift();
    if (!(node in traversed)) {

      traversed.push(node);
      console.log(`On node: ${node}`);
      
      let neighbours = graph[node];
      for(let neighbour=0;neighbour<neighbours.length;neighbour++) {
        nodeQueues.push(neighbours[neighbour]);
        
      }
    }
  }
  console.log(`Successfully traversed tree`);
  return traversed;
}
bfsTraverse(graph, 'A');