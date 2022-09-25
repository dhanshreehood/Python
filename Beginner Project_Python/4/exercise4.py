import random 
import my_module

#for integers
random_integer = random.randint(1,20)
print(random_integer)

#how module works?
print(my_module.pi) #my_module is a different file which includes all the logic behind using pi.

#float
random_float = random.random() * 7 # to get decimal value between 0 and 7.
print(random_float)

#let's find random love score of previous example:
love_score = random.randint(0, 100)
print(f"you're love score : {love_score}.")