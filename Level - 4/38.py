num = int(input("Enter your number : "))
largest = 0 

while num > 0 :
    digit = num%10
    if digit> largest :
        largest = digit
    num = num // 10

print("lARGEST NUMBER IS : ",largest)
