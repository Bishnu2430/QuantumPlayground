from time import perf_counter

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

from app.schemas.circuits import QuantumCircuitIR
from app.schemas.simulations import SimulationRequest, SimulationResult
from app.services.quantum.circuit_validator import validate_circuit


def build_qiskit_circuit(circuit: QuantumCircuitIR) -> QuantumCircuit:
    qc = QuantumCircuit(circuit.numQubits, max(circuit.numClbits, circuit.numQubits))
    for op in sorted(circuit.operations, key=lambda item: item.moment):
        gate = op.gate
        if gate in {"id", "x", "y", "z", "h", "s", "sdg", "t", "tdg"}:
            getattr(qc, gate)(op.targets[0])
        elif gate in {"rx", "ry", "rz"}:
            getattr(qc, gate)(op.params[0], op.targets[0])
        elif gate in {"cx", "cz"}:
            getattr(qc, gate)(op.controls[0], op.targets[0])
        elif gate == "swap":
            qc.swap(op.targets[0], op.targets[1])
        elif gate == "measure":
            qc.measure(op.targets, op.clbits)
    return qc


def run_simulation(request: SimulationRequest, max_qubits: int = 12) -> SimulationResult:
    validate_circuit(request.circuit, max_qubits=max_qubits)
    started = perf_counter()
    qc = build_qiskit_circuit(request.circuit)
    if request.mode == "statevector":
        state = Statevector.from_instruction(qc.remove_final_measurements(inplace=False))
        vector = [
            {"basis": format(index, f"0{request.circuit.numQubits}b"), "real": float(value.real), "imag": float(value.imag)}
            for index, value in enumerate(state.data)
        ]
        probabilities = {basis: float(abs(complex(item["real"], item["imag"])) ** 2) for basis, item in ((v["basis"], v) for v in vector)}
        return SimulationResult(
            backend="qiskit-statevector",
            numQubits=request.circuit.numQubits,
            statevector=vector,
            probabilities=probabilities,
            durationMs=int((perf_counter() - started) * 1000),
        )
    simulator = AerSimulator(seed_simulator=request.seed)
    if not any(operation.gate == "measure" for operation in request.circuit.operations):
        qc.measure(range(request.circuit.numQubits), range(request.circuit.numQubits))
    result = simulator.run(qc, shots=request.shots).result()
    counts = {str(key): int(value) for key, value in result.get_counts().items()}
    probabilities = {key: value / request.shots for key, value in counts.items()}
    return SimulationResult(
        backend="qiskit-aer",
        numQubits=request.circuit.numQubits,
        shots=request.shots,
        counts=counts,
        probabilities=probabilities,
        durationMs=int((perf_counter() - started) * 1000),
        metadata={"seed": request.seed},
    )
