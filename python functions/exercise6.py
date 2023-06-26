#PY4E Exercise 6 - Functions
def computepay(h, r):
    if h > 80:
        print("Overtime accrued.")
        overtime = (r * 0.5 + r) * h
        print("Before taxes, your overtime comes to:", "$", round(overtime, 2))
    else:
        print("No overtime accrued.")
        pay = h * r
        print("Before taxes, you earned:", "$", round(pay, 2))
       
h = float(input("Hours: "))
r = float(input("Rate: "))

computepay(h, r)
 