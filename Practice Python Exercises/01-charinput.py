"""PracticePython.org - Exercise 01 Character Input

Developer: @daddyjab
This script implements a solution for the Character Input exercise.
Enjoy!
"""

# Imports
import time

# Accept input from the user
_u_name = str(input("Please enter your name: "))
_u_age = int(input("Hi, " + _u_name + ", Please enter your age: "))

# Determine the current year
_c_year = int(time.strftime("%Y"))

# Calculate the year in which the person will turn 100
_u_yearat100 = _c_year + (100 - _u_age)

# Print a helpful message
print("Thanks for your input.\nToday's year is " + str(_c_year) + ", and you will turn 100 in the year " + str(_u_yearat100) )
