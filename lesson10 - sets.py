# Sets: used to store multiple items in a single variable
# Sets are unordered, unchangeable, and unindexed
# Sets use braces {}
# Create a set:
mySet = {1, 2, 3, 4}
print(mySet)
mySet1 = {'apple', 56,'kiwi', 23, 1j, 'apple'} # Sets don't allow duplicate values
print(mySet1)
mySet2 = {1, True} # True and 1 are considered the same values
print(mySet2)
mySet1 = {'apple', 56,'kiwi', 23, 1j, 'apple'}
print(len(mySet1))
print(type(mySet1))

# Set constructor:
mySet = set((12, "hi", 865.23444, False, 1j))
print(mySet)

# Accessing sets:
set_1 = {'a', 'b', 'c', 'd'}
for x in set_1:
    print(x)
    
# Checking sets:
print("c" in set_1) # Easiset way to check items (works on sets, tuples, and lists). 

# Practice questions:
sset = {'hi', 'hey', 'hello'}
print(sset)
print(len(sset))
print(type(sset))
print('hi' in sset)
for x in sset:
    print(x)
sset2 = ((12, 3j, "HIHIHIHIHIHIHIH", True))
print(sset2)

# Adding set items:
set_2 = {'apple', 'kiwi', 'pear'}
set_2.add("orange")
print(set_2)

# Updating sets:
set_2 = {'apple', 'kiwi', 'pear'}
set_3 = {'red', 'green', 'blue'}
set_2.update(set_3)
print(set_2)

# Add any iterable: (list, sets, tuples, dictionaries)
set_2 = {'apple', 'kiwi', 'pear'}
myList = ['orange', 'cherry', 'watermelon']
set_2.update(myList)
print(set_2)

# Removing set items:
set_2 = {'apple', 'kiwi', 'pear'}
set_2.discard('apple')
print(set_2)

# Clearing and popping sets:
set_2 = {'apple', 'kiwi', 'pear'}
set_2.clear() # This will clear the set but with the name at the start
print(set_2)

set_2 = {'apple', 'kiwi', 'pear'}
x = set_2.pop() # This will pop a random item
print(x)
print(set_2)

# Practice questions 2:
mySet = {'hi', 'hey', 'hello'}
mySet2 = {'goodbye', 'bye', 'byebye'}
mySet.update(mySet2)
print(mySet)
mySet = {'hi', 'hey', 'hello'}
mySet.pop()
print(mySet)
mySet = {'hi', 'hey', 'hello'}
mySet.add("goodybe")
print(mySet)

# Looping sets:
set_2 = {'apple', 'kiwi', 'pear'}
for x in set_2:
    print(x)
    print(set_2)

# Join sets:
# Union method:
set_1 = {1, 2, 3}
set_2 = {'apple', 'kiwi', 'pear'}
set_3 = set_1.union(set_2)
print(set_3)

# Update method (the same as adding):
set_1 = {1, 2, 3}
set_2 = {'apple', 'kiwi', 'pear'}
set_1.update(set_2)
print(set_1)

# Intersection update:
set_1 = {1, 2, 3, "kiwi"}
set_2 = {'apple', 'kiwi', 'pear', 3}
set_1.intersection_update(set_2) # Shows only the values that are present in both sets
print(set_1)

# Symmetric difference update:
set_1 = {1, 2, 3, 'kiwi'}
set_2 = {'apple', 'kiwi', 'pear', 3}
set_1.symmetric_difference_update(set_2) # Shows only the values that are NOT present in both sets
print(set_1)