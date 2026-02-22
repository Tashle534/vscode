file = open("animalzoo.txt")

import random

animals=[]
counter = 0

for line in file:
    animals.append(line)
    counter += 1

print(random.choice(animals))
print(counter)

file.close()