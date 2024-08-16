
#! What is Divide and Conquer Algorithm?
#  Divide and conqure algorithm design paradigm which works by recursively breaking down a problem into subproblems of similar types, until these become simple enough to be solved directly. The solutions to the subproblems are combined to give a solution to the original problem.

#? Property of Divide and Conqure Algorithm

# Optimal Solution
# If any probelm's overall optimal solution can be constructed from the optimal solutions of its subproblem then this problem has optimal solution.

#? Why we need it?
#  It is very effective when the problem has optimal substructure property


#*##############################################################################################################################################################################################################################################################################################################################

#? Common Divide and conqure algorithms
#  
#   Merge Sort
#   Quick Sort

#*##############################################################################
#! Fibonacci Series
#  Fib(N) = Fib(N-1) + Fib(N-2)
#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################
#! Number Factor
#  Given N, find the number of ways to express N as a sum of 1, 3 and 4.

# Example:
#        N = 4, Number of ways = 4
#   {4}, {1,3}, {3,1}, {1,1,1}

# Example:
#       N = 5, Number of ways = 6
#   {4,1}, {1,4}, {1,3,1}, {3,1,1}, {1,1,3}, {1,1,1,1,1}

def numFactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numFactor(n-1)
        subP2 = numFactor(n-3)
        subP3 = numFactor(n-4)
        return subP1 + subP2 + subP3

num = numFactor(5)
print(f"Num Factor: {num}")

#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################

#! House Robber
#  Given N number of houses along the street with some money
#  Adjacent houses cannot be stolen
#  Find the maximum amount that can be stolen

# Example:
#  [6,7,1,30,8,2,4]
#  House that are stolen for maximum amount = [7,30,4] = 41

def houseRobber(houses, currentindex):
    if currentindex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentindex] + houseRobber(houses, currentindex + 2)
        skipFirstHouse = houseRobber(houses, currentindex + 1)
        return max(stealFirstHouse, skipFirstHouse)
    
houses = [6,7,1,30,8,2,4]
maxAmount = houseRobber(houses, 0)
print(f"Maximum Amount after stealing: {maxAmount}")

#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################

#! Convert String
#   S1 and S2
#   Convert S2 to S1 using deletion, insertion or replace
#   Find the minimum count of edit operations

#  Example:
#   S1 = "catch"
#   S2 = "carch"
#   Output = 1
#   Replace "r" with "t"

#  Example:
#   S1 = "table"
#   S2 = "tbres"
#   Output = 3
#   Replace Insert "a" to second position, replace "r" with "l", delete "s"


def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1 + 1, index2 + 1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1)
        addOp = 1 + findMinOperation(s1, s2, index1 + 1, index2)
        replace = 1 + findMinOperation(s1, s2, index1 + 1, index2 + 1)
        return min(deleteOp, addOp, replace)
        
s1 = "table"
s2 = "tbrles"
answer = findMinOperation(s1, s2, index1=0, index2=0)
print(f"Minimum Operation to Match 2 strings: {answer}")

#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################

#! Zero One Knapsack Problem
#   Given the weights and profits of N items
#   Find the maximum profit within given capacity of C
#   Items cannot be broken

# Example 1:
#   Mango: weight = 3, Profit = 31
#   Apple: weight = 1, Profit = 26
#   Orange: weight = 2, Profit = 17
#   Banana: weight = 5, Profit = 72
# 
#   Answer:
#   Mango(W:3,P:31) + Apple(W:1,P26) + Orange(W:2,P:17) = W:6, Profit:74
#   Banana(W:5,P:72) + Orange(W:2,P:17) = W:7, Profit:89
#*   Apple(W:1,P26) + Banana(W:5,P:72) = W:6, Profit:98

#   Subproblem:
#   Option1 = 31 + f(2,3,4)
#   Option2 = 0 + f(2,3,4)
#   Take max of (option1, option2)


class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
    
def zoKnapSack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapSack(items, capacity - items[currentIndex].weight, currentIndex + 1)
        profit2 = zoKnapSack(items, capacity, currentIndex + 1)
        return max(profit1, profit2)
    else:
        return 0
    
mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]
answer = zoKnapSack(items, 7, 0)
print(f"Maximum profits from items: {answer}")

items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
answer2 = zoKnapSack(items, capacity, 0)
print(f"Maximum profits from items: {answer2}")

#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################


#! The Longest Common Subsequence (LCS)
#   S1 and S2 are given strings
#   Find the length of the longest subsequence which is common to both string
#   Subsequence: a sequence that can be driven from another sequence by deleting some elements without changing the order of them

#  Example:
#   ABCDE   ACE, ADE, ACB
#           ABCE, ABDE

#  Example:
#       S1 = "elephant"
#       S2 = "erepat"
#       Output = 5, "eepat"

#   Subproblem:
#       Option1 = 1 + f(2,8 : 2,7)
#       Option2 = 0 + f(3,8 : 2,7)
#       Option3 = 0 + f(2,8 : 3,7)
#       max(option1, option2, option3)

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1 + 1, index2 + 1)
    else:
        opt1 = findLCS(s1, s2, index1 + 1, index2)
        opt2 = findLCS(s1, s2, index1, index2 + 1)
        return max(opt1, opt2)


S1 = "elephant"
S2 = "eretpat"
lcs = findLCS(S1, S2, 0, 0)
print(f"The Longest Common Subsequence (LCS) is: {lcs}")

#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################

#! Longest Palindromic Subsequence (LPS)
#   S is a given string
#   Find the logest palindromic subsequence(LPS)
#   
#   Example:
#          S = "ELRMENMET"
#           Output = 5
#           LPS: "EMEME"

#   Example:
#          S = "AMEEWMEA"
#           Output = 6
#           LPS: "AMEEMA"
#   Subproblem:
#           Option1: 2 + f(2,8)
#           Option2: 0 + f(1,8)
#           Option3: 0 + f(2,9)
#       max(option1, option2, option3)

def LPS(string, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif string[startIndex] == string[endIndex]:
        return 2 + LPS(string, startIndex + 1, endIndex -1)
    else:
        option1 = LPS(string, startIndex, endIndex -1)
        option2 = LPS(string, startIndex + 1, endIndex)
        return max(option1, option2)

string = "AMEEWMEA"
lps = LPS(string , 0, 7)
print(f"The Palindromic Subsequence (LPS) is: {lps}")

#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################

#! Minimum cost to reach the last cell
#   2D matrix is given
#   Each cell has a cost associrated with it for accessing
#   We need to start from (0,0) and go till (n-1, n-1) cell
#   We can go only to right or down cell from current cell
#   Find the way in which the cost is minimum

#   Example:
#    _____________________________   
#   |  4  |  7  |  8  |  6  |  4  |
#   |  6  |  7  |  3  |  9  |  2  |
#   |  3  |  8  |  1  |  2  |  4  |
#   |  7  |  1  |  7  |  3  |  7  |
#   |  2  |  9  |  8  |  9  |  3  |
#    -----------------------------
# 
#    Min cost = 36

#   Subproblem:
#       option1 = y + 9 + 3  f(4,3)
#       option2 = z + 7 + 3  f(3,4)
#       min(option1, option2)

def findMinCost(twoDarray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDarray[row][col]
    else:
        option1 = findMinCost(twoDarray, row-1, col)
        option2 = findMinCost(twoDarray, row, col-1)
        return twoDarray[row][col] + min(option1, option2)

twoDList = [
    [4,7,8,6,4],
    [6,7,3,9,2],
    [3,8,1,2,4],
    [7,1,7,3,7],
    [2,9,8,9,3 ]
]
minCost = findMinCost(twoDList, 4, 4)
print(f"The Minimum cost from start to end is: {minCost}")

#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################

#! Number of paths to reach the last cell with given cost
#   2D matrix is given
#   Each cell has a cost associated with it for accessing.
#   We need to start from (0,0) cell and go till (n-1, n-1) cell
#   We can go only to right or down cell from current cell
#   We are given total cost to reach the last cell
#   Find the number of ways to reach end of matrix with given "total cost"

#   Example:
#   _________________________  
#   |  4  |  7  |  1  |  6  |
#   |  5  |  7  |  3  |  9  |
#   |  3  |  2  |  1  |  2  |
#   |  7  |  1  |  6  |  3  |
#   -------------------------
#   Need to go from 4 to 3, total cost: 25

#  Subproblem:
#       Option1: y + 2 = 22    f(3,4,22)
#       Option2: z + 6 = 22    f(4,3,22)
#       sum(option1, option2)

def numOfPaths(twoDarray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDarray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numOfPaths(twoDarray, 0, col - 1, cost - twoDarray[row][col])
    elif col == 0:
        return numOfPaths(twoDarray, row - 1, 0, cost - twoDarray[row][col])
    else:
        option1 = numOfPaths(twoDarray, row - 1, col, cost - twoDarray[row][col])
        option2 = numOfPaths(twoDarray, row, col - 1, cost - twoDarray[row][col])
        return option1 + option2
    
twoDArray = [
    [4,7,1,6],
    [5,7,3,9],
    [3,2,1,2],
    [7,1,6,3],
    ]
path = numOfPaths(twoDArray, 3, 3, 25)
print(f"The number of path from start to end is: {path}")