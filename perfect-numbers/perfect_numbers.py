PERFECT='perfect'
ABUNDANT='abundant'
DEFICIENT='deficient'


def get_aliquot_sum(number: int) -> int:
    """
    returns aliquot sum of the given number
    """
    return sum([
        n for n in range(1, (number // 2) + 1) if number % n == 0
    ])


def classify(number: int):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')

    aliquot_sum = get_aliquot_sum(number)

    if aliquot_sum == number:
        return PERFECT
    if aliquot_sum > number:
        return ABUNDANT

    return DEFICIENT
