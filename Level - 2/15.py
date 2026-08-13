# Write a program to read a year and check whether it is a leap year or not.
year = int(input("Enter Your Year : "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 ==0) :
    print("Your year is leap year")
else :
    print("Your year is not leap year")