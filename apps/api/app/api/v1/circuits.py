from fastapi import APIRouter

router = APIRouter(tags=["circuits"])


@router.get("")
def list_circuits() -> dict[str, list]:
    return {"items": []}
