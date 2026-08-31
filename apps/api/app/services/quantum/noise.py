def depolarizing_noise_profile(probability: float) -> dict[str, float | str]:
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must be between 0 and 1")
    return {"type": "depolarizing", "probability": probability}
