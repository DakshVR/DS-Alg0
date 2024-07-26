
#! Floyd Warshall

# Algorithm
# IF D[sourceVer][Destination] > D[source][ViaX] + D[ViaX][Desti]:
#    D[sourceVer][Destination] = D[source][ViaX] + D[ViaX][Desti]

#? Why do we need?
#  Iterate V times.

#!  How may ways?
#*  The vertex is not reachable
#*  Two vertices are directly connected.
#       This is the best solution
#       Can be improved via other vertwx
#*  Two vertices are connected via other vertex

#! Floyd Warshall with Negative Cycle: Doesn't work
#* To go through cycle we need to go via negative cycle participating vertex at least twice.
#* FW never runs loop twice via same vertex
#* Hence, FW can never detect a negative cycle.

INF = 9999
def print_solution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

def floydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    print_solution(nV, distance)


G = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1],
    ]

floydWarshall(4, G)

# ! Single Source Shortest Path Algorithm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# * Graph Type                       #    BFS   #  Dijksta  #  Bellman # Floy #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Unweighted - undirected            #    OK    #    OK      #      OK        #
# Unweighted - directed              #    OK    #    OK      #      OK        #
# Positive - weighted - undirected   #     X    #    OK      #      OK        #
# Positive - weighted - directed     #     X    #    OK      #      OK        #
# Negative - weighted - undirected   #     X    #    OK      #      OK        #
# Negative - weighted - directed     #     X    #    OK      #      OK        #
# Negative Cycle                     #     X    #     X      #      OK    X   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #