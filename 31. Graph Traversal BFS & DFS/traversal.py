
from collections import deque

#! Adjacency 
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addvertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
    
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for othervertex in self.adjacency_list[vertex]:
                self.adjacency_list[othervertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    

    #! Breadth First Search - BFS
    #  Start at arbitery node and then go to adjacent nodes of current node

    """
    def BFS(self, vertex):
        visited = set()      # A set of visited node, performance of set is good
        visited.add(vertex)      # Add the current node to set of visited nodes 
        queue = [vertex]         # Explore the adjacent nodes
        while queue is not empty:
            current_vertex = queue.pop(0) # Get the 1st node
            print(current_vertex)         # Node is visited
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
    """
    
    def bfs(self, vertex):               #! ------------> TC = O(V+E), SC = O(V)
        visited = set()
        visited.add(vertex)                            # ------------> TC = O(1)
        queue = deque([vertex])                        # ------------> TC = O(1)
        while queue:                                   # ------------> TC = O(V)
            current_vertex = queue.popleft()           # ------------> TC = O(1)
            print(current_vertex)                      # ------------> TC = O(1)
            for adjacent_vertex in self.adjacency_list[current_vertex]:#TC =O(E)
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
    
    #! Depth First Search - DFS
    #  Start at arbitery node and then go to deepest node of current node

    """
    def DFS(self, vertex):
        visited = set()      # A set of visited node, performance of set is good
        stack = [vertex]         # First in Last out
        while stack is not empty:
            current_vertex = stack.pop()                    # Get the last node
            if current_vertex not in visted:
                print(current_vertex)                          # Node is visited
                visited.add(adjacent_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    if current_vertex not in visted: 
                        stack.append(adjacent_vertex)
    """
    def dfs(self, vertex):               #! ------------> TC = O(V+E), SC = O(V)
        visited = set()                                # ------------> TC = O(1)
        stack = [vertex]                               # ------------> TC = O(1)
        while stack:                                   # ------------> TC = O(V)
            current_vertex = stack.pop()               # ------------> TC = O(1)
            if current_vertex not in visited:          # ------------> TC = O(1)
                print(current_vertex)                  # ------------> TC = O(1)
                visited.add(current_vertex)            # ------------> TC = O(1)
            for adjacent_vertex in self.adjacency_list[current_vertex]:#TC =O(E)
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)


customGraph = Graph()
customGraph.addvertex("A")
customGraph.addvertex("B")
customGraph.addvertex("C")
customGraph.addvertex("D")
customGraph.addvertex("E")
customGraph.addEdge("A", "B")
customGraph.addEdge("A", "C")
customGraph.addEdge("B", "E")
customGraph.addEdge("C", "D")
customGraph.addEdge("D", "E")
customGraph.print_graph()
customGraph.dfs("A")



#!   BFS   VS   DFS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# *                             #        BFS          #          DFS          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# How does it work Internally?  #    Breath First     #      Depth First      #
# What DS it use Internally?    #        Queue        #          Stack        #
# Time Complexity               #       O(V+E)        #          O(V+E)       #
# Space Complexity              #       O(V+E)        #          O(V+E)       #
# When to use?                  #  If we know target  #   If we know target   #
#                               #  close to starting  #   is buried deep      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 