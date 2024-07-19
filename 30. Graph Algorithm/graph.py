
#! What is a Graph.
#  Graph consists of a finite set of Vertices(or Nodes) and set of Edges which connect a pair of nodes.

#! Why we need Graph.
#  It used to represent networks: path in city, circuit.


#? Terminology
#  Vertices(Vertex): Vertices are the nodes of the graph.
#  Edge: The edge is a line that connects pairs of vertices.
#  Unweighted graph: A graph which does not have a weight associated with any  edge
#  Weighted graph: A graph which has a weight asscoiated with any edge.
#  Undirected graph: In case the edges of the graph do not have a direction associated with them.  
#  Directed graph: If the edges in a graph have a direction assocated with them
#  Cyclic graph: A graph which has at least one loop
#  Acyclic graph: A graph with no loop
#  Tree: It is a special case of directed acyclic graph

#! Types of Graphs

#? Graph
#   | 
#   |--> Directed
#   |       |
#   |       |----> Weighted
#   |       |            |
#   |       |            |--> Positive
#   |       |            |--> Negative
#   |       |
#   |       |----> Unweighted
#   |
#   |--> Undirected
#   |       |
#   |       |----> Weighted
#   |       |            |
#   |       |            |--> Positive
#   |       |            |--> Negative
#   |       |
#   |       |----> Unweighted


#!  Graph Representation

#*  Adjacency Matrix: An Adjacency matrix is a square matrix or a 2D array. The elements of the matrxi indicate weather pairs of vertices are adjacent or not in the graph

#                               #  A  #  B  #  C  #  D  #  E  #   
#   A -- B                   A  #  0  #  1  #  1  #  1  #  0  # 
#   | \   \                  B  #  1  #  0  #  0  #  0  #  1  #  
#   |  \   E                 C  #  1  #  0  #  0  #  1  #  0  # 
#   |   \ /                  D  #  1  #  0  #  1  #  0  #  1  # 
#   C -- D                   E  #  0  #  1  #  0  #  1  #  0  # 


#*  Adjacency List: An adjacency list is a collection of unordered list used to represent a graph. Each list describes the set of neighbours of a vertex in the graph.

#   A -- B                A ---->  B ---->  C ---->  D
#   | \   \               B ---->  A ---->  E
#   |  \   E              C ---->  A ---->  D
#   |   \ /               D ---->  A ---->  C ---->  E
#   C -- D                E ---->  B ---->  D

#! If a graph is complete or almost complete we should use Adjacency Matrix
#! If the number of edges are few then we should use Adjacency List 

#*  In Python it is useful to use Adjacency List. We can use DIctinoary.
#*  Keys will be the Verticies(Nodes), 
#*  Values will be the Edges.

#   A -- B              { A : [B, C, D],
#   | \   \               B : [A, E],
#   |  \   E              C : [A, D],
#   |   \ /               D : [A, C, E],
#   C -- D                E : [B, D] }