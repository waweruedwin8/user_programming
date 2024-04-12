"""
Please write a program which asks for the user's age. If the age is not plausible, 
that is,it is under 5 or something that can't be an actual human age, 
 the program should print out a comment.
"""
user_age = int(input("Please Enter Your Age: "))

if user_age < 5 and user_age >= 0:
    print(" I suspect you cant Write quite yet...")
elif user_age <= 0 or user_age >= 125:
    print("You Entered an Invalid age!! ")
else:
     print(f"Ok you are {user_age} years old ")
