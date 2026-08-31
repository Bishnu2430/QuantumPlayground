from fastapi import APIRouter
router = APIRouter(tags=["algorithms"])
@router.get("")
def list_algorithms() -> dict[str, list[dict]]:
    return {"items": [{"slug": "bell-state", "title": "Bell State", "qubits": 2}, {"slug": "grover-2-qubits", "title": "Grover Search (2 qubits)", "qubits": 2}, {"slug": "qft-small-register", "title": "Quantum Fourier Transform", "qubits": 3}]}
