import numpy as np

def evaluate_function(func_str, w_value, variables):
    # Evaluates a user-defined function at a given value of w.

    #Parameters:
    #- func_str: A string representing the function (e.g., "2*k*(np.sqrt(l**2 + w**2) - l)*(w / np.sqrt(l**2 + w**2)) - F")
    #- w_value: Numerical value of w at which to evaluate
    #- variables: Dictionary containing variable values, including 'w'

    #Returns:
    #- Evaluated function value at w_value
    
    try:
        # Ensure 'w' is in the variables dictionary
        variables["w"] = w_value

        # Evaluate the function
        return eval(func_str, {"np": np}, variables)
    except:
        # Error handling in case of mathematical mistake
        print("Something went wrong! Please check your function.")


def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    #Implements the Bisection Method to find a root of func(w) in [a, b].

    #Parameters:
    #- func: Function to find the root of
    #- a, b: Interval in which the root is searched
    #- tol: Tolerance for stopping condition
    #- max_iter: Maximum number of iterations

    #Returns:
    #- Root of the function within given tolerance
    
    if a >= b:
        raise ValueError("Lower bound 'a' must be less than upper bound 'b'.")

    if func(a) * func(b) >= 0:
        raise ValueError("Function values at 'a' and 'b' must have opposite signs.")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        #Prevent infinite loop by limiting iterations
        mid = (a + b) / 2
        f_mid = func(mid)

        if f_mid == 0 or (b - a) / 2 < tol:
            return mid  # Found the root

        if func(a) * f_mid < 0:
            b = mid  # Root is in left half
        else:
            a = mid  # Root is in right half

        iter_count += 1

    return (a + b) / 2  # Approximate root

def get_user_input():
    #Prompts the user for an equation and necessary variables.
    print("\nWelcome to the Bisection Method Solver!")
    print("Enter your equation in terms of 'w' using Python syntax.")
    print("Example: 2*k*(np.sqrt(l**2 + w**2) - l)*(w / np.sqrt(l**2 + w**2)) - F")

    func_str = input("Enter function f(w): ")

    # Extract variable names (except 'np' and 'w')
    variables = {}
    while True:
        try:
            var_names = input("Enter variable names (comma-separated, excluding 'w'): ").split(',')
            for var in var_names:
                var = var.strip()
                if var and var != "w":
                    variables[var] = float(input(f"Enter value for {var}: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for all variables.")

    # Ask for the interval [a, b]
    while True:
        try:
            a = float(input("Enter the lower bound (a): "))
            b = float(input("Enter the upper bound (b): "))
            if a >= b:
                print("Lower bound must be less than the upper bound. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    # Ask for the tolerance
    while True:
        try:
            tol = float(input("Enter tolerance (e.g., 1e-6): "))
            if tol <= 0:
                print("Tolerance must be a positive number. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    return func_str, variables, a, b, tol

#Get user input
func_str, variables, a, b, tol = get_user_input()

# Define function wrapper for numerical evaluation
def user_function(w_value):
    return evaluate_function(func_str, w_value, variables)

# Check if the function values at a and b bracket a root
try:
    root = bisection_method(user_function, a, b, tol=tol)
    print(f"Root found: w = {root}")
except ValueError:
    print("Something went wrong. Please check your inputs.")
