from newtons_method_solver import newtons_method

def run_examples():
    print("\n### Running Newton's Method Examples ###\n")

       # Example 1: Beam Deflection (Cantilever Beam)
    func_str = "(3 * E * I / L**3) * w - F"
    variables = {"E": 200e9, "I": 1e-6, "L": 2, "F": 1000}
    root = newtons_method(func_str, w0=0.05, variables=variables, tol=1e-6)
    print(f"Example 1 (Beam Deflection) root: {root}\n")

    # Example 2: Buckling Load of a Column (Euler’s Buckling)
    func_str = "(np.pi**2 * E * I / w**2) - P"
    variables = {"E": 200e9, "I": 5e-6, "P": 5000}
    root = newtons_method(func_str, w0=5, variables=variables, tol=1e-6)
    print(f"Example 2 (Buckling Load) root: {root}\n")

    # Example 3: Natural Frequency of a Simple Pendulum
    func_str = "(1 / (2 * np.pi)) * np.sqrt(g / w) - 1"
    variables = {"g": 9.81}
    root = newtons_method(func_str, w0=1, variables=variables, tol=1e-6)
    print(f"Example 3 (Pendulum Frequency) root: {root}\n")

    # Example 4: Projectile Motion – Finding Time of Flight
    func_str = "v0 * np.sin(theta) * w - 0.5 * g * w**2"
    variables = {"v0": 20, "theta": np.pi / 4, "g": 9.81}
    root = newtons_method(func_str, w0=2, variables=variables, tol=1e-6)
    print(f"Example 4 (Projectile Motion) root: {root}\n")

    # Example 5: Torsional Vibration of a Shaft
    func_str = "np.sqrt(K / w) - omega"
    variables = {"K": 1000, "omega": 50}
    root = newtons_method(func_str, w0=0.5, variables=variables, tol=1e-6)
    print(f"Example 5 (Torsional Vibration) root: {root}\n")

if __name__ == "__main__":
    run_examples()
