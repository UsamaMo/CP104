"""
-------------------------------------------------------
[Assignment 2, Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-04"
-------------------------------------------------------
"""
# constants
TAX = 0.225
ptax = TAX * 100

# input
total_sale = float(input("Enter the total sale: $"))

# output
print(f"""
Projected Tax Report""")

print(f"------------------------")
print(f"Total Sale:    ${total_sale: >7.2f}")
print(f"Annual Tax:    %{ptax: >7.2f}")
print(f"------------------------")

# formula for final tax
total = total_sale * TAX

# output
print(f"Tax:           ${total: >7,.2f}")
