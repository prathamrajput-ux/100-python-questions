#Write a program to find the sum of all natural numbers from 1 to n.
n = int (input("Enter your number :  "))

sum = 0

for i in range(1,n):
    sum = sum + i

print(sum , end= " ")