from fastapi import APIRouter

router = APIRouter(tags=["auth"])


@router.get("")
def list_auth() -> dict[str, list]:
    return {"items": []}
