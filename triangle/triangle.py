def is_valid_sides(sides):
    """
    checks if given sides can form a valid triangle
    """
    a, b, c = sides
    return (
        all([side > 0 for side in sides]) and
        (a + b >= c) and (a + c >= b) and (b + c >= a)
    )


def equilateral(sides):
    """
    returns if sides can form an equilateral triangle
    """
    a, b, c = sides
    return is_valid_sides(sides) and a == b and a == c


def isosceles(sides):
    """
    returns if sides can form an isosceles triangle
    """
    a, b, c = sides
    return (
        is_valid_sides(sides) and
        (a == b or a == c or b == c)
    )


def scalene(sides):
    """
    returns if sides can form a scalene triangle
    """
    a, b, c = sides
    return is_valid_sides(sides) and a != b and b != c
