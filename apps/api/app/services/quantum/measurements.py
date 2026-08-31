def counts_to_probabilities(counts: dict[str, int], shots: int) -> dict[str, float]:
    if shots <= 0:
        raise ValueError("shots must be positive")
    return {key: value / shots for key, value in counts.items()}
