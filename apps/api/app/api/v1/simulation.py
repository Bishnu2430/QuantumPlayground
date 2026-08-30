from fastapi import APIRouter

from app.core.config import get_settings
from app.core.exceptions import QuantumLabError, bad_request
from app.schemas.circuits import CodeRunRequest
from app.schemas.simulations import SimulationRequest, SimulationResult
from app.services.quantum.code_runner import run_python_code
from app.services.quantum.simulator import run_simulation

router = APIRouter(tags=["simulation"])


@router.post("/run", response_model=SimulationResult)
def simulate(request: SimulationRequest) -> SimulationResult:
    try:
        return run_simulation(request, max_qubits=get_settings().max_sync_qubits)
    except QuantumLabError as exc:
        raise bad_request(exc.code, exc.message, exc.details) from exc


@router.post("/python")
def run_python(request: CodeRunRequest) -> dict[str, str | int]:
    timeout = request.timeoutSeconds or get_settings().code_runner_timeout_seconds
    try:
        return run_python_code(request.code, timeout_seconds=timeout)
    except QuantumLabError as exc:
        raise bad_request(exc.code, exc.message, exc.details) from exc
