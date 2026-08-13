#Write a program to find the product of all natural numbers from 1 to n (factorial of n).

n = int(input("Enter yout number : "))

faactorial = 1
for i in range(1,n+1):
    faactorial = faactorial* i

print(faactorial)