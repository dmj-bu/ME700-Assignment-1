import numpy as np
import matplotlib.pyplot as plt

# Base class for material model
class MaterialModel:
    def __init__(self, E, yield_stress):
        self.E = E  # Elastic modulus
        self.yield_stress = yield_stress  # Initial yield stress
        self.plastic_strain = 0.0  # Plastic strain

    def stress(self, strain):
        raise NotImplementedError("Subclass must implement stress calculation!")

# Elastic model (No hardening)
class Elastic(MaterialModel):
    def stress(self, strain):
        return self.E * strain

# Isotropic Hardening Model
class IsotropicHardening(MaterialModel):
    def __init__(self, E, yield_stress, H):
        super().__init__(E, yield_stress)
        self.H = H  # Isotropic hardening modulus

    def stress(self, strain):
        total_strain = strain - self.plastic_strain
        trial_stress = self.E * total_strain

        if abs(trial_stress) > self.yield_stress:
            delta_plastic_strain = (abs(trial_stress) - self.yield_stress) / (self.E + self.H)
            self.plastic_strain += np.sign(trial_stress) * delta_plastic_strain
            self.yield_stress += self.H * delta_plastic_strain  # Update yield stress
            return np.sign(trial_stress) * self.yield_stress
        return trial_stress

# Kinematic Hardening Model
class KinematicHardening(MaterialModel):
    def __init__(self, E, yield_stress, H):
        super().__init__(E, yield_stress)
        self.H = H  # Hardening modulus
        self.backstress = 0.0  # Initial backstress

    def stress(self, strain):
        total_strain = strain - self.plastic_strain
        trial_stress = self.E * total_strain - self.backstress

        if abs(trial_stress) > self.yield_stress:
            delta_plastic_strain = (abs(trial_stress) - self.yield_stress) / self.E
            self.plastic_strain += np.sign(trial_stress) * delta_plastic_strain
            self.backstress += np.sign(trial_stress) * self.H * delta_plastic_strain  # Update backstress
            return np.sign(trial_stress) * self.yield_stress + self.backstress
        return trial_stress

# Material properties
E = 200e9  # Young's modulus (Pa)
yield_stress = 250e6  # Initial yield stress (Pa)
H = 10e9  # Hardening modulus (Pa)

# Create material models
elastic = Elastic(E, yield_stress)
iso_hardening = IsotropicHardening(E, yield_stress, H)
kin_hardening = KinematicHardening(E, yield_stress, H)

# Define cyclic strain path
strain_range = np.linspace(-0.02, 0.02, 100)
cyclic_strain = np.concatenate([strain_range, strain_range[::-1], strain_range, strain_range[::-1]])

# Store results
stress_elastic, stress_iso, stress_kin = [], [], []
backstress_kin = []

# Compute stress response
for strain in cyclic_strain:
    stress_elastic.append(elastic.stress(strain))
    stress_iso.append(iso_hardening.stress(strain))
    stress_kin.append(kin_hardening.stress(strain))
    backstress_kin.append(kin_hardening.backstress)

# Convert lists to numpy arrays for plotting
stress_elastic = np.array(stress_elastic)
stress_iso = np.array(stress_iso)
stress_kin = np.array(stress_kin)
backstress_kin = np.array(backstress_kin)

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Stress-Strain Plot
axes[0].plot(cyclic_strain, stress_elastic, label="Elastic (No Hardening)", color="blue")
axes[0].plot(cyclic_strain, stress_iso, label="Isotropic Hardening", color="orange")
axes[0].plot(cyclic_strain, stress_kin, label="Kinematic Hardening", color="green")
axes[0].axhline(y=yield_stress, color="red", linestyle="dashed", label="Yield Stress")
axes[0].axhline(y=-yield_stress, color="red", linestyle="dashed")

axes[0].set_xlabel("Strain")
axes[0].set_ylabel("Stress (Pa)")
axes[0].set_title("Cyclic Loading: Elastic, Isotropic, and Kinematic Hardening")
axes[0].legend()

# Backstress Plot
axes[1].plot(cyclic_strain, backstress_kin, label="Kinematic Hardening", color="green")
axes[1].set_xlabel("Strain")
axes[1].set_ylabel("Backstress (Pa)")
axes[1].set_title("Backstress Evolution")
axes[1].legend()

plt.tight_layout()
plt.show()
