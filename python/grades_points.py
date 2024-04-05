points = int(input("How many points did you get out of 100: "))

if points < 0 or points  > 100 :
    print(" Thats Impossible!")
elif points >= 0 and points < 49:
    print("Thats a fail please make another attempt")
elif points >= 50 and points < 70:
    print("Thats a pass keep up the spirit!")
elif points >= 70 and points < 90:
    print("Thats a credit well done!")
elif points >= 90 and points <= 100:
    print("Thats a distiction Congrats!")