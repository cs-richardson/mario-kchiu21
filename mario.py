"""
Kolton Chiu
In this program the user has to input a number between 0-23
and a pyramid with that input as height. If the user inputs a negative number
or a number not between 0-23 then it will re-prompt the user. 
"""
#variable
user_input = 24

#loops prompt until user input a number that meets the requirements
while user_input > 23 or user_input < 0:
    user_input = int(input("Height: "))

#this loop prints the two triangle shapes with the user's input
#the "\" continues the print statement to the next line. 
for i in range(0, user_input):
    print(" " * (user_input - (i + 1)) + "#" * (i + 1) \
    + "  " + "#" * (i + 1) + " " * (user_input - (i + 1)))
