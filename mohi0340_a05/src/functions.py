"""
-------------------------------------------------------
[Assignment 5 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-08"
-------------------------------------------------------
"""
# import
import math

# functions


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """

    product = 1

    for n in range(2, num + 1, 1):

        product *= n

    return product


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Calculates and returns the time of calories burned every five minutes
    Use: calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute- calories burnt every minute
        minutes- max number of minutes 
    Returns:

    ------------------------------------------------------
    """
    print(f"calories_burned({per_minute},{minutes})")

    m = 5
    for i in range(0, minutes, m):
        calories = per_minute * m
        print(f" {m:2d}:  {calories:.1f}")
        m = m + 5

    return


def open_triangle(num_rows):
    """
    -------------------------------------------------------
    Prints a triangle with a pattern of spaces in the middle
    Use: open_traingle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows- the number of rows of the triangle (int)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(0, num_rows, 1):
        print("#", end='')
        for c in range(i):

            print(" ", end='')
        print("#")
    return


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"multiplication_table({start}, {stop}) -->")
    print("       ", end="")
    for i in range(start, stop + 1):
        print(f"{i:5d}", end="")

    print()
    dash = "-----" * (stop - start + 1)
    print(f"       {dash}")

    for z in range(start, stop + 1):

        print(f"{z:5d} |", end="")

        for r in range(start, stop + 1):
            product = z * r

            print(f"{product:5d}", end="")

        print()
    return


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """

    total = 0
    for i in range(start, start + (count * increment), increment):

        total = total + i

    return total
