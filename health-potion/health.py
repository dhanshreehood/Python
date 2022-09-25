import random

health = 50

difficulty = 3 # setting difficulty value,  1 for easy; 2 for medium; 3 for hard.

# here we will divide through difficulty, difficulty increases potion_health given to player decreases.
potion_health = int(random.randint(25,50) / difficulty) # using casting to get value in int.

health = health + potion_health

print(health)