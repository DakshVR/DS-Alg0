
#! Minimum Spanning Tree
#?  A minimum spnaning tree (MST) is a subset of the edges of connected, weighted and undirected graph which:
#*      Connects all vertices together
#*      No cycle
#*      Minimum total edge

#? Real life problem
#  Connecte 5 island wirh bridges
#  Cost of the bridges between island varies based on different factors
#  Which bridge should be constructed so that all island are accessible and the cost is minimum


#! Disjoint Set
#  It is a data structure that keeps track of set of elements which are partitioned into a number of disjoint and non overlapping sets and each sets have representative which helps in identifying that sets.
#*  Make Set
#   Used to create initial set. makeSet(N)

#*  Union(x, y):
#   Merge two given sets

#*  Find Set(x)
#   Returns the set name in which this element is there

#! Disjoint in Python

class DisjointSet:                         #! ------------> TC = O(N), SC = O(N)
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:             # ----------> O(n), 
            self.parent[v]  = v
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        
    
vertices = ["A", "B", "C", "D", "E"]

ds = DisjointSet(vertices)
ds.union("A", "B")
print(ds.find("B"))