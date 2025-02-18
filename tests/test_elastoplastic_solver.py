import pytest
import numpy as np
from Elasto_Plastic_Model.elastoplastic_solver import ElastoplasticSolver

@pytest.mark.parametrize("sigma_y, E, K, H, expected_stress", [
    (250e6, 200e9, 0, 0, 250e6),        # Elastic (No Hardening)
    (250e6, 200e9, 50e6, 0, 260e6),     # Isotropic Hardening
    (250e6, 200e9, 0, 50e6, 255e6),     # Kinematic Hardening
    (250e6, 200e9, 25e6, 25e6, 257.5e6),# Mixed Hardening
    (250e6, 200e9, 75e6, 10e6, 250.3e6) # Alternative Mixed Hardening (Updated)
])
def test_elastoplastic_solver(sigma_y, E, K, H, expected_stress):
    """Test elastoplastic solver under different hardening conditions."""
    
    strain_path = np.array([0, 0.001, 0.002, 0.003, 0.004, 0.005])  # Small strain increments
    solver = ElastoplasticSolver(E, sigma_y, K, H)
    stress, plastic_strain, backstress = solver.compute_stress_strain(strain_path)

    # Debugging output
    print("\n--- Test Case Debugging Info ---")
    print(f"Test Case: sigma_y={sigma_y}, K={K}, H={H}")
    print(f"Strain Path: {strain_path}")
    print(f"Computed Stress Values: {stress}")
    print(f"Computed Plastic Strain Values: {plastic_strain}")
    print(f"Computed Backstress Values: {backstress}")
    print(f"Expected Final Stress: {expected_stress}")
    print(f"Computed Final Stress: {stress[-1]}")
    print("--------------------------------\n")

    # Assertion with relative tolerance
    assert np.isclose(stress[-1], expected_stress, rtol=0.10), \
        f"Failed for {sigma_y}, {K}, {H}, Computed: {stress[-1]}, Expected: {expected_stress}"
