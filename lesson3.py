"""# Checking strings:
text="The best things in life are free."
print("free" in text)
print("forest" in text)
if "best" in text:
    print("Yes, it is present.")
# Slicing strings:
x="Hello World!"
print(x)
print(x[6:12])
print(x[:5])
b="Astronaut"
print(b[5:9])
# Practice:
a="extraordinary"
print(a)
print(a[5:13])
b="Pneumonia"
print(b)
print(b[4:9])

# Negative indexing:
c="Goodbye, World!"
print(c[-6:-1])
d="Programming"
print(d)
print(d[-11:-4])
e="Establishment"
print(e)
print(e[-4:-1])
f="Pneumonoultramicroscopicsilicovolcanoconiosis"
print(f)
print(f[-32:-21])
# Modifying strings:
# upper()
a="hello, world"
print(a.upper())
# lower()
b="HELLO, WORLD"
print(b.lower())
# strip() is used to remove whitespaces.
text=" Hard things are hard to get. "
print(text.strip())
# replace() is used to replace characters from a string.
string="milo"
print(string.replace("m", "k"))
# split() is used to split up a single string into two.
x="Python is,a programming language."
y=x.split(",")
print(y)
# format() is used to insert numbers into strings.
age=12
text="I am {} years old."
print(text.format(age))
# Practice of ALL of the methods mentioned above.
pieces=3
price=45.98
text="I bought {} pieces of cake for {} dollars."
print(text.format(pieces, price))
whitespaces=" Whitespaces "
print(whitespaces.strip())
hat="hat"
print(hat.replace("h","c"))
textPiece="Python is better than C++  because it is easier to understand."
print(textPiece.split("  "))
print("")"""
# Capitalize:
text="today is friday."
x=text.capitalize()
print(x)
y="25 is a number."
x=y.capitalize()
print(x)
