# Write a program to read a temperature in Celsius and convert it to Fahrenheit. (0°C × 9/5) + 32 = 32°F

t = int(input("Enter your temperature in celsisus : "))
f = (t * 9/5) + 32
print("Your temperature in Fahrenheit is : ",f)