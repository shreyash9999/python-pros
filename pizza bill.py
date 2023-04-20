print("Welcome to FAST PIZZA.")
size = input("What pizza size do you prefer (s,m,l)? ")
add_pepperoin = input("Would you like to add pepperoni (y or n)? ")
extra_cheese = input("Do you want extra cheese(y or n)? ")

bill = 0
if size == "s":
    bill += 20
elif size == "m":
    bill += 25
else:
    bill += 30

if add_pepperoin == "y":
    if size == "s":
      bill += 3
else:
      bill += 5

if extra_cheese == "y":
    bill += 1
    print (f"Youe total bill is {bill}rs.")
else:
    print(f"Your total bill is {bill}rs.")