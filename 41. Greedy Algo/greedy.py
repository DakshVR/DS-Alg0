
#! What is greedy Algorithm?
# It is an algorithmic paradigm that builds the solution piece by piece.
# It  each step it chooses the piece that offers most obvious and immediate benefit.
# It fits perfectly for those solutions in which local optimal solutions lead to global solution

#? Already Known Greedy Algorithm 
#  Insertion Sort
#  Selection Sort
#  Topological Sort
#  Prim's Algoritm
#  Kruskal Algorithm

#!  Activity Slection Problem
#   Given N number of activities qith their start and end times. We need to select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#!  Activity  #   A1   #   A2   #   A1   #   A2   #   A1   #   A2   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#*  Start     #   0    #   3    #   1    #   5    #   5    #   8    # 
#*  Finish    #   6    #   4    #   2    #   8    #   7    #   9    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#? Pseudocode
#  Sort activities based on finish time:
#  Select first activity from sorted array and print it
#  for all remaining activities:
#      If the start time of this activity is greater or equal to the
#      finish time of previously selected activity then select this
#      activity and print it

activities =[
    ['A1', 0, 6],
    ['A2', 3, 4],
    ['A3', 1, 2],
    ['A4', 5, 8],
    ['A5', 5, 7],
    ['A6', 8, 9],
]

def printMaxActivities(activities):
    activities.sort(key= lambda x: x[2])
    i = 0
    firstActivity = activities[i][0]
    print(firstActivity)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j
    
print(printMaxActivities(activities))

#  Coin Change problem
#  Fractional Knapsaack Probelm

