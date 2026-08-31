BLOCKED_TERMS = {"give me the answer key", "bypass", "cheat on exam"}


def is_allowed_prompt(message: str) -> bool:
    lowered = message.lower()
    return not any(term in lowered for term in BLOCKED_TERMS)
