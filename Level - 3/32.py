#Write a program to display all numbers from 1 to n that are divisible by 3 or 5
n = int(input("Enter your number : "))

for i in range(1,n):
    if(i%3== 0 or i%5 == 0):
        print(i, end = " ")