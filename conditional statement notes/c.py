#conditional notes

#program to decide if x is bigger or smaller than the input

constant = float(input("Enter a constant: "))
delta = float(input("Enter the delta variable: "))
if delta == constant: 
    print("On the money!")
elif delta < constant:
    print("Smaller")
elif delta > constant: 
    print("Bigger")
print("\n")
