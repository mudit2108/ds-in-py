# An implementation of Graph data structure with Python

## What is a Graph
A graph is a data structure which has connections between nodes. 
There are two types of graph viz.
1. Directed graph i.e. (u, v) is not equal to (v, u) where v and u are two vertices/nodes
2. Un-Directed graph i.e. (u, v) is equal to (v, u) where v and u are two vertices/nodes

A graph has the following two components

1. Vertices/Nodes is the data
2. Edge/Arc is a relationship between two nodes. These edges can be weighted. 

Consider a network of computers ie internet with each computer being a node and the connection between them an edge/arc.
Another example would be google maps application wherein each turn or end of the road can be a node and the road being an edge. The traffic or length of the road can be the weight of the edge which helps in calculation of the most optimum route.

There are two representations of a graph
1. Adjacency Matrix
2. Adjacency List

Adjacency Matrix is 2-D array of size V x V where V is the number of vertices. A slot with a non zero value indicates a connection/edge between the vertex i and j. Adjacency Matrix consumes more space, even if the edges are less it consumes the same space if every vertex is connected to every other vertex. Edge identification i.e. if there is an edge between two vertex is fast.

Adjacency List is a list/array of Linked List. The size of the list/array is equal to the number of vertex. This consumes lesser space than Adjacency Matrix but takes more time to create and find an edge.