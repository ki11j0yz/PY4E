#'try' and 'except'

temp = input("Input F temp: ")
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 0.5556
    print(round(cel, 2))
except:
    print("Please enter a number...")

