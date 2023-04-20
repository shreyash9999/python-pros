sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=75):
    print("Distinction")
elif(avg>=65&avg<75):
    print("First Class")
elif(avg>=50&avg<65):
    print("Second Class")
elif(avg>=35&avg<49):
    print("pass")
else:
    print("Grade: F")
