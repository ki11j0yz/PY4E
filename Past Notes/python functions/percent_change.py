#percent change
def change(initial, final):
    if final.isnumeric() and initial.isnumeric():
        final = float(final)
        initial = float(initial)
        eqn = ((final - initial) / initial) * 100
        print(round(eqn, 2), "% change")
    else:
        print("Invalid input, data not numeric.")
a = input("Enter a number: ")
b = input("Enter another number: ")
change(a, b)
