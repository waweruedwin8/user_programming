# A program that takes user input of two numbers and the prefered mathematical operator from the user and gives the result of the math
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
math_symbol = (input("Enter the mathematical sign you wish to use, choose between *,  /,  +,  - or  % "))
result = None
if math_symbol == '*':
    result = number1 * number2
    print("The multiple of",number1,"&",number2," is = ",result)
elif math_symbol == '/':
    result = number1 / number2
    print("The qotient of",number1,"&",number2," is = ",result)
elif math_symbol == '+':
    result = number1 + number2
    print("The sum of",number1,"&",number2," is = ",result)
elif math_symbol == '-':
    result = number1 - number2
    print("The difference of",number1,"&",number2," is = ",result)
elif math_symbol == '%':
    result = number1 % number2
    print("The remainder of",number1,"&",number2," is = ",result)
else:
    print( math_symbol ," is an Invalid mathematical Symbol")