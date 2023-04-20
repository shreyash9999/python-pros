height = float(input("Whats your height? "))
if height <= 120:
    print("Your are allowed to ride!!!")
    age = int(input("Whats your age? "))
    if age < 12:
        print("Please pay 10rs.")
    elif age <=18:
        print("Please pay 15rs")
    elif age <22:
        print("Please pay 20rs.")
    elif age >22:
        print("please pay 30rs.")
    else:
        print("Please pay 20rs.")
else:
    print("You have grown faster! Sorry not allowed")