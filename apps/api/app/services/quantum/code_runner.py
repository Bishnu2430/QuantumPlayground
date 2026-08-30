import ast
import subprocess
import sys
import tempfile
from pathlib import Path

from app.core.exceptions import QuantumLabError

ALLOWED_IMPORT_ROOTS = {"qiskit", "qiskit_aer", "math", "cmath", "json", "numpy"}


def validate_code(code: str) -> None:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    raise QuantumLabError("IMPORT_NOT_ALLOWED", f"Import is not allowed: {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                raise QuantumLabError("IMPORT_NOT_ALLOWED", f"Import is not allowed: {module}")
        elif isinstance(node, (ast.Global, ast.Nonlocal)):
            raise QuantumLabError("CODE_NOT_ALLOWED", "global/nonlocal statements are disabled in the classroom runner.")


def run_python_code(code: str, timeout_seconds: int) -> dict[str, str | int]:
    validate_code(code)
    with tempfile.TemporaryDirectory(prefix="quantum-lab-") as tmpdir:
        script = Path(tmpdir) / "runner.py"
        script.write_text(code)
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=tmpdir,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
    return {"stdout": result.stdout, "stderr": result.stderr, "exitCode": result.returncode}
