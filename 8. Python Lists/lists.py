# List can be of multiple data types, unlike array.

# ####################################################################
# Accessing/Traversing the List
# ####################################################################

# shoopping = ['Milk', 'Cheese', 'Butter']
# print(shoopping[1])
# print(shoopping[-1])

# In Operator
# print('Milk' in shoopping)


# for i in range(len(shoopping)):
#     shoopping[i] = shoopping[i]+"+"
#     print(shoopping[i])


# ####################################################################
# Update/Insert the List
# ####################################################################

# Time Complexity: O(1)
# Space Complexity: O(1)

# UPDATE
# myList = [1,2,3,4,5,6,7,8,9]
# myList[5] = 100
# print(myList)

# INSERT

# list methods: 
# ---- insert(), --------------- O(n)
# ---- append(), --------------- O(1)
# ---- extend(), --------------- O(n)

# myList = [1,2,3,4,5,6,7,8,9]
# mylist2 = [11,22,33,44,55,66]
# myList.insert(4,11)
# print(myList)

# myList.append(33)
# print(myList)

# myList.extend(mylist2)
# print(myList)

# ####################################################################
# Slice/Delete the List
# ####################################################################

# list = ['a', 'b', 'c', 'd', 'e', 'f']
# print(list[0:2])
# print(list[:2])
# print(list[1:2])
# print(list[1:])

# DELETE

# ----- pop()    --------------- O(1), O(n)
# ----- delete() --------------- O(n)
# ----- remove() --------------- O(n)

# list.pop(1)
# print(list)

# del list[1]
# print(list)

# list.remove('f')
# print(list)

# ####################################################################
# Searching For an element from the List
# ####################################################################

# list = [10,20,30,40,50,60,70]

# in operator ------------------- O(n)
# target = 50 
# if target in list:
#     print("Found")

#  ! ************************** Linear Search ************************
#  ? Time Complexity: O(n)

# def linear(p_list, p_target):
#     for i, value in enumerate(p_list):
#         if value == p_target:
#             return i
#     return -1

# print(linear(list, 40))

# ####################################################################
# List Operations and functions
# ####################################################################

# ? + Operator = Concatinates two Lists

# a = [1,2,3]
# b = [3,4,5]
# c = a+b
# print(c)

# ? * Operator = multiplies elements

# a=[3,4]
# a = a*4
# print(a)

# ? Len() = gives the length of the list
# ? max(), min(), sum()

# a = [0,1,2,3,4,5,6,7,8,9]
# print("The length is: " ,len(a))
# print("The max num is: " , max(a))
# print("The min num is: " ,min(a))
# print("The sum of the list is: " ,sum(a))
# print("The Avg is: " ,sum(a)/len(a))

# list = []
# while(True):
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     Value = float(inp)
    
#     list.append(Value)
# res = sum(list)/len(list)

# print('Average: ', res)

# ####################################################################
# Strings & Lists
# ####################################################################

# ! list(), split()
# a = 'spam hello what?'
# b = list(a)
# print(b)
# c=a.split()
# print(c)

#  ! delimeter()
# a = 'spam-hello-what?'
# delimeter ='-'
# c = a.split()
# print(c)
# b = a.split(delimeter)
# print(b)

# ! joint() = revert back to string
# a = 'spam-hello-what?'
# delimeter ='a'
# b = a.split(delimeter)
# print(b)
# print(delimeter.join(b))

# PitFalls and ways to avoid them

# list can't use sort()

# !               ARRAYS      VS      LIST
#  Both data structures are Mutable
#  Both can be indexed and itterated thorugh.
#  They both can be sliced.

# import numpy as np

# myArr = np.array( [1,2,3,4,5,6, 'a'])
# mylist = [1,2,3,4,5, 'a']

# print(myArr/2)
# print(mylist/2) ------- Arthmetic operations are supported on List.

# print(myArr) # difference is Data types everything gets converted into string.
# print(mylist) 

# ? ************** List Comprehension
# ? *********************************

# newlist = [new_item for item in list]
# prev_list = [1,2,3]

# new_list = []
# for i in prev_list:
#     val = i*2
#     new_list.append(val)
# new_list = [i*2 for i in prev_list]

# lang = 'Python'
# new_list = [letter for letter in lang]

# print(new_list)

# ? ************** Conditional List Comprehension
# ? *********************************

# newlist = [new_item for item in list if condition]

# prev_lis=[10,-10,-2,3,5,-6,78,-8]
# newlist = [item for item in prev_lis if item>0]
# newlist1 = [item*item for item in prev_lis if item<0]
# print(newlist)
# print(newlist1)

# sentence = "My name is Daksh"
# def isConsonant(letter):
#     vowels = 'aeiou'
#     return letter.isalpha() and letter.lower() not in vowels

# consonants = [i for i in sentence if isConsonant(i)]
# print(consonants)


# newlist = [new_item if condition for item in list]
# prev_lis=[10,-10,-2,3,5,-6,78,-8]
# new_list = [number if number>0 else 0 for number in prev_lis]
# print(new_list)


def pair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i,j)


my_list = [1,2,3,4,5,6,7]

pair(my_list, 6)