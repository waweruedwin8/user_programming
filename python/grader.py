# Function to input marks from the user
def input_marks():
    marks = []
    while True:
        mark = input("Enter a mark (or 'done' to finish): ")
        if mark.lower() == 'done':
            break
        try:
            marks.append(int(mark))
        except ValueError:
            print("Please enter a valid integer.")
    return marks

# Get marks from the user
marks = input_marks()

# Calculate mean
marks_sum = sum(marks)
length = len(marks)
mean = marks_sum / length

# Function to calculate and print average
def average():
    print("The Average marks is:", mean)

average()

# Function to grade the average
def grader():
    if mean >= 80:
        print("You got an A congrats!")
    elif 60 <= mean <= 79:
        print("You got a B well done!")
    elif 50 <= mean <= 59:
        print("You got a C keep it up!")
    elif mean < 50:
        print("You got an F. Make another attempt!")
    else:
        print("The marks you input are invalid")

grader()
