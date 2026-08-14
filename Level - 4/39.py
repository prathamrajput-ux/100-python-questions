#Write a program to find the smallest digit in a number n.
n = int(input("ENter your number : "))

small = 9

while n > 0 :
    digit = n % 10
    if digit < small : 
        small = digit
    n =n // 10

print("Smallest number is : ",small)