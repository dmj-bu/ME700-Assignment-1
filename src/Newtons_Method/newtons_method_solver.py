import numpy as np

def evaluate_function(func_str, w_value, variables):
   
    try:
        variables["w"] = w_value  
        return eval(func_str, {"np": np}, variables)
    except Exception as e:
        print(f"Error evaluating function: {e}")
        return None

def newtons_method(func_str, dfunc_str, w0, variables, tol=1e-6, max_iter=500):

    iter_count = 0
    w_value = w0
    w_min = 1e-3  # Minimum allowed w to avoid sqrt issues

    while iter_count < max_iter:
        f_val = evaluate_function(func_str, w_value, variables)
        df_val = evaluate_function(dfunc_str, w_value, variables)

        if df_val == 0 or df_val is None:
            print("Error: Derivative is zero or undefined. Newton's method failed to converge.")
            return None

        # Compute the Newton step
        step = f_val / df_val

        # Prevent Newton's Method from making extreme changes
        if abs(step) > abs(w_value) * 0.5:  # Limits update to 50% of current value
            step = np.sign(step) * abs(w_value) * 0.5

        w_new = w_value - step

        # Ensure w does not become non-physical
        if w_new <= 0:
             print(f"Warning: Adjusting w from {w_new} to minimum allowed {w_min}.")
             return w_min  # Explicitly return here


        if abs(w_new - w_value) < tol:
            return w_new  # Root found

        w_value = w_new
        iter_count += 1

    print("Newton's method did not converge.")
    return None

