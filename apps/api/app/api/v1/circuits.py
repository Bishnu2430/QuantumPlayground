from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.database import get_session
from app.db.models.circuit import Circuit, CircuitVersion
from app.db.models.user import User
from app.schemas.circuits import CircuitCreate, CircuitResponse, CircuitUpdate, QuantumCircuitIR
from app.services.quantum.circuit_validator import validate_circuit

router = APIRouter(tags=["circuits"])


def _out(c: Circuit) -> CircuitResponse:
    return CircuitResponse(id=c.id, owner_id=c.owner_id, title=c.title, description=c.description, circuit=QuantumCircuitIR.model_validate_json(c.ir_json), num_qubits=c.num_qubits, is_public=c.is_public, related_lesson_id=c.related_lesson_id, created_at=c.created_at.isoformat(), updated_at=c.updated_at.isoformat())


@router.get("", response_model=list[CircuitResponse])
def list_circuits(session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> list[CircuitResponse]:
    rows = (session.scalars(select(Circuit).where(or_(Circuit.owner_id == user.id, Circuit.is_public.is_(True))).order_by(Circuit.updated_at.desc()))).all()
    return [_out(c) for c in rows]


@router.post("", response_model=CircuitResponse, status_code=201)
def create_circuit(request: CircuitCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> CircuitResponse:
    validate_circuit(request.circuit)
    circuit = Circuit(owner_id=user.id, title=request.title, description=request.description, ir_json=request.circuit.model_dump_json(), num_qubits=request.circuit.numQubits, is_public=request.is_public, related_lesson_id=request.related_lesson_id)
    session.add(circuit)
    session.flush()
    session.add(CircuitVersion(circuit_id=circuit.id, version_number=1, ir_json=circuit.ir_json, change_summary="Initial version"))
    session.commit(); session.refresh(circuit)
    return _out(circuit)


@router.get("/{circuit_id}", response_model=CircuitResponse)
def get_circuit(circuit_id: str, session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> CircuitResponse:
    circuit = session.get(Circuit, circuit_id)
    if circuit is None or (circuit.owner_id != user.id and not circuit.is_public):
        raise HTTPException(status_code=404, detail="Circuit not found")
    return _out(circuit)


@router.patch("/{circuit_id}", response_model=CircuitResponse)
def update_circuit(circuit_id: str, request: CircuitUpdate, session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> CircuitResponse:
    circuit = session.get(Circuit, circuit_id)
    if circuit is None or circuit.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Circuit not found")
    if request.title is not None: circuit.title = request.title
    if request.description is not None: circuit.description = request.description
    if request.is_public is not None: circuit.is_public = request.is_public
    if request.circuit is not None:
        validate_circuit(request.circuit); circuit.ir_json = request.circuit.model_dump_json(); circuit.num_qubits = request.circuit.numQubits
        latest = session.query(CircuitVersion).filter(CircuitVersion.circuit_id == circuit.id).count() + 1
        session.add(CircuitVersion(circuit_id=circuit.id, version_number=latest, ir_json=circuit.ir_json, change_summary="API update"))
    session.commit(); session.refresh(circuit)
    return _out(circuit)


@router.delete("/{circuit_id}", status_code=204)
def delete_circuit(circuit_id: str, session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> None:
    circuit = session.get(Circuit, circuit_id)
    if circuit is None or circuit.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Circuit not found")
    session.delete(circuit); session.commit()
