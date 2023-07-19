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