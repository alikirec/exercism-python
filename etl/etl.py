def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """
    transform from {scores: [letters]} to {letter: score}
    """

    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
