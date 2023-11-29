"""
-------------------------------------------------------
[Lab 2, Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:      212090340
Email:   mohi0340@mylaurier.ca
__updated__ = "2021-09-20"
-------------------------------------------------------
"""
# Constants
COSTFORLARGEDOG = 75
COSTFORSMALLDOG = 50

# Calculates the Number of Dogs Groomed That Day
numlargedogs = int(input("Number of Large Dogs Groomed: "))
numsmalldogs = int(input("Number of Small Dogs Groomed:"))

# calculates the cost of the Large Dogs
totalcostlargedog = COSTFORLARGEDOG * numlargedogs

# calculates the cost of the Small Dogs
totalcostsmalldog = COSTFORSMALLDOG * numsmalldogs


# Calculates the Cost of both the large and small dogs groomed that day
total = totalcostlargedog + totalcostsmalldog
print(
    "Total Earned For The Day:  ($)", total)
