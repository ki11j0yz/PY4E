#return values:

def greet(lang):
    if lang == "es":
        return("Hola")  #-> the return function takes some input, and returns the result. 
    elif lang == "fr":
        return("Bonjour")
    else:
        return("Hello")

print(greet("fr"), "Glenn")
print(greet("en"), "Sally")
print(greet("es"), "Michael")


#multiple parameters & returns

def eqn(a, b):
    add = a + b
    return add

x = eqn(3, 5)
print(x)


#my practice:

def equation(x):
    add = x + 10
    return add

y = equation(10)
print(y)

def volume(a, b, c):
    vol = a * b * c
    return vol

x = volume(5, 5, 5)
print(x)  
