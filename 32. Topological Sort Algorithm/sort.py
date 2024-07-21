
#! Topological Sort
#  Sorts given acrions in such a way that if there is a dependency of one action on another, then the dependent action always comes later than its parent action.

#? Algorithm

""""
If a vertex depends on currentVertex:
    Go to that vertex and 
    then come back to currentVertex
else
    Push currentVertex to Stack
"""

from collections import defaultdict

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack): 
        #! ------------> TC = O(E), SC = O(V)
        visited.append(v)                              # ------------> TC = O(1)
        for i in self.graph[v]:                        # ------------> TC = O(E)
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)                            # ------------> TC = O(1) 
    
    def topologicalSort(self):         #! ------------> TC = O(E+V), SC = O(V+E)
        visited = []
        stack = []
        for k in list(self.graph):                   # ------------> TC = O(E+V)
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        print(stack)

customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")
customGraph.topologicalSort()