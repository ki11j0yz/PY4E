#program to convert celsius to fahrenheit

temp = float(input("Celsius: "))
conv = (temp * 1.8) + 32 
print("Fahrenheit = ", round(conv, 3))

temp = float(input("What is the numeric temperature to two decimal points? "))
unit = input("Enter Fahrenheit or Celsius, (F/C): ")
if unit == "C":
    conv = (temp * 1.8) + 32
    print("The temp in Fahrenheit is: ", round(conv, 2))
else: 
    conv = (temp - 32) * 0.5556
    print("The temp in Celsius is: ", round(conv, 2))
    