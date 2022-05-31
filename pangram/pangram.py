def is_pangram(sentence: str):
    """
    returns if the given sentence is pangram
    """
    return len(set([c for c in sentence.lower() if c.isalpha()])) == 26
