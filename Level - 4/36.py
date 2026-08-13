#Write a program to find the product of all digits of a number n    
n = input("enter your no.  : ")
pro = 1
for i in n :
    pro *= int(i)

print(pro)