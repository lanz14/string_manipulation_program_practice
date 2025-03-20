# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# ask the user to input a number between 1-1000
number = int(input("Input a number (0-1000): "))

# add zeros to the inputted number
    # if the user entered a single digit it will add five zeros, and print
if 0 <= number <= 9:
    print(f"00000{number}")

    # if the user entered two digits it will add four zeros, and print
elif 10 <= number <= 99:
    print(f"0000{number}")

    # if the user entered three digits it will add three zeros, and print
elif 100 <= number <= 999:
    print(f"000{number}")

    # if the user entered four digits it will add two zeros, and print
elif number == 1000:
    print(f"00{number}")

else:
    print(f"Numbers must be 1-1000 only.")