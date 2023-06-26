# notes taken June 25th, 2023 @ 19:50 central time

# values and types refer to the value that you can assign to a variable and what type that value is depends on whether it's a string, integer, boolean, list, etc.
# type() method takes a parameter and can identify a variable's type:
w = 34.5
x = "Hello World!"
y = 42
z = True
print(type(w), type(x), type(y), type(z))
print()

# you can type cast - which means you can identify a variable's type by describing what it is like this:
a = int(34)
b = str("Hello World!")
c = bool(True)
d = float(34.5)       # a float is a number, imaginary or real that contains a decimal
print(type(a), type(b), type(c))
print()

# this can be helpful when you want to identify a number as a string like this:
numstr = str(34)
print(type(numstr))

#