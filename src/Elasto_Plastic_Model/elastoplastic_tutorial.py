import numpy as np
import matplotlib.pyplot as plt
from Elasto_Plastic_Model.elastoplastic_solver import ElastoplasticSolver

# Material Properties
E = 200e9  # Young's modulus (Pa)
sigma_y = 250e6  # Yield stress (Pa)
K = 1e9  # Isotropic hardening modulus (Pa)
H = 10e9  # Kinematic hardening modulus (Pa)

# Define a cyclic strain path
strain_amplitude = 0.02
n_cycles = 3
n_points_per_cycle = 100
strain_path = np.concatenate([
    np.linspace(0, strain_amplitude, n_points_per_cycle),
    np.linspace(strain_amplitude, -strain_amplitude, 2 * n_points_per_cycle),
    np.linspace(-strain_amplitude, 0, n_points_per_cycle)
] * n_cycles)

# Initialize solver
solver = ElastoplasticSolver(E, sigma_y, K, H)

# Compute stress-strain response
stress, plastic_strain, backstress = solver.compute_stress_strain(strain_path)

# Plot stress-strain curve
plt.figure(figsize=(8, 6))
plt.plot(strain_path, stress, label="Stress-Strain", color='b')
plt.xlabel("Strain")
plt.ylabel("Stress (Pa)")
plt.title("Elastoplastic Stress-Strain Response")
plt.legend()
plt.grid(True)
plt.show()

# Plot plastic strain evolution
plt.figure(figsize=(8, 6))
plt.plot(strain_path, plastic_strain, label="Plastic Strain", color='r')
plt.xlabel("Strain")
plt.ylabel("Plastic Strain")
plt.title("Plastic Strain Evolution")
plt.legend()
plt.grid(True)
plt.show()

# Plot backstress evolution
plt.figure(figsize=(8, 6))
plt.plot(strain_path, backstress, label="Backstress", color='g')
plt.xlabel("Strain")
plt.ylabel("Backstress (Pa)")
plt.title("Backstress Evolution")
plt.legend()
plt.grid(True)
plt.show()

