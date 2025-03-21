# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# user's full name in incorrect casing
# converting into pascal casing
full_name = str(input("Input your full name: ")).title().replace(" ", "")

# print output
print(full_name)