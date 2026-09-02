from app.schemas.simulations import SimulationRequest, SimulationResult
from app.services.quantum.simulator import run_simulation


def simulate_tool(request: SimulationRequest) -> SimulationResult:
    return run_simulation(request)
