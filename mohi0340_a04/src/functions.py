"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""

# functions


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Takes a number and converts it to the day of the week
    Use: number = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - number representing the day of the week(int)
    Returns:
         number - day of the week (str)
    ------------------------------------------------------
    """
    if (day_number == 1):
        number = "Monday"
    elif (day_number == 2):
        number = "Tuesday"
    elif (day_number == 3):
        number = "Wednesday"
    elif (day_number == 4):
        number = "Thursday"
    elif (day_number == 5):
        number = "Friday"
    elif (day_number == 6):
        number = "Saturday"
    elif (day_number == 7):
        number = "Sunday"
    else:
        number = "Error"
    return(number)


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if (0 <= aqi <= 50):
        level = "Good"
    elif (51 <= aqi <= 100):
        level = "Moderate"
    elif (101 <= aqi <= 150):
        level = "Unhealthy for Sensitive Groups"
    elif (151 <= aqi <= 200):
        level = "Unhealthy"
    elif (201 <= aqi <= 300):
        level = "Very Unhealthy"
    elif(aqi > 300):
        level = "Hazardous"
    else:
        level = "Error"
    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1 >= v3 and v2 >= v3:
        product = v1 * v2
    elif v1 > v2:
        product = v1 * v3
    else:
        product = v2 * v3
    return (product)


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if(rgb1 == "red" and rgb2 == "blue"):
        colour = "fuchsia"
    elif(rgb1 == "blue" and rgb2 == "red"):
        colour = "fuchsia"
    elif(rgb1 == "red" and rgb2 == "green"):
        colour = "yellow"
    elif(rgb1 == "green" and rgb2 == "red"):
        colour = "yellow"
    elif(rgb1 == "green" and rgb2 == "blue"):
        colour = "aqua"
    elif(rgb1 == "blue" and rgb2 == "green"):
        colour = "aqua"
    elif(rgb1 == "red" and rgb2 == "red"):
        colour = "red"
    elif(rgb1 == "blue" and rgb2 == "blue"):
        colour = "blue"
    elif(rgb1 == "green" and rgb2 == "green"):
        colour = "green"
    else:
        colour = "Error"
    return(colour)


def yee_ha(number):
    """
    -------------------------------------------------------
    yee_ha takes an integer parameter and returns one of the following strings:
    "Yee" number is evenly divisible by 3
    "Ha"  number is evenly divisible by 7
    "Yee Ha" number is evenly divisible by both 3 and 7
    "Nada"  number is none of the above
    Use: output = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number- input of the number (int)
    Returns:
        output- output of inputs returning the strings mentioned (int)
    ------------------------------------------------------
    """
    if(number % 3 == 0 and number % 7 == 0):
        output = "Yee Ha"
    elif(number % 3 == 0):
        output = "Yee"
    elif(number % 7 == 0):
        output = "Ha"
    else:
        output = "Nada"
    return(output)
