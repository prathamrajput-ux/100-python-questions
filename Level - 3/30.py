#Write a program to display all multiples of a number m up to n terms.

m = int(input("Enter your base number : "))
n = int(input("Enter your number upto where you want multiple : "))

for i in range(m,n+1):
    print(f"{m} X {i} = {i*m}")