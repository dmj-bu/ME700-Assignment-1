# Elasto-Plastic Model Simulation

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)](https://github.com/dmj-bu/ME700-Assignment-1)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/dmj-bu/ME700-Assignment-1/blob/main/LICENSE)

[![codecov](https://codecov.io/gh/dmj-bu/ME700-Assignment-1/Elasto_Plastic_Model/graph/badge.svg?token=YOUR_CODECOV_TOKEN)]((https://codecov.io/gh/dmj-bu/ME700-Assignment-1/tree/main/src%2FElasto_Plastic_Model))
[![Run Tests](https://github.com/dmj-bu/ME700-Assignment-1/actions/workflows/tests.yml/badge.svg)](https://github.com/dmj-bu/ME700-Assignment-1/actions/workflows/tests.yml)

---
## Introduction

This repository provides a numerical solver for **elasto-plastic material behavior** under **cyclic loading**, implemented in Python.

The solver is structured into two files:

1. `elastoplastic_solver.py` – Contains the core solver logic.
2. `elastoplastic_tutorial.py` – Demonstrates usage with multiple examples.

---

## Installation & Usage

### 1: Clone the Repository

```bash
git clone https://github.com/dmj-bu/ME700-Assignment-1.git
cd ME700-Assignment-1
```
## **create and activate Conda environment**
```bash
conda create --name me700-tutorial python=3.12
conda activate me700-tutorial
```

### **2: Install Dependencies**
```bash
pip install -e .
```

### 4: Run the Tutorial
```bash
cd src/Elasto_Plastic_Model
python elastoplastic_tutorial.py
```

---

## How the Model Works

The model updates stress-strain behavior **incrementally**, based on:

1. **Elastic Stress Update** (Hooke's Law):
```math
\sigma_{\text{trial}} = E (\varepsilon - \varepsilon_{\text{plastic}})
```
2. **Plastic Flow Condition**:
   - If $|\sigma_{\text{trial}}| \leq \sigma_Y$, the material remains **elastic**.
   - If $|\sigma_{\text{trial}}| > \sigma_Y$, **plastic deformation** occurs.

3. **Hardening Behavior**:
   - **No Hardening**: The yield stress is constant.
   - **Isotropic Hardening**: Yield stress increases with plastic strain.
   - **Kinematic Hardening**: Yield surface translates without expanding.
   - **Mixed Hardening**: Combination of isotropic and kinematic hardening.

---
## Running the Model

Execute the tutorial script:
```sh
python elastoplastic_tutorial.py
```
This will generate **five separate stress-strain plots**, each corresponding to a different hardening model.

---
## Example Cases: Stress-Strain Response Under Cyclic Loading
Each example below varies the material hardening parameters while keeping the Young’s modulus and yield stress constant.

### Example 1: Elastic (No Hardening)

#### Parameters:
```
E = 200 GPa, σ_Y = 250 MPa, K = 0, H = 0
```
#### Behavior:
   - The material remains elastic for all strains.
   - No plastic deformation occurs.
   - Stress-strain behavior follows a linear path.
#### Implementation:
```python
model1 = ElastoplasticSolver(sigma_y=250e6, E=200e9, K=0, H=0)
stress1 = model1.compute_stress_strain(strain_range)
```
---

### Example 2: Isotropic Hardening

#### Parameters:
```
E = 200 GPa, σ_Y = 250 MPa, K = 50 MPa, H = 0
```
#### Behavior:
   - The yield stress increases with plastic strain.
   - The stress-strain curve expands outward due to hardening.
   - No shifting of the yield surface occurs.
#### Implementation:
```python
model2 = ElastoplasticSolver(sigma_y=250e6, E=200e9, K=50e6, H=0)
stress2 = model2.compute_stress_strain(strain_range)
```

---

### Example 3: Kinematic Hardening

#### Parameters:
```
E = 200 GPa, σ_Y = 250 MPa, K = 0, H = 50 MPa
```
#### Behavior:
   - The yield surface shifts left and right but does not expand.
   - The stress-strain curve remains bounded within the same yield stress.
   - The material yields earlier in the opposite loading direction.
#### Implementation:
```python
model3 = ElastoplasticSolver(sigma_y=250e6, E=200e9, K=0, H=50e6)
stress3 = model3.compute_stress_strain(strain_range)
```

---

### Example 4: Mixed Hardening (Equal Contributions)

#### Parameters:
```
E = 200 GPa, σ_Y = 250 MPa, K = 25 MPa, H = 25 MPa
```
#### Behavior:
   - A combination of isotropic and kinematic hardening.
   - Yield surface expands and shifts simultaneously.
   - Stress-strain curves display gradual changes in yielding.
#### Implementation:
```python
model4 = ElastoplasticSolver(sigma_y=250e6, E=200e9, K=25e6, H=25e6)
stress4 = model4.compute_stress_strain(strain_range)
```

---

### Example 5: Mixed Hardening (More Isotropic)

#### Parameters:
```
E = 200 GPa, σ_Y = 250 MPa, K = 75 MPa, H = 10 MPa
```
#### Behavior:
   - Yield stress increases significantly due to dominant isotropic hardening.
   - The kinematic hardening component results in some shifting of the yield surface.
   - The stress-strain curve shows asymmetric hardening.
#### Implementation:
```python
model5 = ElastoplasticSolver(sigma_y=250e6, E=200e9, K=75e6, H=10e6)
stress5 = model5.compute_stress_strain(strain_range)
```
---
