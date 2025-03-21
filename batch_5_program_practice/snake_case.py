# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# user's full name
# convert to snake case
full_name = str(input("Input your full name: ")).lower().replace(" ", "_")

# print output