from fastapi import APIRouter

router = APIRouter(tags=["users"])


@router.get("")
def list_users() -> dict[str, list]:
    return {"items": []}
