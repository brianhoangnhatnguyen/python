# Tuples: used to store multiple items in a single variable
# Tuples are ordered but unchangeable
# Tuples use parentheses
# Creating a tuple:
tuple1 = (1, 2, 3j, "hadsfhsadf", 2.23423, False, "efasdfadfsasdfasdfasdf")
print(tuple1)
print(len(tuple1))
print(type(tuple1))
# Tuple constructor:
tuple1 = tuple((1, 123123j, 12.123123123, "asdfasdf", True, True)) # Tuples allow duplicate values
print(tuple1)
# Accessing tuples:
tuple2 = (1123213123j, 1, 12.123123123, "asdfasdf", True, True)
print(tuple2[2])
print(tuple2[1:3])
print(tuple2[-4:-1])
print(tuple2[-4:])
# Checking tuples:
thistuple = ("apple is a fruit")
if "fruit" in thistuple:
    print("YES!!!!!!!!!!!")
thistuple = ("apple is a fruit")
if "eat" not in thistuple:
    print("nah.")
# Practice questions:
tuple1 = ("hi", "yes", "OMG")
print(tuple1)
tuple1 = tuple(("no", "yes", "true", "SURVIVAL THE SPONGEBOB THE KILLER SURVIVAL THE SPONGEBOB THE KILLER SURVIVAL THE SPONGEBOB THE KILLER"))
print(tuple1)
thisisatuple = ("mhm", "delicious", "mute", "remote control")
print(type(thisisatuple))
print(len(thisisatuple))
thisisalsoatuple = ("yo", "yes", "yep", "woohoo")
print(thisisalsoatuple[-3:-1])
if "yo" in thisisalsoatuple:
    print("yo")
if "hi" not in thisisalsoatuple:
    print("yoyo")

# Changing tuples:
tuple1 = ("apple", "kiwi", "pear")
x = list(tuple1)
x[1] = "cherry"
x = tuple(x)
print(x)

# Add items:
x = ("apple", "kiwi", "pear")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

# Remove items:
x = ("apple", "kiwi", "pear")
y = list(x)
y.remove("kiwi")
x = tuple(y)
print(x)

# Practice questions:
x = ("hey", "hi", "goodbye")
y = list(x)
y[2] = "hello"
x = tuple(y)
print(x)
x = ("hey", "hi", "goodbye")
y = list(x)
y.append("byebye")
x = tuple(y)
print(x)
x = ("hey", "hi", "goodbye")
y = list(x)
y.remove("goodbye")
x = tuple(y)
print(x)

# Unpacking a collection:
fruits = ('apple', 'kiwi', 'pear')
(red, green, blue) = fruits
print(red)
print(green)
print(blue)

# Loop tuples:
greetings = ("hi", "hello", "hey")
for x in greetings:
    print(x)
tupe1 = ("This", "is", "a", "tuple.")
for i in range(len(tupe1)):
    print(tupe1[i])
fruits = ("lychee", "lemon", "apple", "watermelon")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# Join tuples:
_tuple = (1, 2, 3, 4, 5)
_tuple2 = ('a', 'b', 'c', 'd')
_tuple3 = _tuple + _tuple2
print(_tuple3)
print(_tuple + _tuple2)

# Multiply tuples:
_tuple = (1, 2, 3, 4, 5)
myTuple = _tuple * 3
print(myTuple)

# Practice questions 2:
myTuple = ('Visual', 'Studio', 'Code', 'is', 'better', 'than', 'Online', 'GDB', 'Compiler.')
(a1, a2, a3, a4, a5, a6, a7, a8, a9) = myTuple
print(a1, a2, a3, a4, a5, a6, a7, a8, a9)
for x in myTuple:
    print(x)
print("")
i = 0
while i < len(myTuple):
    print(myTuple[i])
    i = i + 1