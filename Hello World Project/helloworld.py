# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:29:43 2018

@author: daddyjab
"""

#compExample = [(x**3, y**3) for x in [1, 2, 3] for y in [1, 2, 3] ]
#print(compExample)

# Ask the user's name
try:
    uName=str(input("Hey, what's your name? "))
except:
    print("Sorry, you really do need to enter a name.")
    exit()

# Display a "Hello, World" message
print(f"Hello {uName}, welcome to the World!")

