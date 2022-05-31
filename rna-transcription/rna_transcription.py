RNA_COMPLEMENTS = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand: str):
    """
    Given a DNA strand, return its RNA complement (per RNA transcription).
    """
    return "".join(
        [RNA_COMPLEMENTS[nucleobase] for nucleobase in dna_strand]
    )
