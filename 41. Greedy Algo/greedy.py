
# #! What is greedy Algorithm?
# # It is an algorithmic paradigm that builds the solution piece by piece.
# # It  each step it chooses the piece that offers most obvious and immediate benefit.
# # It fits perfectly for those solutions in which local optimal solutions lead to global solution

# #? Already Known Greedy Algorithm 
# #  Insertion Sort
# #  Selection Sort
# #  Topological Sort
# #  Prim's Algoritm
# #  Kruskal Algorithm

# #!  Activity Slection Problem
# #   Given N number of activities qith their start and end times. We need to select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #!  Activity  #   A1   #   A2   #   A1   #   A2   #   A1   #   A2   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #*  Start     #   0    #   3    #   1    #   5    #   5    #   8    # 
# #*  Finish    #   6    #   4    #   2    #   8    #   7    #   9    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# #? Pseudocode
# #  Sort activities based on finish time:
# #  Select first activity from sorted array and print it
# #  for all remaining activities:
# #      If the start time of this activity is greater or equal to the
# #      finish time of previously selected activity then select this
# #      activity and print it

# activities =[
#     ['A1', 0, 6],
#     ['A2', 3, 4],
#     ['A3', 1, 2],
#     ['A4', 5, 8],
#     ['A5', 5, 7],
#     ['A6', 8, 9],
# ]

# def printMaxActivities(activities):    #! ------------> TC = O(NlogN), SC = O(1)
#     activities.sort(key= lambda x: x[2])           # ------------> TC = O(NlogN)
#     i = 0
#     firstActivity = activities[i][0]                   # ------------> TC = O(1)
#     print(firstActivity)
#     for j in range(len(activities)):                   # ------------> TC = O(N)
#         if activities[j][1] > activities[i][2]:
#             print(activities[j][0])
#             i = j
    
# print(printMaxActivities(activities))

# #  Coin Change problem
# #  Fractional Knapsaack Probelm




# #! Coin Change Problem
# #  You are given coins of different denominations and total amount of money. Find the minimum number of coins that you need to make up the given amount.

# #? Pseudocode
# #  Find the biggest coin that is less than the given number
# #  Add the coin to the result and subtract coin from the total
# #  if the V is equal to zero:
# #       print the result
# #  else:
# #       Sepeat step 2 and 3


# def coinChange(totalNumber, coins):
#     # Sort coins in descending order
#     coins.sort(reverse=True)
#     targetVal = totalNumber
#     result = []  # Store the coins used

#     for coinValue in coins:
#         while targetVal >= coinValue:
#             result.append(coinValue)  # Add coin to result
#             targetVal -= coinValue  # Subtract coin from target value

#         if targetVal == 0:
#             break

#     if targetVal > 0:
#         return "Not possible to make the target value with the given coins"
#     else:
#         return result

# coins = [1, 4, 5, 6, 7, 3, 40, 23, 45, 75]
# result = coinChange(70, coins)
# print("Coins used:", result)




# #! Fractional Knapsack Problem
# #  Given a set of items, each with a weight and a value, determine the number of each items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

# #? Pseudocode
# #  calculate the density or ratio of each item
# #  sort item based on density
# #  Take item with height ratio sequentially until weight allows
# #  Add the next item as much (fractional) as we can

# class Item:
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value
#         self.ratio = value / weight
    
# def knapSack(items, capacity):         #! ------------> TC = O(NlogN), SC = O(1)
#     items.sort(key=lambda x:x.ratio, reverse = True)
#     usedCapacity = 0
#     totalValue = 0
    
#     for i in items:
#         if usedCapacity + i.weight <= capacity:
#             usedCapacity += i.weight 
#             totalValue += i.value
#         else:
#             unusedWeight = capacity - usedCapacity
#             value = i.ratio * unusedWeight
#             usedCapacity += usedCapacity
#             totalValue += value
        
#         if usedCapacity == capacity:
#             break
    
#     print("Total Value Obtained "+ str(totalValue))

# itertem1 = Item(20, 100)
# itertem2 = Item(30, 120)
# itertem3 = Item(10, 60)

# cList = [itertem1, itertem2, itertem3]

# knapSack(cList, 50)