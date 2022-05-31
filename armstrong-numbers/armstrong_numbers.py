from functools import reduce

def is_armstrong_number(number):
    digits = [int(digit_str) for digit_str in str(number)[:]]
    armstrong_sum = reduce(lambda acc, digit: acc + digit ** len(digits), digits, 0)

    return armstrong_sum == number
