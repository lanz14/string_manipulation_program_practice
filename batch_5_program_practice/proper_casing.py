# Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

# user's full name
first_name = input("First name: ")
last_name = input("Last name: ")

# proper casing the inputted full name
# print the proper cased full name
print(f"\n{first_name.title()} {last_name.title()}")