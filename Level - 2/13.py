# Write a program to read three numbers and find the largest among them.
a = int(input("Enter your number : "))
b = int(input("Enter your number : "))
c = int(input("Enter your number : "))

if (a > b) and (a>c) : 
    print(f"{a} is largest than {b} and {c}")
elif (b > a) and (b > c) :
    print(f"{b} is largest than {a} and {c}")
elif (c > a) and (c > b):
    print(f"{c} is largest than {a} and {b}")