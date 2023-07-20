# Escape characters:
# Single quote:
text = 'It\'s tuesday today.'
print(text)
# New line:
text = "I am learning Python\nescape characters."
print(text)
# Tab:
text = "Hello\tWorld!"
print(text)
# Backspace:
text = "Hello  \bWorld!"
print(text)
# Python operators:
# Arithmetic: (+ , -, *, /, %, **, //)
x = 7
y = 8
# Addition:
print(x + y)
# Subtraction:
print(x - y)
# Multiplication:
print(x * y)
# Division:
print(x / y)
# Modulus:
print(x % y)
# Exponentiation:
print(x ** y)
# Floor division:
print(x // y)
print("")
# Assignment operators: (=, +=, -=, *=, /=, **=, //=, &=, >=, <=)
x = 7
x += 2
print(x)
x = 7
x -= 2
print(x)
x = 7
x *= 2
print(x)
x = 7
x /= 2
print(x)
x = 7
x **= 2
print(x)
x = 7
x //= 2
print(x)
x = 7
x &= 2
print(x)
x = 7
x >>= 2
print(x)
x = 7
x <<= 2
print(x)
# Comparison operators: (==, >=, <=, !=, >, <)
x = 12
y = 7
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)
print(x<y)
print(x>y)
print("")
# Logical operators: (and, or, not)
a = 12
print(a < 19 and a > 10)
print(a < 8 or a > 7)
print(not(a < 19 and a > 10))
print(a < 20000 and a > -2476)
print(a < -9876345 or a > -23479623478623598567878569234495237864523976825436789)
print(not(a < -9876345 or a > -2347962))
print(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(not(a < -9876345 or a > -2347962)))))))))))))))))))))))))
print("")
# Indentity operators: (is, is not)
x = ["Apple", "Kiwi"]
y = ["Apple", "Kiwi", "Orange"]
z = x
print(x is z)
print(x is y)
print(x is not z)
print(x is not y)
print("")
# Membership operators: (in, not in)
print("Kiwi" in x)
print("Pear" in x)
print("Orange" not in x)

# List: (used to store multiple items in a single variable) 
my_List = ["Monday", "Tuesday", "Wednesday"]
print(my_List)
my_List = ["Monday", "Tuesday", "Wednesday", "Monday"]
print(my_List)
# Length of a list:
my_List = ["Monday", "Tuesday", "Wednesday", "Wednesday"]
print(len(my_List))
# Type:
my_List = ["Monday", "Tuesday", "Wednesday", "Wednesday"]
print(type(my_List))
my_List1 = [12, 12.121212, 12j, "Hello World!", True]
print(my_List1)
print(type(my_List1))
# list() constructor:
my_List2 = list(("Apple", "Kiwi"))
print(my_List2)
# Access items:
my_List3 = ["Apple", "Kiwi", "Orange", "Melon", "Cherry"]
print(my_List3[2:])
my_List3 = ["Apple", "Kiwi", "Orange", "Melon", "Cherry"]
print(my_List3[:5])
my_List3 = ["Apple", "Kiwi", "Orange", "Melon", "Cherry"]
print(my_List3[-2:])
# Practice questions:
print(len(my_List3))
print(type(my_List3))
print(my_List3[1])
print(my_List3[-2])
# Change items:
my_List4 = ["Apple", "Kiwi", "Orange"]
print(my_List4)
my_List4[1] = "Pear"
print(my_List4)
my_List4[1:3] = ["Pineapple", "Watermelon"]
print(my_List4)
# Adding items:
# append():
my_List4 = ["Apple", "Kiwi", "Orange"]
my_List4.append("Pear")
print(my_List4)
# insert():
my_List4 = ["Apple", "Kiwi", "Orange"]
my_List4.insert(1, "Pear")
print(my_List4)
# Practice questions 2:
the_List = list(("One", "Two", "Three", "Four"))
print(the_List)
print(the_List[2])
the_List[0] = 1
print(the_List)
the_List.append("Five")
print(the_List)
the_List.insert(1, 1.5)
print(the_List)