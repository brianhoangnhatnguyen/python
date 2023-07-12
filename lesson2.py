# Multiple values in multiple variables:
x,y,z="apple","banana","strawberry"
print(x)
print(y)
print(z)
print(x,y,z)
# Assign the same value to multiple variables:
x=y=z=10
print(x,y,z)
# Unpacking a collection
numbers=[10,11,12]
x,y,z=numbers
print(x,y,z)
# Outputting variables:
x="Python is so easy."
print(x)
a="Python"
b="is"
c="so"
d="easy."
print(a,b,c,d)
# Concatenation:
a="Python"
b=" is"
c=" so"
d=" easy."
print(a+b+c+d)
print(" ")
# Python datatypes:
# string - text type
# int, float, complex - numeric type
# list, tuple, range - sequence type
# dictionaries - mapping type
# set - set type
# bool - boolean type

# string:
x="Python"
print(x)
print(type(x))
# int:
x=100
print(x)
print(type(x))
x=-100
print(x)
print(type(x))
# float:
x=100.111
print(x)
print(type(x))
# complex:
x=100j
print(x)
print(type(x))
x=100+100j
print(x)
print(type(x))
print(" ")
# Example questions from teacher:
x,y,z=1123,2123,3123
print(x,y,z)
x=y=z="hello"
print(x,y,z)
a=10
b=10.1
c=10j
d="Hello World!"
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
greeting=["hello","goodbye","good morning","good night"]
a,b,c,d=greeting
print(a,b,c,d)
print("")
x="hello"
y=" bye"
z=" something"
print(x+y+z)
# Python casting:
x=int(10.123)
print(x)
y=float("10.123123")
print(y)
z=str(6.0)
print(z)
# Python strings:
a="Hello"
print(a)
# Strings are arrays:
a="Python Programming"
print(a[8])
print(a[17])
b="Python is a popular programming language created by Guido Van Rossum in 1991."
print("")
print(b[49])
# Length of a string:
s="Lengthy"
print(len(s)) 