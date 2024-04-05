#a program that request user input on random letters and arranges them in the alphabetical order and selects the middle one
letter1 = input("Enter the first letter: ")
letter2 = input("Enter the second letter: ")
letter3 = input("Enter the third letter: ")
list_letters = {letter1, letter2, letter3}
# sorts the list
sorted_list = sorted(list_letters)
# Calculate the index of the middle letter
middle_index = len(sorted_list) // 2
# Extract the middle letter from the sorted list
middle_letter = sorted_list[middle_index]


print(middle_letter)
    