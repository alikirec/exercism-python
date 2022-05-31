import re


def isbn_digit_val(digit: str) -> int:
    if re.match(r'^\d$', digit):
        return int(digit)
    if digit == 'X':
        return 10

    raise ValueError(f'"{digit}" is not a valid ISBN digit')


def is_valid(isbn_with_hyphens: str):
    isbn = isbn_with_hyphens.replace('-', '')

    if not re.match(r'^[\d]{9}[\dX]$', isbn):
        return False

    factor_value_pairs = list(enumerate([isbn_digit_val(digit) for digit in isbn[::-1]], 1))

    isbn_value = sum([factor * value for factor, value in factor_value_pairs])
    return isbn_value % 11 == 0
