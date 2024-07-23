
#! Single Source Shortest Path Problem
#  A single source problem is about finding a path between a given vertex(source) to all the other vertices in a graph such that distance between them(source and destination) is minimum

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


    #? Problem:
    #  - Five offices in different cities.
    #  - Travel costs between cites are known.
    #  - Find the cheapest way from head office to branches in different cities.

    #* BFS
    #  Algorithm
    #  enqueue any starting vertex
    #          while the queue is not empty:
    #                p = dequeue()
    #                if p is unvisited:
    #                    mark it visited
    #                    enqueue all adjacent unvisited vertices
    #                    update parent of adjacent vertices to currentvertex 
    #!  Doesn't work with weighted graph
        
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)



customDict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"]
}

newGraph = Graph(customDict)
print(newGraph.bfs("a", "f"))
#* Dijkstra's Algorithm
#* Bellman Ford