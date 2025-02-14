import sys
import numpy as np
from pathlib import Path

# Ensure Python recognizes src/
sys.path.append(str(Path(__file__).resolve().parent.parent / "src/Newtons-Method"))

from newtons_method_solver import newtons_method

def test_newtons_method():
    func_str = "(np.pi**2 * E * I / w**2) - P"
    dfunc_str = "-2 * np.pi**2 * E * I / w**3"
    variables = {"E": 200e9, "I": 5e-6, "P": 5000}
    root = newtons_method(func_str, dfunc_str, w0=10, variables=variables, tol=1e-4)

    expected_value = np.sqrt((np.pi**2 * 200e9 * 5e-6) / 5000)  # Correct value
    assert np.isclose(root, expected_value, atol=1e-4), f"Root incorrect: {root}"
