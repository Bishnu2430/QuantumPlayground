from fastapi import APIRouter

from app.api.v1 import (
    algorithms,
    auth,
    circuits,
    copilot,
    experiments,
    lessons,
    progress,
    simulation,
    users,
    voice,
)

router = APIRouter()

@router.get("/status")
def status() -> dict[str, str]:
    return {"status": "ok", "version": "v1"}

router.include_router(auth.router, prefix="/auth")
router.include_router(users.router, prefix="/users")
router.include_router(lessons.router, prefix="/lessons")
router.include_router(circuits.router, prefix="/circuits")
router.include_router(simulation.router, prefix="/simulation")
router.include_router(algorithms.router, prefix="/algorithms")
router.include_router(experiments.router, prefix="/experiments")
router.include_router(copilot.router, prefix="/copilot")
router.include_router(voice.router, prefix="/voice")
router.include_router(progress.router, prefix="/progress")
