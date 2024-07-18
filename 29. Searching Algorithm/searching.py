
import math

#! Linear Searching ( Sequential Search )
#  TC: O(N) , SC: O(1)

#* Linear Search
#  Create function with 2 parameters which are an array and a value
#  Loop through the array and check if the current array element is equal to the value
#  If it is return the index at which the element is found
#  If the value is never found return -1

def linearSearch(arr, value):        #! TC: O(N) , SC: O(1) 
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

arr = [3,4,5,6,7,2,3,5]
print(linearSearch(arr, 2))


#! Binary Searching (  Search )
#  Binary is faster than Linear search
#  Half of the remaining elements can be elemninated at a time, instead of eliminating them one by one
#? Binary Search only works for sorted arrays.

#* Binary Search
#  Create function with 2 parameters which are a sorted array and a value
#  Create 2 pointers: a left at the start and right at the end
#  Based on left and right calculate middle pointer
#  While middle is not equal to the value and start <= end
#        If the middle is greater than the value, move right pointer down
#        If the middle is less than the value, move left up
#  If value is not found, return -1

def binarySearch(arr, value):
    start = 0
    end = len(arr)
    middle = math.floor((start+end)/2)
    while not (arr[middle] == value):
        if arr[middle] < value:
            start += 1
        elif arr[middle] > value:
            end -= 1
        middle = math.floor((start+end)/2)
    return middle

arr = [1,2,3,4,5,6,7,8,9,166,555,2345]
print(binarySearch(arr, 8))

