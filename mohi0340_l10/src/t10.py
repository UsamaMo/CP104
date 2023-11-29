"""
-------------------------------------------------------
[Lab 10, Task 10]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""

# imports
from functions import count_frequency_word

# file location
file_1 = "words.txt"

# file
fh = open(file_1)

print(f"file '{file_1}' open for reading")

# inputs
word = str(input("Word to count: "))

# function
count = count_frequency_word(fh, word)

# output
print(f"'{word}' appears {count} time(s)")
