# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

# user's input
sentence = input("Input a sentence: ")

# count the words inputted
word_count = len(sentence.split())

# print the word count
print(f"{word_count}")