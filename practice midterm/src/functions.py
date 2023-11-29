"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-30"
-------------------------------------------------------
"""


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
    for i in range(1, num + 1, 2):
        if i % 2 == 0:
            total = total + i
    return total


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """

    total = 0

    for i in range(1, num + 1, 2):
        if i % 2 != 0:
            total = total + i
    return total


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """

    total = 0
    for i in range(start, finish + 1, increment):
        total = total + i
    return total


def sum_partial_harmonic(n):
    """
    -------------------------------------------------------
    Sums and returns the total of a partial harmonic series.
    This series is the sum of all terms 1/i, where i ranges
    from 1 to n (inclusive)
    i.e. 1 + 1/2 + 1/3 + ... + 1/n
    Use: total = sum_partial_harmonic(n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int > 0)
    Returns:
        total - sum of partial harmonic series from 1 to n (int)
    ------------------------------------------------------
    """

    total = 0
    for i in range(1, n + 1, i):

        total = total + i
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
        for j in range(width):
            print(char, end="")
        print()
    return


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(height + 1):
        print(" " * ((height + 1) - i - 1), end="")
        print((i * 2 - 1) * char)
    return


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(1, width, 1):
        print((i * 2) * char)
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
        total = i * burnt_per_minute
        print(f"Calories burned after {1} minutes: {total}")
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
    
    val= float(input("First Value: "))
    
    minimum=val
    maximum=val
    total=val
    
    for i in range(val):
        next_val=float(input("Next Value: "))
        total=total+1
    
    if minimum<val:
        minimum=val
    else maximum>val:
        maximum=val
    
    average=total/n
    
    return minimum, maximum, total,average 
    
        
        
    