# Even more lists:
# List comprehension:
fruits = ["apple", "kiwi", "pear"]
newlist = []
for x in fruits:
    if "i" in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "kiwi", "pear"]
newlist = [x for x in fruits if "e" in x]
print(newlist)

fruits = ["apple", "kiwi", "pear"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x <= 10]
print(newlist)

fruits = ["apple", "kiwi", "pear"]
newlist = [x.upper() for x in fruits]
print(newlist)
# Sorting lists:
# Ascending order:
fruits = ["orange", "apple", "watermelon"]
fruits.sort()
print(fruits)
numbers = [22, 23, 54, 12, 9, 63, 106, 395, 1, -643]
numbers.sort()
print(numbers)

# Descending order:
numbers = [22, 23, 54, 12, 9, 63, 106, 395, 1, -643]
numbers.sort(reverse = True)
print(numbers)
objects = ["umbrella", "shampoo", "pencil"]
objects.reverse()
print(objects)

# Practice questions:
greetings = ["Hi", "Hello", "Hey", "Bye"]
newlist = []
for x in greetings:
    if "e" in x:
        newlist.append(x)
print(newlist)
newlist = [x for x in range(21)]
print(newlist)
string = ["book", "pencil", "bomb", "microphone", "speaker", "glue"]
string.sort()
print(string)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
numbers.sort(reverse = True)
print(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
numbers.reverse()
print(numbers)

# copy() method:
objects = ["umbrella", "shampoo", "pencil"]
objects2 = objects.copy()
print(objects2)
# list() method:
objects = ["umbrella", "shampoo", "pencil"]
newlist = list(objects)
print(newlist)