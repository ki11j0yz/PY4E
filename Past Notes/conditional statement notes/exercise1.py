#Rewrite your pay program using 'try' and 'except' so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours = input("Input hours: ")
rate = input("Input rate: ")
try: 
    grosspay = hours * rate
    print("Your gross-pay is: ", grosspay)
except: 
    print("Please provide all numeric input...")