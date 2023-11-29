"""
-------------------------------------------------------
[Assignment 2, Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-04"
-------------------------------------------------------
"""

# inputs
length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
concrete = int(input("Cost of concrete ($/m^3): "))
brick = int(input("Cost of brick ($/m^2): "))

# formulas
concrete_needed = (length * width * height)
concrete_cost = (concrete_needed * concrete)
bricks_needed = 2 * ((length * wall_height) + (wall_height * width))
brick_cost = (brick * bricks_needed)
total_cost = concrete_cost + brick_cost

# outputs
print(" ")
print(f"Concrete needed for foundation (m^3): {concrete_needed:.2f}")
print(f"Cost of concrete: ${concrete_cost:,.2f}")
print(f"Bricks needed for walls (m^2): {bricks_needed:.2f}")
print(f"Cost of bricks: ${brick_cost:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
