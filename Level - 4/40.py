n = int(input("Enter youtr number : "))

even_count = 0
odd_count = 0 

while n > 0 :
    if n % 2 == 0:
        even_count = even_count + 1

    else :
        odd_count = odd_count + 1

    n = n //10

print("Your evben digit in a number is : ", even_count)
print("Your odd count digit in a number is : ", odd_count)
