import random
name = input("Give names name :  ")
split_names = name.split(", ")
noof = len(split_names)
random_select = random.randint(0 , noof - 1)
print(split_names[random_select])

#or

import random
name = input("Give names name :  ")
choice = random.choice(name)
print(choice)