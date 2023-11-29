"""
-------------------------------------------------------
[Assignment 8, Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-28"
-------------------------------------------------------
"""

# import
from functions import is_word_chain

# input
word_list = input("Enter a list of strings separated by space: ").split(" ")

# function
word_chain = is_word_chain(word_list)

# output
print(word_chain)
