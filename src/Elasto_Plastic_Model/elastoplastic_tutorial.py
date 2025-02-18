import numpy as np
import matplotlib.pyplot as plt
from Elasto_Plastic_Model.elastoplastic_solver import ElastoplasticSolver

def run_examples():
    print("\n### Running Elastoplastic Model Examples ###\n")

    # Define strain range for all examples
    strain_amplitude = 0.02
    n_cycles = 3
    n_points_per_cycle = 100
    strain_path = np.concatenate([
        np.linspace(0, strain_amplitude, n_points_per_cycle),
        np.linspace(strain_amplitude, -strain_amplitude, 2 * n_points_per_cycle),
        np.linspace(-strain_amplitude, 0, n_points_per_cycle)
    ] * n_cycles)

    # Example configurations
    examples = [
        ("Elastic (No Hardening)", 250e6, 200e9, 0, 0),
        ("Isotropic Hardening", 250e6, 200e9, 50e6, 0),
        ("Kinematic Hardening", 250e6, 200e9, 0, 50e6),
        ("Mixed Hardening", 250e6, 200e9, 25e6, 25e6),
        ("Alternative Mixed Hardening", 250e6, 200e9, 75e6, 10e6),
    ]

    for title, sigma_y, E, K, H in examples:
        print(f"Running: {title}")

        # Initialize solver
        model = ElastoplasticSolver(E, sigma_y, K, H)

        # Compute stress-strain response
        stress, plastic_strain, backstress = model.compute_stress_strain(strain_path)

        # Plot stress-strain curve
        plt.figure(figsize=(8, 6))
        plt.plot(strain_path, stress, label=title, color='b')
        plt.xlabel("Strain")
        plt.ylabel("Stress (Pa)")
        plt.title(f"Stress-Strain Response: {title}")
        plt.legend()
        plt.grid(True)
        
        # Only show plots if NOT running inside pytest
        if "pytest" not in sys.modules:
            plt.show()
        else:
            plt.close()  # Close figure to prevent blocking in CI
if __name__ == "__main__":
    run_examples()
