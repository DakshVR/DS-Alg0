# Day 1: 11, 15, 10, 6
# Day 2: 10, 14, 11, 5
# Day 3: 12, 17, 12, 8
# Day 4: 15, 18, 14, 9

import numpy as np

# ################################
#  Creating an empty array
# Space complex: O(n*m)
# Time Complex: O(n*n)
# ################################

# ################################
#  Creating an array with element
# ################################

# Space complex: O(n*m)
# Time Complex: O(n*n)
# twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

# print(twoDArray)

# ################################
#  INSERTION
# ################################

##############################################################
# Axis=1 adds colums, and axis = 0 adds row.

#####
# Adding Column -      
# Time Complex: O(nm)
# Space Complex: O(nm)
####
# newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)
# print(newTwoDArray)

#####
# Adding Row -      Time Complex: O(nm)
####
# newTwoDArray = np.insert(twoDArray, 2, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

########
# Append to add it to the end
#######
# newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

##############################
# Accessing Elements in 2D array
##############################
# twoDArray[i][j]
#  i is the row and j is column

# Time Complexity:  O(1)
# Space Complexity: O(1)
# def accessElement(arr,x,y):
#     if x >= len(arr) or y>= len(arr[0]):
#         return print("Incorrect indexes")
#     print(arr[x][y])

# accessElement(twoDArray,6,1)

##############################
# Traversing 2D array
##############################

# Time Complexity:  O(mn)
# Space Complexity: O(1)
# def traverse(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])

# traverse(twoDArray)

##############################
# Search for an element in 2D array
##############################

# Time Complexity:  O(mn)
# Space Complexity: O(1)
# def searchelement(array, element):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == element:
#                 return print("Success")
#     print("Not Found")

# searchelement(twoDArray, 115)

##############################
# Deletion of row or column in 2D array
##############################

# Time Complexity:  O(mn)
# Space Complexity: O(mn)
# result = np.delete(twoDArray, 0, axis=0)
# print(" ")
# print(result)
# result = np.delete(twoDArray, 0, axis=1)
# print(" ")
# print(result)

# When to use array
# To store multiple variables of same data type
# Random access
#


def rotate(matrix):
    n = len(matrix)
 
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row
    
    

lista=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(lista))