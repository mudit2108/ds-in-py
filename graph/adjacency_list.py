'''
    A short program to implement graph in python using adjacency list
    A vertex(node) is the data 
    An edge/arc is relationship between two nodes
        An edge can be weighted
'''

class AdjNode:
    # A linked list to implement adjacency list
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    # A graph is a list of linked lists or a list of adjacency lists.
    # Size of the list holding linked lists is the number of vertices
    def __init__(self, vertices):
        self.size = vertices
        self.graph = [None] * self.size
    
    # Add an edge between two vertices
    def add_edge(self, src, dest):
        # Add node to source linked list
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Add a node to destination linked list as it is an undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    
    def print_graph(self):
        for i in range(self.size):
            print("Adjacency list of vertex {}\n head". format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")

if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.print_graph()