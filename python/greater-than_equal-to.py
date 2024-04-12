"""
Please write a program which asks for two integer numbers. 
The program should then print out whichever is greater. 
If the numbers are equal, the program should print a different message.
"""
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2 :
    print("The greatest number is:",number1)
elif number1 == number2:
    print("both numbers are equal!")
else:
    print("The greatest number is:",number2)
