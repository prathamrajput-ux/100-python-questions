# Write a program to read three numbers and find the smallest among them.
a = int(input("Enter your number : "))
b = int(input("Enter your number : "))
c = int(input("Enter your number : "))

if (a > b) and (a>c) : 
    print(f"{a} is smallest ")
elif (b > a) and (b > c) :
    print(f"{b} is smallest ")
elif (c > a) and (c > b):
    print(f"{c} is smallest ")