from fastapi import APIRouter

router = APIRouter(tags=["experiments"])


@router.get("")
def list_experiments() -> dict[str, list]:
    return {"items": []}
