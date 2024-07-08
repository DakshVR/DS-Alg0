
#? What is Hashing
# Hashing is a method of soting and indexing data. The idea behind hashing is to allow large amounts of data to be indexed using keys commonly created by formulas.

#? Why we need Hashing?
# It is time efficient in case of SEARCH Operations.

# ! Time Complexity for Search Operations in Ideal scenario

# # # # # # # # # # # # # # # # # # # # # # # # # #
# *   DATA Structures       #       Time          #
# # # # # # # # # # # # # # # # # # # # # # # # # #
# Array / Python Lists      #       O(logN)       #
# Linked List               #        O(N)         #
# Tree                      #       O(logN)       #
# Hashing                   #      O(1)/O(N       #
# # # # # # # # # # # # # # # # # # # # # # # # # #  

#? Hash function is a function that can be used to map data of arbitrary size to data of fixed size.
#? Key : input data givin by the user.
#? Hash value: value returned by the Hash Function
#* Hash Table: It is a data structure which implements an associative array abstract data type, a structure that can map keys to values

#! Key  ---> Hash Function  --> Hash Value

#! Collison : A collison occurs when two different keys to a hash function produce the same output.

#! Hash Function Examples

# Mod Function
# def mod(number, cellNumber):
#       return number % cellNumber
# 
#  mod(400, 24)  -----> 16
#  mod(700, 24)  -----> 4

# def modASCII(string, cellNumber):
#       total = 0
#       for i in string:
#           total += ord(i)
#       return total % cellNumber

# modASCII("ABC", 24)   -----> 6


# Properties of good hash fuction
""" 
1 - It distributes hash values uniformly across hash tables.
2 - It has to use all the input data provided by the user
"""

"""
Collison Resolution Technique

1st - Direct Chaining
Implements the buckets as Linked List. Colliding elements are stored in this lists.

2nd - Open Addressing
Colliding elements are stoed in other vacant buckets. During storage amd lookup these are found through so called probing

i - Linear Probing
It places new key into closest following emoty cell

ii - Quadratic Ptobing: Adding arbitrary polynomial to the index until an empty cell is found.

iii - Double Hashing
Interval between probes is computed by another hash function

"""


# Hash Table is Full
"""
Direct Chaining: Will never arise, once the table full, the new items are linked to previous.
"""

"""
OPEN Addressing
create 2X size of current Hash Table and recall hashing for current keys.
"""


