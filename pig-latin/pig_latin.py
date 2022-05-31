import re

def translate_inner(text: str) -> str:
    if re.match(r'^(a|e|i|o|u|xr|yt)', text):
        return f'{text}ay'

    if re.match(r'^[^aeiou]?qu', text):
        return re.sub(r'^([^aeiou]?qu)(.*)', r'\2\1ay', text)

    if re.match(r'^\wy$', text):
        return f'y{text[0]}ay'

    if re.match(r'^[^aeiouy]+y', text):
        return re.sub(r'^([^aeiouy]+)(y.*)', r'\2\1ay', text)

    if re.match(r'^[^aeiou]+', text):
        return re.sub(r'^([^aeiou]+)(.*)', r'\2\1ay', text)

    return text 


def translate(text: str):
    return ' '.join([translate_inner(word) for word in text.split()])
