lunch = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))
weekly_expenditure = lunch * price + groceries
daily_expenditure = weekly_expenditure / 7

print("your daily  food expenditure is $:",daily_expenditure)
print("your weekly food  expenditure is $:",weekly_expenditure)