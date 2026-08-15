#Write a program to check whether a number n is a palindrome (reads the same reversed).

n = int(input("Enter yout number : "))

reverse = 0

while n > 0:
    reverse = reverse * 10 + (n %10 )

    n = n // 10

print("Reverse number is :", reverse)