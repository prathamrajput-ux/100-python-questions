# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).
c = int(input("Enter your number : "))

if (c >= 90) :
    print("Your grade is A")
elif (c >= 75) :
    print("Your grade is B")
elif (c >= 50):
    print("Your grade is C")
elif (c >= 33):
    print("Your grade is D")
else :
    print("You are fail.")