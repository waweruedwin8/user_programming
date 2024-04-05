
user_age = int(input("Please Enter Your Age: "))

if user_age < 5 and user_age >= 0:
    print(" I suspect you cant Write quite yet...")
elif user_age <= 0 or user_age >= 125:
    print("You Entered an Invalid age!! ")
else:
     print(f"Ok you are {user_age} years old ")
"""
user_age = int(input("Please Enter Your Age: "))

if user_age < 5 and user_age >= 0:
    print("I suspect you can't write quite yet...")
elif user_age <= 0 or user_age >= 125:
    print("You entered an invalid age!!")
else:
    print(f"Ok, you are {user_age} years old.")
"""