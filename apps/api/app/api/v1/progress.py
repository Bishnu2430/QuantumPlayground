from fastapi import APIRouter

router = APIRouter(tags=["progress"])


@router.get("")
def list_progress() -> dict[str, list]:
    return {"items": []}
