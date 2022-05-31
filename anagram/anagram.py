def is_anagram(word: str, candidate: str) -> bool:
    if len(word) != len(candidate) or word == candidate.lower():
        return False
    return sorted(list(word)) == sorted(list(candidate.lower()))


def find_anagrams(word: str, candidates: list[str]):
    word_lower = word.lower()

    return list(filter(lambda c: is_anagram(word_lower, c), candidates))
