number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Enter the mathematical function  you wont to use in words or symbols : ")

sum = number1 + number2
multiple = number1 * number2
division = number1 / number2
difference = number1 - number2
average = sum /2


if operator == 'add' or operator == '+':
    print(f"{number1} + {number2} = {sum}")

elif operator == 'multiply'or operator == '*':
    print(f"{number1} * {number2} = {multiple}")

elif operator == 'divide' or  operator == '/' or operator == '//':
    print(f"{number1} / {number2} = {division}")

elif operator == 'minus' or operator == 'subtract' or operator == '-':
    print(f"{number1} - {number2} = {difference}")

elif operator == 'Average' or operator ==  'mean':
    print(f" the mean of {number1} and {number2} = {average}")

else:
    print("You Entered an invalid math function!")

