#write a program to rep all zeros in a number n with the digit 5.
n = int(input("enter your number :"))
dgt = 0
p = 1

while n > 0 :
    rem =  n % 10
    if rem == 0:
        rem = 5

    dgt = dgt + (rem * p)
    p = p * 10
    n = n//10

print(dgt)