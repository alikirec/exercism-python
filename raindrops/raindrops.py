digits_to_notes = (
    (3, 'Pling'),
    (5, 'Plang'),
    (7, 'Plong')
)


def convert(number):
    """
    Gets a number and returns notes if possible
    otherwise, returns given number as string
    """
    notes = "".join([note for digit, note in digits_to_notes if number % digit == 0])

    if len(notes) == 0:
        return str(number)
    
    return notes
