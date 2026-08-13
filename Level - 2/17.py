# Write a program to read a character and check whether it is an alphabet, digit or special symbol.
char = input("Enter your one charcter : ")
if (len(char)==1) :
    if ((char >= 'a' and char <= 'z')or (char >= 'A' and char <='Z') ):
        print(f"Your character '{char}' is alphabet.")

    elif((char >= '0' and char <= '9')):
        print(f"Your character '{char}' is digit.")

    else :
        print(f"Your character '{char}' is special character.")

else :
    print("Please enter only one character" \
    "Thank You")