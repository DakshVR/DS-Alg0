# A dictionary is a collection which is unorderd, changable and indexed.
# Miller: a person who owns or works in a corn mill
# MyDict = {"Miller": "a person who owns or works in a corn mill"}

# Creating a Dictionary in Python
# Time Complexity & Space complexity = O(1)

# myDict = dict()
# print(myDict)
# myDict1 = {}
# print(myDict1)

# eng_sp = dict(one= "uno",two ='dos', three = 'tres')
# eng_sp = {'one': "uno",'two':'dos', 'three' : 'tres'}
# print(eng_sp)

# Tuples: Time & Space complexity = O(n)
# eng_sp_list = [('one', 'uno'),('two', 'dos'),('three', 'tres')]
# eng_sp1 = dict(eng_sp_list)
# print(eng_sp1)

# ???????????????????????????????????????????????????
# How to Update/add element to the dictionary
# ???????????????????????????????????????????????????

# Updating Time & Space complexity is O(1)
# myDict = {'name': 'Daksh', 'age': 25}
# myDict['age'] = 37
# print(myDict)

# # Adding Time & Space Complexity is O(1)
# myDict['city'] = 'Corvallis'
# print(myDict)

# ???????????????????????????????????????????????????
# Traverse through the dictionary
# ???????????????????????????????????????????????????

# Time complexity: O(n)
# Space complexity: O(1)
myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis'}

# def traverse(dict):
#     for key in dict:
#         print(key, dict[key])

# traverse(myDict)

# ???????????????????????????????????????????????????
# Search an element in the dictionary
# ???????????????????????????????????????????????????

# Time complexity: O(n)
# Space complexity: O(1)

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis'}

# def search(dict, value):
#     for key in dict:
#         if dict[key] == value:
#             return key, value
#     return 'Value does not exist'
        
# print(search(myDict, 'Corvallis'))

# ???????????????????????????????????????????????????
# Delete/Remove an element in the dictionary
# ???????????????????????????????????????????????????

# Time complexity: O(1)
# Space complexity: O(1)

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# del myDict['city']
# print(myDict)

# * Pop method

# Time complexity: O(1)
# Space complexity: O(1)

# removed = myDict.pop('city')
# print(removed)
# print(myDict)

# * popitem()
# Time complexity: O(1)
# Space complexity: O(1)

# removed = myDict.popitem()
# print(removed)
# print(myDict)

#  * Clear = clears everything in the list

# Time complexity: O(n) n = number of element
# Space complexity: O(1)

# myDict.clear()
# print(myDict)

# ???????????????????????????????????????????????????
# Dictionary Method
# ???????????????????????????????????????????????????

# ! clear()
# syntax; dictionary.clear()

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# myDict.clear()
# print(myDict)

# ! copy() = returns a shallow copy of the dictionary, doesn't modify the og dictonary.
# syntax; dictionary.copy()

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# newDct = myDict.copy()
# print(newDct)
# print(myDict)

# newDct.pop('city')
# print(newDct)

# ! Fromkeys()
# syntax; dictionary.fromkeys(sequence[], value)

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# newDict = {}.fromkeys([1,2,3], 0)
# newDict = {}.fromkeys([1,2,3])
# print(newDict)

# ! get()
# syntax; dictionary.get(key, value)

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# print(myDict.get('asge','Jhon'))
# print(myDict.get('age','Jhon'))

# ! items()  - returns key value tuple pairs
# syntax: dictionary.items()

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# print(myDict.items())


# # ! keys()  - returns all key from dictionary
# # syntax: dictionary.keys()

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# print(myDict.keys())

# # ! values()  - returns all values from dictionary
# # syntax: dictionary.values()

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# print(myDict.values())

# ! popitem()  - pops last key,value pair from the dictionary
# syntax: dictionary.popitem()

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# print(myDict.popitem())
# print(myDict)

# ! setdefault = if key is present it returns the value, or will create a new key with default value
# syntax: dictionary.setdefault(key, default_value)

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# print(myDict.setdefault('naddme', 'Gu'))
# print(myDict)

#  ! pop()
# syntax: dictionary.pop(key, default_value)
# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# print(myDict.pop('name', 'Gu'))

# ! update() = adds the key and value, if key doesn't exist, or else updates the value for the key
# syntax: dictionary.update(other_dictionary)

# myDict = {'name': 'Daksh', 'age': 25, 'city': 'Corvallis', 'education': 'Masters'}

# newDict = {'name': 'Hello', 'age': 225, 'a': 'b'}

# myDict.update(newDict)
# print(myDict)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Dictionary Operators/ Builtin Functions
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# myDict = {3: 'three', 5: 'five', 9: 'nine', 2: 'two', 1: 'one', 4:'four'}

#  ? In/Not operator = works with keys not values, for values we can use dict.values()

# print( 3 in myDict)
# print( 'four' in myDict.values())

# ? len() function = each pair is one element

# print(len(myDict))

# ? all() function

# print(all(myDict))

# ? any() function - any one true return true, all false = false

# print(any(myDict))

# ? sorted() function = sort out the keys

# print(sorted(myDict))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Dictionary Vs List
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Distionary                                               List
# ordered python 3.7
# unordered                                          Ordered
# Access via key                                     Access via index
# Collection of key value pairs                      Collection of elemen
# Preffered when you have unique key values          when you have ordered data
# No duplicates members                              Allow duplicate members


# Time and Space complexity

#       Operation                   Time Complexity             Space Complexity

# Creating a Dict                   O(len(dict))                    O(n)
# Inserting value                   O(1) / O(n)                     O(1)
# Traversing                            O(n)                        o(1)
# Accessing a given cell                O(1)                        O(1)
# Searching a given value               O(n)                        O(1)
# Deleting a given value                O(1)                        O(1)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ? Dictionary Comprehension

# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key, value) in dict.items()}

# new_dict={new_key: new_value for (key, value) in dict.items() if condition ()}

import random

city_names = ['Madrid', 'London', 'Mumbai', 'Berlin']

city_temps = {city:random.randint(20,30) for city in city_names}
print(city_temps)

above_25 = {city: temp for (city, temp) in city_temps.items() if temp > 25}
print(above_25)
