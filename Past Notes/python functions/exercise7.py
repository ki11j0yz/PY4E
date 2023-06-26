#PY4E - exercise 7 - computegrade function: 
def computegrade(g):
    if g >= 0.9: 
        print("A")
    elif g < 0.9 and g >= 0.8: 
        print("B")
    elif g < 0.8 and g >= 0.7: 
        print("C")
    elif g < 0.7 and g >= 0.6: 
        print("D")
    elif g < 0.6: 
        print("F")

a = 100
b = float(input("Enter # correct: "))
x = b/a
computegrade(x)
 