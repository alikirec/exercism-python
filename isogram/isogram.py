import re


def is_isogram(text: str):
    """
    returns True if the given text is isogram
    """
    no_space_and_hyphen_text = re.sub(r'[-\s]', '', text.lower())
    return len(set(no_space_and_hyphen_text)) == len(no_space_and_hyphen_text)
