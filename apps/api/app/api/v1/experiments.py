from pathlib import Path
import yaml
from fastapi import APIRouter, HTTPException
router = APIRouter(tags=["experiments"])
ROOT = Path(__file__).resolve().parents[5] / "content" / "experiments"
@router.get("")
def list_experiments() -> dict[str, list[dict]]:
    return {"items": [yaml.safe_load(p.read_text()) | {"slug": p.stem} for p in sorted(ROOT.glob("*.yaml"))]}
@router.get("/{slug}")
def get_experiment(slug: str) -> dict:
    p = ROOT / f"{slug}.yaml"
    if not p.exists(): raise HTTPException(status_code=404, detail="Experiment not found")
    return yaml.safe_load(p.read_text()) | {"slug": slug}
