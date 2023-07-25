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