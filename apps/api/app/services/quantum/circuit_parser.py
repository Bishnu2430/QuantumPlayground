from app.schemas.circuits import CircuitOperation, QuantumCircuitIR


def bell_state() -> QuantumCircuitIR:
    return QuantumCircuitIR(
        numQubits=2,
        numClbits=2,
        operations=[
            CircuitOperation(gate="h", targets=[0], moment=0),
            CircuitOperation(gate="cx", controls=[0], targets=[1], moment=1),
            CircuitOperation(gate="measure", targets=[0, 1], clbits=[0, 1], moment=2),
        ],
    )
