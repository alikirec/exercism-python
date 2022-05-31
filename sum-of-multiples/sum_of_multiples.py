def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    non_zero_multiples = list(filter(lambda m: m > 0, multiples))

    return sum([
        num for num in range(1, limit) if any(
            [num % multiple == 0 for multiple in non_zero_multiples
        ])
    ])
