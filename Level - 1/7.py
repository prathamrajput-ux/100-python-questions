#  Write a program to swap two numbers without using a third variable. 
a = int(input("Enter your 1st number : " ))
b = int(input("Enter your 2nd number : " ))

print(f"Before swap value of a is {a}")
print(f"Before swap value of b is {b}")

a , b = b,a 


print(f"After Swap value of a is {a}")
print(f"After Swap value of b is {b}")