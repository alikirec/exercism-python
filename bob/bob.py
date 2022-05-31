def response(hey_bob: str) -> str:
    """
    returns Bob's answer to the given string
    """
    trimmed_sentence = hey_bob.strip()

    if trimmed_sentence.isupper():
        if trimmed_sentence.endswith('?'):
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    
    if trimmed_sentence.endswith('?'):
        return 'Sure.'

    if not trimmed_sentence:
        return 'Fine. Be that way!'
    
    return 'Whatever.'
