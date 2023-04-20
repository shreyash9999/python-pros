height = int(input("Whats your height in cm? "))
if height < 120:
    print("You can ride.")
    age = int(input("What's your age? "))
    if age <12:
        bill = 10

    elif age <18:
        bill = 15

    elif age >= 45 and age <= 55:
        
        print("Your are free to ride for free!")

    elif age >=18:
        bill = 20
    else:
        print("You have grown too fast.")

    pic = input("Do you want to take photo. Say y or n.")

    if pic == "Y":
        bill += 3
        #Means now wh so ever current bill is will be added to 3 and ans will be given
        print(f"Your total bill is {bill}")
    else:
        print(f"Your bill is {bill}")

