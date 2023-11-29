"""
-------------------------------------------------------
[Assignment 5 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-15"
-------------------------------------------------------
"""

# functions

# Task 1


def winner():
    """
    -------------------------------------------------------
    Determines the number of wins in each color
    Use: blue_count, grey_count = winner()
    -------------------------------------------------------
    Parameters:
       winner = Asks for the input of the winning team

    Returns:
        blue_count - a positive integer (str)
        grey_count - a positive integer (str)
    ------------------------------------------------------
    """
    winner = str(input("Enter the winning team: "))
    blue_count = 0
    grey_count = 0

    while winner != "":
        if winner == "blue":
            blue_count = blue_count + 1
            winner = str(input("Enter the winning team: "))
        if winner == "grey":
            grey_count = grey_count + 1
            winner = str(input("Enter the winning team: "))

    return blue_count, grey_count

# Task 2


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True

    if num == 2 or num == 3:
        prime = True
    if num % 2 == 0 or num < 2:
        prime = False

    i = 3
    while i < int(num**(1 / 2) + 1):
        if num % i == 0:
            prime = False
        i += 1

    return prime

# Task 3


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly_payment interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly_payment payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    monthly_payment = 1

    newly_rate = (rate / 100) / 12

    print(f"Principal:   ${principal:.2f}")
    print(f"Interest Rate : {rate:.2f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print(f"Month Interest   Payment   Balance")
    print("----------------------------------")

    while principal != 0:
        monthly_interest = (newly_rate * principal)

        if principal < payment:
            payment = principal + monthly_interest
            principal = 0
        else:
            principal = principal - payment + monthly_interest
        print(
            f"{monthly_payment:5d}{monthly_interest:9.2f}{payment:10.2f}{principal:10.2f}")
        monthly_payment += 1

    return

# Task 4


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    DIGIT = 10
    count = 0
    num = abs(num)

    if num == 0:
        count = 1

    while (num):
        count = count + 1
        num = int(num / DIGIT)

    return count

# Task 5


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    i = 1
    total = 0

    while i < num:
        if num % i == 0:
            total = total + i
        i += 1

    return total
