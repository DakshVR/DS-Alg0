# Tuples are immutable
# Comparable and hashable

# ???????????????
# Create New Tuple
# ???????????????

# Time Complexity: O(1)
# Space Complexity: O(n)

# newTuple = ('a','b','c', 'd', 'e')
# newTuple2 = ('a',) # Need to include a comma

#  use built in function
# new = tuple('abcde')
# print(new)
# print(newTuple)

# ???????????????
# Tuples in Memory/ Accessing an element in Tuple
# ???????????????

# Time Complexity: O(1)
# Space Complexity: O(n)

# newTuple = ('a','b','c', 'd', 'e')
# print(newTuple[2])
# print(newTuple[-2])

#  Slice operator [:]
#  starts from left : not including the index

# print(newTuple[2:4]) # prints 2nd and 3rd not 4th
# print(newTuple[:4])
# print(newTuple[3:])

# ???????????????
# Traverse through elements in Tuple
# ???????????????

# Time Complexity: O(n)
# Space Complexity: O(1)

# newTuple = ('a','b','c', 'd', 'e')

# for i in newTuple:
#     print(i)

# for i in range(len(newTuple)):
#     print(newTuple[i])

# ???????????????
# Search an element in Tuple
# ???????????????

# Time Complexity: O(n)
# Space Complexity: O(1)

# newTuple = ('a','b','c', 'd', 'e')

# ! in operator = returns boolean value
# Time Complexity: O(n)
# Space Complexity: O(1)

# print('a' in newTuple)

# ! index method
# Time Complexity: O(n)
# Space Complexity: O(1)

# print(newTuple.index('c'))

# ! custom message
# Time Complexity: O(n)
# Space Complexity: O(1)

# def search(p_tuple, element):
#     for i in p_tuple:
#         if i == element:
#             return f"Found the element at indedx {i}"
#     return ' Element not found'

# print(search(newTuple, 'a'))

# ???????????????
# Operations/ Function
# ???????????????

# * "+ Operator"

# newTuple = ('a','b','c', 'd', 'e')
# tuple1 = (1,2,3,4,5,2,3,4,2,2)

# print(newTuple + tuple1)

# * " * operator"

# print(tuple1 * 3)

# print( 4 in tuple1)

# # ! Count method

# print(tuple1.count(2))

# # ! index method, min(), max()

# print(tuple1.index(3))

# # ! tuple method can convert list inot tuple

# print(tuple([1,2,3,4,5]))