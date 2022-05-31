from math import ceil


def is_palindrome(number: int) -> bool:
    if number < 10:
        return True

    return str(number) == str(number)[::-1]


def get_factors(n: int, all_numbers: range) -> list[tuple[int, int]]:
    result = [(number, n / number) for number in all_numbers if n % number == 0 and (n / number) in all_numbers]
    return result


def get_possible_products(min_factor: int, max_factor: int) -> list[tuple[int, int, int]]:
    return sorted([
        (first * second, first, second)
        for first in range(min_factor, max_factor + 1)
        for second in range(first, max_factor + 1)
        if is_palindrome(first * second)
    ], key=lambda tup: tup[0])

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    pivot = min(min_factor + ceil((max_factor - min_factor) / 3), min_factor + 10)
    min_palindrome = None
    for i in range(min_factor, max_factor + 1):
        if i > pivot and min_palindrome is not None:
            break
        for j in range(i, max_factor + 1):
            product = i * j
            if not is_palindrome(product):
                continue
            min_palindrome = product if min_palindrome is None else min(min_palindrome, product)
    
    if min_palindrome is None:
        return None, []
    
    return min_palindrome, get_factors(min_palindrome, range(min_factor, max_factor + 1))


def largest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    pivot = max(max_factor - ceil((max_factor - min_factor) / 3), max_factor - 10)
    max_palindrome = None
    for i in range(max_factor, min_factor - 1, -1):
        if i < pivot and max_palindrome is not None:
            break
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if not is_palindrome(product):
                continue
            max_palindrome = product if max_palindrome is None else max(max_palindrome, product)
    
    if max_palindrome is None:
        return None, []
    
    return max_palindrome, get_factors(max_palindrome, range(min_factor, max_factor + 1))
