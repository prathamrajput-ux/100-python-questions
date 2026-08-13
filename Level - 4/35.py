#Write a program to find the sum of all digits of a number n.

n = input("enter here your no. : ")
sum = 0
for i in n:
    sum +=int(i)

print(sum)