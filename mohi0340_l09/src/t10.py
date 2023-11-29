"""
-------------------------------------------------------
[Lab 9, Task 10]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-19"
-------------------------------------------------------
"""

# import
from functions import text_analyze

# input
txt = input("Enter a string: ")

# function
uppr, lowr, dgts, whtspc = text_analyze(txt)


# output
print(f"""
upper case letters: {uppr:d}
lower case letters: {lowr:d}
digits: {dgts:d}
whitespace characters: {whtspc:d}""")
