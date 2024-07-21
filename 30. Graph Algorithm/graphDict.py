
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

customGraph = Graph()
customGraph.addvertex("A")
customGraph.addvertex("B")
customGraph.addvertex("C")
print(customGraph.addEdge("A", "B"))
print(customGraph.addEdge("A", "C"))
print(customGraph.addEdge("B", "C"))
customGraph.print_graph()
print(customGraph.removeEdge("A", "C"))
customGraph.print_graph()

# graph = Graph(customDict)
# print(graph.gdict)
# graph.addEdge("e", "c")
# print(graph.gdict["a"])