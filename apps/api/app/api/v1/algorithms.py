from fastapi import APIRouter

router = APIRouter(tags=["algorithms"])


@router.get("")
def list_algorithms() -> dict[str, list]:
    return {"items": []}
