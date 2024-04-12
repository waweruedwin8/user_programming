import calendar
from datetime import datetime # Get the current year
current_year = datetime.now().year
name = input("What is your name? ")
year_birth = int(input("Which year were you born? "))
age = current_year - year_birth
print(f"Hi {name} you will be {age} years old at the end of the year")
