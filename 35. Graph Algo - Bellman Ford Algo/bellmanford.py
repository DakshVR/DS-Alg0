
#! Bellman Ford Algorithm
#  Bellman ford algorithm is used to find single source shortest path problem. If there is a negative cycle it catches it and report its existence.

#? If the distance of the destination vertex > (dist of source vertex + weight btwn source and destination vertex):
#?              Update dist of destination vertex to (dist of source vertex +               weight bwtn source and destination vertex)

#! Why does Bellman Ford run v-1 times?
#* IF any node is achieved better distance in previous iteration, then that better distance is used to improve distance of other vertices.

# ! Single Source Shortest Path Algorithm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# * Graph Type                       #    BFS   #   Dijksta  #  Bellman Ford  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Unweighted - undirected            #    OK    #    OK      #      OK        #
# Unweighted - directed              #    OK    #    OK      #      OK        #
# Positive - weighted - undirected   #     X    #    OK      #      OK        #
# Positive - weighted - directed     #     X    #    OK      #      OK        #
# Negative - weighted - undirected   #     X    #    OK      #      OK        #
# Negative - weighted - directed     #     X    #    OK      #      OK        #
# Negative Cycle                     #     X    #     X      #      OK        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)
    
    def print_solution(self, dist):
        print("Vertex distance from Source")
        for key, value in dist.items():
            print(' ' + key, ': ', value)
    
    def bellmanFord(self, source):        #! ------------> TC = O(EV), SC = O(V)
        dist = {i: float('inf') for i in self.nodes}   # ------------> TC = O(V)
        dist[source] = 0

        for _ in range(self.v-1):                      # ------------> TC = O(V)
            for s, d, w in self.graph:                 # ------------> TC = O(E)
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        for s, d, w in self.graph:                     # ------------> TC = O(E)
            if dist[s] != float('inf') and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                return

        self.print_solution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)

g.bellmanFord("E")