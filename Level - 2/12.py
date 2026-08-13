#Write a program to read a number and check whether it is positive, negative or zero.
num = int(input("Enter your number : "))
if (num == 0) :
    print("Number is zero.")
elif (num > 0):
    print("Number is positive.")
else :
    print("Number is negative.")