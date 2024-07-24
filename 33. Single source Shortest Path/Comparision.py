
# ! Single Source Shortest Path Algorithm

#?      BFS
#       Time Complexity:  O(V^2)
#       Space Complexity:  O(E)
#       Implementation:   Easy
#       Limitation:       doesn't work with weighted graph
#       Unweighted Graph: OK
#*                        Use this as time complexity is good
#       Not supported for weighted and Negative cycle graph


#?      Dijkstra
#       Time Complexity:  O(V^2)
#       Space Complexity:  O(V)
#       Implementation:   Moderate
#       Limitation:       doesn't work with negative cycle graph
#       Unweighted Graph: OK
#*                        Not Use this as implementaion is not easy
#       weighted graph:   OK
#*                        Use as time complexity is better than Bellman
#       Not supported for Negative cycle graph

#?      Bellman Ford
#       Time Complexity:  O(VE)
#       Space Complexity:  O(V)
#       Implementation:   Moderate
#       Limitation:       No Limitations
#       Unweighted Graph: OK
#*                        Not Use this as time complexity is bad
#       weighted graph:   OK
#*                        Not Use this as time complexity is bad
#       Negative Cycle:   OK
#*                        Use as others don't support this
#       Not supported for Negative cycle graph