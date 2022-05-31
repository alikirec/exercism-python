import re


def is_opening(c: str) -> bool:
    if len(c) != 1:
        raise ValueError('Should be a character')
    
    return re.match(r'[\[({]', c) != None


def is_paired(input_string):
    stack = []

    opening_pair = {'}': '{', ']': '[', ')': '('}
    
    for c in input_string:
        if re.match(r'[\[\](){}]', c):
            if is_opening(c):
                stack.append(c)
            elif not stack or stack.pop() != opening_pair[c]:
                return False

    return not stack