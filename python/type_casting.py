"""
Please write a program which asks the user for a floating point number
and then prints out the integer part and the decimal part separately. 
Use the Python int function.
"""
number = float(input("Enter A Float number: "))
print(int(number))
print(float(number) - int(number))