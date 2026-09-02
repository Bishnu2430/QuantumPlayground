from qiskit import QuantumCircuit, transpile


def transpile_for_backend(circuit: QuantumCircuit, basis_gates: list[str] | None = None) -> QuantumCircuit:
    return transpile(circuit, basis_gates=basis_gates, optimization_level=1)
