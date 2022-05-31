def leap_year(year):
    """
    returns True if it's a leap year
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
