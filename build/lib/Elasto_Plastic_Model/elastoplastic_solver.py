import numpy as np

class ElastoplasticSolver:
    def __init__(self, E, sigma_y, K, H):
        """
        Initialize the elastoplastic solver with material properties.

        :param E: Elastic modulus (Pa)
        :param sigma_y: Yield stress (Pa)
        :param K: Isotropic hardening modulus (Pa)
        :param H: Kinematic hardening modulus (Pa)
        """
        self.E = E
        self.sigma_y = sigma_y
        self.K = K
        self.H = H

    def compute_stress_strain(self, strain_path):
        """
        Compute stress-strain response using an elastoplastic material model.

        :param strain_path: Array of strain values
        :return: Arrays of stress, plastic strain, and backstress
        """
        n_steps = len(strain_path)
        stress = np.zeros(n_steps)
        plastic_strain = np.zeros(n_steps)
        backstress = np.zeros(n_steps)

        for i in range(1, n_steps):
            delta_strain = strain_path[i] - strain_path[i - 1]
            trial_stress = stress[i - 1] + self.E * delta_strain
            yield_condition = abs(trial_stress - backstress[i - 1]) - (self.sigma_y + self.K * plastic_strain[i - 1])

            if yield_condition > 0:
                delta_plastic_strain = yield_condition / (self.E + self.K + self.H)
                sign = np.sign(trial_stress - backstress[i - 1])
                stress[i] = trial_stress - self.E * delta_plastic_strain * sign
                plastic_strain[i] = plastic_strain[i - 1] + delta_plastic_strain
                backstress[i] = backstress[i - 1] + self.H * delta_plastic_strain * sign
            else:
                stress[i] = trial_stress
                plastic_strain[i] = plastic_strain[i - 1]
                backstress[i] = backstress[i - 1]

        return stress, plastic_strain, backstress

