def steps(number):
    if number < 1:
        raise ValueError('Only positive integers are allowed')

    value = number
    steps = 0

    while value > 1:
        if value % 2 == 0:
            value /= 2
        else:
            value = (value * 3) + 1
        steps += 1

    return steps
