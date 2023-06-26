#simplest form of a conditional statement
x = float(input("Enter a number: "))
if x > 0:
    print("x is positive")
if x < 0: 
    print("x is negative")

#alternative 'if' statement with 'else'
x = float(input("Enter a number: "))
if x % 2 == 0: 
    print("Your number is even.")
else: 
    print("Your number is odd.")

#chained conditional - 'else' can only be last in chain, otherwise it's 'if' and 'elif' - can also end with 'elif'
x = float(input("Enter a number: "))
if x == 99:
    print("Right on the money!")
elif x > 0 and x < 100:
    print("You're close.")
elif x >= 100:
    print("Too high...")
elif x < 0:
    print("Too Low...")
    
#nested conditional
x = float(input("Enter a number for the x axis: "))
y = float(input("Enter a number for the y axis: "))
if x == y:
    print("x and y are equal")
else:
    if x < y:
        print("x is less than y")
    else:
        print("x is greater than y")
        
#simplifying nested conditional statement using logical operator:
x = float(input("Guess a number between 1 and 10: "))
if 0 < x:
    if x == 6:
        print("On the money!")
    elif x < 10:
        print("x is a single digit, positive number")
elif x < 0:
    print("You went negative")

#alternate simplified conditional statement:
x = float(input("Guess a number between 1 and 10: "))
if 0 < x and x < 10:
    if x == 6:
        print("Right on the money!")
    else:
        print("x is a single-digit, positive number")
else:
    print("x is less than 0")
    
