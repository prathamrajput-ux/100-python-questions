# Write a program to read the marks of 5 subjects and print the total and average.
a = float(input("Enter the marks of maths : "))
b = float(input("Enter the marks of sci : "))
c = float(input("Enter the marks of sst : "))
d = float(input("Enter the marks of hindi : "))
e = float(input("Enter the marks of eng : "))

total = a + b + c + d + e
avg = total/5
print("Total marks is : ",total)
print("Average is : ",avg)