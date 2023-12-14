# a program that checks if the student has passed the exams based on a set pass mark
score = int(input("Enter your score: "))
if score >= 100 or score < 0:
    print("You enterd an Invalid score")
elif score >= 50:
    print ("your Score is: ",score) 
    print ("you have passed the exams, congulatulations" )
else:
    print ("your Score is: ",score) 
    print ("you have not met the minimum theresh hold in the exams, please make another attempt")
