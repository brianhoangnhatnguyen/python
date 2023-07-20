# More lists:
# extend()
fruits = ["apple", "tomato", "blueberry"]
vegetables = ["carrot", "lettuce", "radish"]
fruits.extend(vegetables)
print(fruits)
# Iterable: (tuples, sets, dictionaries)
fruits = ["apple", "tomato", "blueberry"]
vegetables = ("carrot", "lettuce", "radish") # tuple
fruits.extend(vegetables)
print(fruits)
# Practice questions:
car = ["honda", "toyota", "volkswagen"]
food = ["pho", "bun bo", "nem cuong"]
car.extend(food)
print(car)
# Remove items:
# remove()
x = [1, 2, 3, 4, 5, 6]
x.remove(6)
print(x)
y = ["apple", "kiwi", "orange"]
y.remove("kiwi")
print(y)
# pop()
fruits = ["apple", "kiwi", "orange"]
fruits.pop(1)
print(fruits)
fruits = ["apple", "kiwi", "orange"]
fruits.pop()
print(fruits)
# clear()
fruits = ["apple", "kiwi", "orange"]
fruits.clear()
print(fruits)
# Delete:
fruits = ["apple", "kiwi", "orange"]
del fruits
fruits = ["apple", "kiwi", "orange"]
print(fruits)
# Practice questions 2:
name = ["Brian", "Kyler", "Raymond", "AmNa", "Urvashi"]
name.pop(2)
print(name)
name = ["Brian", "Kyler", "Raymond", "AmNa", "Urvashi"]
name.clear()
print(name)
# Loop lists:
a = ["a", "b", "c", "d", "e", "f"]
for x in a:
    print(x)
a = ["a", "b", "c", "d", "e", "f"]
for i in range(len(a)):
    print(a[i])
# While loops:
fruits = ["apple", "kiwi", "orange"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i=i+1
print("")
# Short hand for loop:
fruits = ["apple", "kiwi", "orange"]
[print(x) for x in fruits]
# Practice questions 3:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[print(x) for x in a]
print("")
i = 0
while i < len(a):
    print(a[i])
    i=i+1
print("")
for i in range(len(a)):
    print(a[i])