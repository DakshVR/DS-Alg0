
import mst as dst

#! Kruskal's Algorithm
#   It is s greedy algorith,
#   It finds a minimum spanning tree for weighted undirected graphs in two ways:
#           - Add increasing cost edges at each step
#           - Avoid any cycle at each step

#* Pseudocode
#  Kruskal(G):
#  for each vertex:                                    -------------------> O(v)
#       makeSet(v)
#  sort each edge in non decreasing order by weight-------------------> O(eLogE)
#  for each edge(u, v):          -------------------> O(e)
#       if findSet(u) != findSet(v): ---------------> O(1)   ------------> O(EV)
#          union(u, v)           -------------------> O(v)
#       cost = cost + edge(u,v)     ----------------> O(1)

#? Time Complexity: O(V+ ElogE + EV) = O(Elog(E))
#? Space Complexity: O(V+E)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []
    
    def addEdge(self, s, d, w):
        self.graph.append([s,d,w])
    
    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))
    
    def kruskalAlgo(self):
        i, e = 0, 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key= lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "D", 8)
g.addEdge("B", "C", 10)
g.addEdge("B", "A", 5)
g.addEdge("D", "C", 6)
g.addEdge("D", "B", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("E", "C", 20)
g.addEdge("E", "A", 15)

g.kruskalAlgo()

#! Landing Cables
#! TV Network
#! Tour Operations
#! LAN Network
#! A network of pipes for drinking water of natural gas
#! An electric grid
#! Single-link Cluster