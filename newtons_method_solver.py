import numpy as np
import sympy as sp

def evaluate_function(func_expr, w_value, variables):
    """
    Evaluates a symbolic function numerically at a given value of w.

    Parameters:
    - func_expr: A SymPy expression representing the function.
    - w_value: Numerical value of w at which to evaluate.
    - variables: Dictionary containing variable values.

    Returns:
    - Evaluated function value at w_value.
    """
    try:
        # Create a numerical function from the symbolic function
        func_lambda = sp.lambdify(['w'] + list(variables.keys()), func_expr, modules=["numpy"])
        return func_lambda(w_value, **variables)
    except Exception as e:
        print(f"Error evaluating function: {e}")
        return None

def newtons_method(func_str, w0, variables, tol=1e-6, max_iter=100):
    """
    Implements Newton's Method to find a root of func(w) using automatic differentiation.

    Parameters:
    - func_str: Function as a string.
    - w0: Initial guess for the root.
    - variables: Dictionary of additional variables.
    - tol: Tolerance for stopping condition.
    - max_iter: Maximum number of iterations.

    Returns:
    - Approximate root or None if convergence fails.
    """
    w = sp.Symbol('w')  # Define symbolic variable
    func_expr = sp.sympify(func_str)  # Convert string to symbolic expression
    dfunc_expr = sp.diff(func_expr, w)  # Compute derivative

    iter_count = 0
    w_value = w0

    while iter_count < max_iter:
        f_val = evaluate_function(func_expr, w_value, variables)
        df_val = evaluate_function(dfunc_expr, w_value, variables)

        if df_val == 0:
            print("Derivative is zero. Newton's method failed to converge.")
            return None

        w_new = w_value - f_val / df_val

        if abs(w_new - w_value) < tol:
            return w_new  # Root found

        w_value = w_new
        iter_count += 1

    print("Newton's method did not converge within the maximum number of iterations.")
    return None
