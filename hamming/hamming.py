def distance(strand_a, strand_b):
    """
    Calculates the Hamming Distance between two DNA strands.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    difference = 0
    for index, letter in enumerate(strand_a):
        if letter != strand_b[index]:
            difference += 1
    
    return difference