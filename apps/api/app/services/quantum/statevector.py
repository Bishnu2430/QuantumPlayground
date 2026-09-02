from qiskit.quantum_info import Statevector

from app.schemas.circuits import QuantumCircuitIR
from app.services.quantum.simulator import build_qiskit_circuit


def compute_statevector(circuit: QuantumCircuitIR) -> Statevector:
    return Statevector.from_instruction(build_qiskit_circuit(circuit).remove_final_measurements(inplace=False))
