# Python Syntax:
print("Hello World!")

# Python Indentation:
if 5>3:
    print("Goodbye World!")

# Python Variables
x=7
y=5
print(x)
print(y)

# Python Comments (this is a comment)

"""
This is a multiline comment.
"""

print("aeiou")
name="Brian"
lastname="Nguyen"
print(name, lastname)

# Yesterday came a patient named Burak. 
# His age was 56. 
# He was diagnosed with Covid. 
# He is admitted in room no. 13. 
# He crashed his car in the parking area.
# He works as a  manager in a bank.

patientName="Burak"
patientAge=56
patientVirus="Covid"
patientRoomNumber=13
patientAccident="Car Crash"
patientOccupation="Bank Manager"

print(patientName)
print(patientAge)
print(patientVirus)
print(patientRoomNumber)
print(patientAccident)
print(patientOccupation)

# Type of Variable:
print(type(patientName))
print(type(patientAge))

# Case Sensitive:
a=3
B="Brian"
print(B, a)

#Legal Variables names:
myvar="a"
_my_var="b"
myVar="c"
my_var="d"
MYVAR="e"
myvar2="f"

# Illegal:
""" 2myvar
my-var
my var """

# Camel Case: each word (except the first) starts with a capital letter
firstName="Brian"

# Pascal Case: each word starts with a capital letter
FirstName="Brian"

# Snake Case: each word is separated with an underscore
First_name="Brian"

print(firstName, FirstName, First_name)
print(myvar, _my_var, myVar, my_var, MYVAR, myvar2)