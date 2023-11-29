"""
-------------------------------------------------------
[Lab 4 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-08"
-------------------------------------------------------
"""


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
# calculation
    diam = radius * 2

    return diam


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """

# calculation
    sh = (((base / 2)**2) + height**2)**(1 / 2)
    area = base**2 + (2 * base) * sh
    vol = (base**2 * ((height) / 3))

    return sh, area, vol


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
# constants
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    LOONIE = 1.00
    TOONIE = 2.00

# calculation
    total = ((nickels * NICKEL) + (dimes * DIME) + (quarters *
                                                    QUARTER) + (loonies * LOONIE) + (toonies * TOONIE))

    return total


def slope(x1, y1, x2, y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: slp = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        slp - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """

# calculation
    rise = y2 - y1
    run = x2 - x1

    slope_s = (rise / run)

    return slope_s


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """

# constants
    SEC_DAYS = 86400
    SEC_HOURS = 3600
    SEC_MINUTES = 60

# calculation
    days = seconds // SEC_DAYS
    hours = seconds // SEC_HOURS
    minutes = seconds // SEC_MINUTES

    return days, hours, minutes
