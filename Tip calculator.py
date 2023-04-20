print("Welcome to tip calculator.")
bill = float(input("What is your bill?Rs "))
tip = float(input("How much tip would you like to give? 10%, 12%, 15% ? "))
split = float(input("In no. people would you like to split bill? "))
total_bill_per = bill * (tip/100)
total_bill = (bill + total_bill_per) / split
round_bill = (round(total_bill, 2 ))
print(f"Each one will pay {round_bill}rs. ")

