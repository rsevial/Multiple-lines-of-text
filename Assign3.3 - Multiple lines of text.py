# Programmed by: Rebekah Joy E. Sevial
# Problem 3 of Assignment 3
# Multiple lines of text

# Opening mylife.txt and assign as the main file
with open("mylife.txt", "w") as main_file:
# While loop asking the user for the lines
    while True:
# Ask the user to input lines
        inputted_lines = input("Enter line:")
# Input the lines in the text file
        main_file.write(inputted_lines)
# Inputted the lines in different line
        main_file.write("\n")
# Asking the user if are there more lines
        ask_user = input("Are there more lines y/n?")
# If the user inputted "y", continue
        if ask_user == "y":
            continue
# Elif the user inputted "n", break
# Else, invalid
# Ask the user again if there are more lines
# Break, if the user inputted "n"
