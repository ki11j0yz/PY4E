import random

for i in range(10):
    x = random.random()
    print(x)
    
#random.randint()
print(random.randint(1, 10))


#choose element from sequence
t =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(t))

