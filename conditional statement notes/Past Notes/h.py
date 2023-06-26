#preventing a short circuit evaluation
#resource: https://www.py4e.com/html3/03-conditional

x = float(input("Enter x: "))
y = float(input("Enter y: "))
if x >= 2 and y != 0 and (x/y) > 2:
    print("True")
else:
    print("False")
