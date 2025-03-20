# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# user's input
    # first name
first_name = input("First name: ")
    # last name
last_name = input("Last name: ")

# remove unnecessary spaces
remove_space_firstname = first_name.strip()
remove_space_lastname = last_name.strip()

# print the full name with no spaces