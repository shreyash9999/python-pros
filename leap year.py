year = int(input("Check weather year is leap or not = "))
if year % 4 == 0:
    if year % 100 == 0:
       if year % 400 == 0:
            print("Its a leap year.")
       else:
            print("Not leap year.")
    else:
        print("Its leap year.")
else:
    print("Not leap year.")