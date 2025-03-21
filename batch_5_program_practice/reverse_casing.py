# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# user's input of full name
first_name = input("First name: ")
last_name = input("Last name: ")

# reverse the casing
# print the output
print(f"\n{first_name.swapcase()} {last_name.swapcase()}")