year = int(input("Enter A year you want to check for  a leap year: "))

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0  or year % 400 == 0:
        print(f" {year} is a leap year!")

    else:
       print(f" {year} is not a leap year!")
leap_year(year)
