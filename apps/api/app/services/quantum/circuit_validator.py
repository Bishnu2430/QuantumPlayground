from app.core.exceptions import QuantumLabError
from app.schemas.circuits import CircuitOperation, QuantumCircuitIR

ONE_QUBIT = {"id", "x", "y", "z", "h", "s", "sdg", "t", "tdg", "rx", "ry", "rz"}
TWO_QUBIT = {"cx", "cz", "swap"}
PARAMETERIZED = {"rx", "ry", "rz"}


def validate_circuit(circuit: QuantumCircuitIR, max_qubits: int = 12) -> None:
    if circuit.numQubits > max_qubits:
        raise QuantumLabError("CIRCUIT_TOO_LARGE", f"Synchronous simulation supports up to {max_qubits} qubits.")
    for index, op in enumerate(circuit.operations):
        _validate_operation(circuit, op, index)


def _validate_operation(circuit: QuantumCircuitIR, op: CircuitOperation, index: int) -> None:
    qubits = op.targets + op.controls
    if any(q < 0 or q >= circuit.numQubits for q in qubits):
        raise QuantumLabError("INVALID_QUBIT_INDEX", f"Operation {index} references a qubit outside the circuit.")
    if any(c < 0 or c >= max(circuit.numClbits, circuit.numQubits) for c in op.clbits):
        raise QuantumLabError("INVALID_CLBIT_INDEX", f"Operation {index} references an invalid classical bit.")
    if set(op.targets) & set(op.controls):
        raise QuantumLabError("CONTROL_TARGET_COLLISION", f"Operation {index} uses the same qubit as control and target.")
    if op.gate in ONE_QUBIT and len(op.targets) != 1:
        raise QuantumLabError("INVALID_GATE_ARITY", f"Gate {op.gate} requires exactly one target.")
    if op.gate in PARAMETERIZED and len(op.params) != 1:
        raise QuantumLabError("INVALID_PARAMETER_COUNT", f"Gate {op.gate} requires one angle parameter.")
    if op.gate in {"cx", "cz"} and (len(op.controls) != 1 or len(op.targets) != 1):
        raise QuantumLabError("INVALID_GATE_ARITY", f"Gate {op.gate} requires one control and one target.")
    if op.gate == "swap" and len(op.targets) != 2:
        raise QuantumLabError("INVALID_GATE_ARITY", "Swap requires two targets.")
    if op.gate == "measure" and len(op.targets) != len(op.clbits):
        raise QuantumLabError("INVALID_MEASUREMENT", "Measurement targets and classical bits must have equal length.")
