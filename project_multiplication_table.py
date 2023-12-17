# a program that gets an input from user and gives the reverse multiplication table 
number = int(input("Enter a whole number: "))
count = 10
while count >= 1:
    result = number * count
    print(number,"*",count,"=",result)
    count = count -1
