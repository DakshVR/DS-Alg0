
#! What is Dynamic Programming?
#  DP is analgorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall probelm depends upon the optimal solution to its subproblem.

# Example:
# 1 + 1 + 1 + 1 + 1 + 1 + 1 = 7
# Use 7 from above
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 = 9

#* Optimal Substructre:
#  If any problem's overall optimal solution can be constructed from the optimal solutions of its subproblem then this problem has optimal substructure

# Example: Fin(n) = Fin(n-1) + Fib(n-2) 

#* Overlapping Subproblems:
#  Subproblems are smaller versions of the orginal problem. Any problem has overlapping sub-problems if finding its solutions involves solving the same problem multiple times.

# Example: Fin(n) = Fin(n-1) + Fib(n-2)


#! Top Down with Memoization
#  Solve the bigger problem by recursively finding the solution to smaller subproblems. Whenever we solve the sub-problem, we cache its results so that we don't end up solving it repeatedly if its called multiple times. This technique of storing the results of already solved subproblems is called Memoization.

def fibMemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

myDict = {}
num = 6
fibMemoanswer = fibMemo(num, myDict)
print(f"FibMemo of {num} is {fibMemoanswer}")

#! Bottom Up with Tabulation
#  Tabulation is the opposite of top down approach and avoids recursion. In this approach, we solve the problem "bottom-up" (i.e by solving all the related subproblems first). This is done by filling up a table. Based on the results in the table, the solution to the top/original problem is then computed.

def fibTab(n):
    tb = [0, 1]
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])
    return tb[n-1]

num = 6
fibTab = fibTab(num)
print(f"fibTab of {num} is {fibTab}")


#! Top Down VS Bottom Up
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# *                  #  Divide and conquer  #  Top Down   #    Bottom Up      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Fibonacci Numbers  #   O(C^n)             #     O(n)    #       O(n)        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


#! Is merge Sort Dynamic Programming?
#  Does it have Optimal Substructure property?: Yes
#  Does it have Overlapping Subproblems property?: No



#*##############################################################################################################################################################################################################################################################################################################################
#*##############################################################################
#! Number Factor
#  Given N, find the number of ways to express N as a sum of 1, 3 and 4.

# Example:
#        N = 4, Number of ways = 4
#        {4}, {1,3}, {3,1}, {1,1,1}

# Example:
#       N = 5, Number of ways = 6
#       {4,1}, {1,4}, {1,3,1}, {3,1,1}, {1,1,3}, {1,1,1,1,1}

#! Top-Down Approach
#  Create temp array, hash, dict to save subproblems result

def numFactor(n, dp):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    elif n in dp:
        return dp[n]
    else:
        subP1 = numFactor(n-1, dp)
        subP2 = numFactor(n-3, dp)
        subP3 = numFactor(n-4, dp)
        dp[n] = subP1 + subP2 + subP3
    return dp[n]

myDict = {}
num = numFactor(5, myDict)
print(f"Num Factor: {num}")


