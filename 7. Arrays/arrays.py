from array import *
# --------------------------------------------------------------------------
# Accessing an element
# --------------------------------------------------------------------------
# def accesselement(array, index):
#     if index >= len(array) or index < 0:  # OR       #if index > len(array) - or index < 0
#         print('Wrong index')
#     else:
#         print(array[index])


# array1 = [1, 2, 3, 4, 5]
# index = 5
# print(accesselement(array1, index))


# --------------------------------------------------------------------------
# Searching for an element in Array
# --------------------------------------------------------------------------
# array = [2,4,6,7,8]

# def searchelement(arr, element):
#     for i in range(len(arr)):
#         if arr[i] == element:
#             return i
#     return -1
        
# print(searchelement(array, 7))

# --------------------------------------------------------------------------
# Traversing 
# --------------------------------------------------------------------------
# def traverse(array):
#     for i in array:
#         print(i)

# array1 = [1, 2, 3, 4, 5]
# print(traverse(array1))

# --------------------------------------------------------------------------
# Delete an element 
# --------------------------------------------------------------------------

def deleteAnElement(arr, element):
    arr.remove(element)

array = [2,4,6,78,9]
print(deleteAnElement(array, 6))
print(array)