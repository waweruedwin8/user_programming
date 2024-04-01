number = int(input("Please type a number: "))
multiple = 1 * 10
if number != multiple:
    print("This number is smaller than:",multiple)
    print("Thank you!")
    multiple -= multiple// 10
else:
    print("the number is equal to:", multiple)