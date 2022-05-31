def flatten(iterable):
    result = []
    
    for val in iterable:
        if val is None:
            continue
        if type(val) == list:
            result += flatten(val)
        else:
            result.append(val)

    return result
