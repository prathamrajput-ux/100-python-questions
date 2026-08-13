# Write a program to read seconds and convert them into hours, minutes and seconds.
sec = int(input("Enter your second : "))
hour = sec//3600
minu = sec//60
print(f"{sec}second into hours : {hour}")
print(f"{sec}second into minutes : {minu}")
print(f"{sec}second into Seconds : {sec}")