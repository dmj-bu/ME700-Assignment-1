# Newton's Method Solver

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/newton-method-solver.git
   cd newton-method-solver
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tutorial:
   ```bash
   python newtons_method_tutorial.py
   ```

---

## Example Problems
The following problems are solved using Newton’s Method.

### **Example 1: Beam Deflection (Cantilever Beam)**
Find the deflection \( w \) for given **force, elastic modulus, moment of inertia, and length**.

```python
func_str = "(3 * E * I / L**3) * w - F"
variables = {"E": 200e9, "I": 1e-6, "L": 2, "F": 1000}
root = newtons_method(func_str, w0=0.05, variables=variables, tol=1e-6)
print(f"Example 1 root: {root}")
```

---

### **Example 2: Buckling Load of a Column**
Find the **minimum column length \( L \) that causes buckling**.

```python
func_str = "(np.pi**2 * E * I / w**2) - P"
variables = {"E": 200e9, "I": 5e-6, "P": 5000}
root = newtons_method(func_str, w0=5, variables=variables, tol=1e-6)
print(f"Example 2 root: {root}")
```

---

### **Example 3: Natural Frequency of a Simple Pendulum**
Find the **length \( L \) for a pendulum** with a **1 Hz frequency**.

```python
func_str = "(1 / (2 * np.pi)) * np.sqrt(g / w) - 1"
variables = {"g": 9.81}
root = newtons_method(func_str, w0=1, variables=variables, tol=1e-6)
print(f"Example 3 root: {root}")
```

---

### **Example 4: Projectile Motion – Finding Time of Flight**
Find the **time \( t \) when the projectile returns to the ground**.

```python
func_str = "v0 * np.sin(theta) * w - 0.5 * g * w**2"
variables = {"v0": 20, "theta": np.pi / 4, "g": 9.81}
root = newtons_method(func_str, w0=2, variables=variables, tol=1e-6)
print(f"Example 4 root: {root}")
```

---

### **Example 5: Torsional Vibration of a Shaft**
Find the **polar moment of inertia \( J \)** for a given **torsional vibration frequency**.

```python
func_str = "np.sqrt(K / w) - omega"
variables = {"K": 1000, "omega": 50}
root = newtons_method(func_str, w0=0.5, variables=variables, tol=1e-6)
print(f"Example 5 root: {root}")
```

---

## Running Tests & Code Coverage
This project integrates **Codecov** for automated testing and code coverage.

1. Install testing dependencies:
   ```bash
   pip install pytest pytest-cov codecov
   ```
2. Run tests:
   ```bash
   pytest --cov=newtons_method_solver
   ```
3. Upload coverage results:
   ```bash
   codecov
   ```


