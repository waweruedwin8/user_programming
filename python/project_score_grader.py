marks = [55,64,75,80,65]
mark_sum = sum(marks)
print("Your Total marks is",mark_sum)
def average_grade():
    length = len(marks)
    average = marks/length
    print("Your average score is:", average)
average_grade
def grade():
    if average >= 80:
        print("Your Grade is A")
    elif average>= 60 < 80:
        print("Your Grade is B")   
grade()

