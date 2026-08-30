from fastapi import APIRouter

router = APIRouter(tags=["lessons"])


@router.get("")
def list_lessons() -> dict[str, list]:
    return {"items": []}
