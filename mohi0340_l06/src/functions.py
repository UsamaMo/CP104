"""
-------------------------------------------------------
[Lab 6 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""

# functions


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(0, num + 1, 2):

        total += i

    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(height):
        for r in range(width):
            print(char, end="")

        print()
    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(n, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(
            f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        i = i - 1
    if i == 1:
        print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
        print(f"Take one down, pass it around, no more bottles of beer on the wall!")

    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(start, end + 1, inc):

        total_cal_burned = i * burnt_per_minute
        print(f"Calories burned after {i} minutes: {total_cal_burned}")
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """

    value = float(input("First value: "))

    minimum = value
    maximum = value
    total = value

    for i in range(1, n, 1):
        value = float(input("Next value: "))
        total = total + value

        if value < minimum:
            minimum = value

        elif value > maximum:
            maximum = value
    average = total / n

    return minimum, maximum, total, average
