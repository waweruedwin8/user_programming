"""
Please write a program which asks the user for a word and then prints out the number of characters,
 if there was more than one typed in.
"""
word = input("Enter any word or sentence and find out the no of characters: ")
if len(word) > 1:
    print(f" There are {len(word)} letters in the word {word}")
print("Thank you!")
