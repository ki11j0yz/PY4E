#logical operators

#programs for logical operators

x = float(input("Enter a number: "))
if x >= 0:
    if x == 100 or x == 0:
        print("Right on the money my dude!")
    if x <= 100:
        print("Your number is for sure less than 100, but greater than 0, my dude.")
elif x <= 0:
    print("Your number is for sure less than 0, my dude.")

#Original, alternate way
#elif x > 0 and x < 100:
#    print("Your number is in between 0 and 100. ")
#elif x >= 100:
#    print("Your number is 100, or greater than 100, my dude.")
#elif x <= 0:
#    print("Your number is for sure 0, or less than 0, my dude.")
