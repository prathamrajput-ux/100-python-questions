# Write a program to read a character and check whether it is a vowel or a consonant.
char = input("Enter one character to check its vowel or a consonant : ")
if len(char)==1:
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        print(f"Your character {char} is vowel")


    elif(char >= 'A' and char <='Z') or (char >= 'a' and char <='z'):
        print(f"Your character {char} is consonant ")


    else : 
        print("Invalid character")

else :
    print("Invalid input")
