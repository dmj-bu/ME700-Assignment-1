import sys
import numpy as np
from pathlib import Path

# Ensure Python recognizes src/
sys.path.append(str(Path(__file__).resolve().parent.parent / "src/Newtons_Method"))

from newtons_method_solver import newtons_method, evaluate_function

def test_newtons_method():
    func_str = "(np.pi**2 * E * I / w**2) - P"
    dfunc_str = "-2 * np.pi**2 * E * I / w**3"
    variables = {"E": 200e9, "I": 5e-6, "P": 5000}
    root = newtons_method(func_str, dfunc_str, w0=10, variables=variables, tol=1e-4)

    expected_value = np.sqrt((np.pi**2 * 200e9 * 5e-6) / 5000)  # Correct value
    assert np.isclose(root, expected_value, atol=1e-4), f"Root incorrect: {root}"


# 1 Test invalid function string (exception handling)
def test_evaluate_function_invalid():
    func_str = "invalid_func(w)"  # Invalid function
    variables = {"x": 5}  # Missing "w"
    result = evaluate_function(func_str, 2, variables)
    assert result is None  # Ensure it handles the error correctly


# 2 Test derivative becomes zero
def test_newtons_method_zero_derivative():
    func_str = "w**2 - 4"
    dfunc_str = "2*w"  # The derivative is 0 when w = 0
    variables = {}

    result = newtons_method(func_str, dfunc_str, 0, variables)
    assert result is None  # Should return None due to derivative being zero


# 3 Test Newton’s method step limiting
def test_newtons_method_step_size_limiting():
    func_str = "w**3 - 8"  # Root at w = 2
    dfunc_str = "3*w**2"  # Large derivative at large w
    variables = {}

    result = newtons_method(func_str, dfunc_str, 50, variables)  # Large w0
    assert result is not None  # Ensure method still converges


# 4 Test w_new adjusting to minimum allowed value
def test_newtons_method_min_w_adjustment():
    func_str = "w - 10"
    dfunc_str = "1"  # Constant derivative
    variables = {}

    result = newtons_method(func_str, dfunc_str, -5, variables)  # Start below zero
    assert result == 1e-3  # Should adjust to w_min


# 5️ Test Newton’s method non-convergence
def test_newtons_method_non_convergence():
    func_str = "w**2 + 1"  # Always positive, no real roots
    dfunc_str = "2*w"
    variables = {}

    result = newtons_method(func_str, dfunc_str, 1, variables)  # Start at w=1
    assert result is None  # Should return None due to non-convergence
