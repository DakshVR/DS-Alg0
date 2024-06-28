# Hash function is a function that can be used to map data of arbitrary size to data of fixed size.

# Key : input data givin by the user.
# Hash value: value returned by the Hash Function

# Key  ---> Hash Function  --> Hash Value

# Collison : A collison occurs when two different keys to a hash function produce the same output.

# Properties of good hash fumction
""" 
1 - It distributes hash values uniformly across hash tables.
2 - It has to use all the input data provided by the user
"""

"""
Collison Resolution Technique

1st - Direct Chaining
Implements the buckets as Linked List. Colliding elements are stored in this lists.

2nd - Open Addrrssing
Colliding elements are stoed in other vacant buckets. During storage amd lookup these are found through so called probing

i - Linear Probing
It places new key into closest following emoty cell

ii - Quadratic Ptobing: Adding arbitrary polynomial to the index until an empty cell is found.

iii - Double Hashing
Interval between probes is computed by another hash function

"""


# Hash Table is Full
"""
Direct Chaining: Will never arise.
"""