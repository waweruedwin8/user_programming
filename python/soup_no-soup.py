"""
Please write a program which asks for the user's name.
 If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost.
 The price of a single portion is 5.90.
"""
user_name = input("Please tell me your name: ")
Cost= 5.90
if user_name.lower() != 'Jerry':
    portion = int(input("How many portions: "))
    print("the total cost is: ",portion * Cost)
    
else:
    print("Next Please!")