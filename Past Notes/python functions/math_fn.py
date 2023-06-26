#import math function: 

import math
print(math)

#import math and dot notation: 
signal_power = input("Enter the signal power: ")
noise_power = input("Enter the noise power: ")
ratio = float(signal_power) / float(noise_power)
decibels = 10 * math.log10(ratio) #-> notice the dot notation from the imported module
print(round(decibels, 2))

radians = 0.7
height = math.sin(radians)
print(height)
