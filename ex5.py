my_name = 'Shreyash . S . D.'
my_age = 18
my_height = 80 #inches
my_weight = 53 #kg
my_eyes = 'brownish-black'
my_teeth = 'white'
my_hair = 'black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} kg heavy.")
print(f"Actually that's not to heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"his teeth are usually {my_teeth} depending on coffee.")
#I am using addition of strings
total = my_age + my_height + my_weight
print(f"If I add {my_age} , {my_height} and {my_weight} I get {total}.")


# converting inches to centimeters and kilograms to pounds.
# dont do this [inches = 80 , cm = inches * 2.54] you won't get output.
inches = 80
cm = inches * 2.54
weight = 53
pd = weight * 0.45
print(f"{inches} inches in centimeters is {cm}cm")
print(f"{weight} kilograms in pounds is {pd}pounds")

# using round() function
ro = round(2.6)
print(ro)
