from collections import defaultdict

_STORE: dict[str, list[dict[str, str]]] = defaultdict(list)


def append_message(conversation_id: str, role: str, content: str) -> None:
    _STORE[conversation_id].append({"role": role, "content": content})


def get_messages(conversation_id: str) -> list[dict[str, str]]:
    return list(_STORE[conversation_id])
