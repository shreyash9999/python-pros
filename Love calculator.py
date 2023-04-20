name1 = input("Whats your name? \n")
name2 = input("Whats your patner's name? \n")

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

t = lowercase_name1.count("t")
r = lowercase_name1.count("r")
u = lowercase_name1.count("u")
e = lowercase_name1.count("e")
true_total1 = t + r + u + e

l = lowercase_name1.count("l")
o = lowercase_name1.count("o")
v = lowercase_name1.count("v")
e = lowercase_name1.count("e")
love_total1 = l + o + v + e
total1 = int(true_total1) + int(love_total1)


t = lowercase_name2.count("t")
r = lowercase_name2.count("r")
u = lowercase_name2.count("u")
e = lowercase_name2.count("e")
true_total2 = t + r + u + e

l = lowercase_name2.count("l")
o = lowercase_name2.count("o")
v = lowercase_name2.count("v")
e = lowercase_name2.count("e")
love_total2 = l + o + v + e
total2 = int(true_total2) + int(love_total2)

total = str(true_total1) + str(love_total2)
print(total)

if total < str(40):
    print("Your result  =  Better kill each other!")
elif total < str(50):
    print("Your result  =  Have a coka and mint on your face!")
else:
    print(f"Your result  =  Your love score is {total}.")