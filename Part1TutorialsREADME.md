# Newton's Method Solver

## **Introduction**
**How It Works**
1. **User provides a function and its derivative**
2. **Newton's Method iteratively refines the guess (`w`)** using:
   ```math
   w_{\text{new}} = w_{\text{old}} - \frac{f(w)}{f'(w)}
   ```

## **Installation & Usage**
### **1️: Clone the Repository**
```bash
git clone https://github.com/yourusername/newton-method-solver.git
cd newton-method-solver
```

### **2️2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️: Run the Tutorial**
```bash
python newtons_method_tutorial.py
```
This will execute Newton’s Method on multiple real-world physics and engineering examples.

---

## **Example Problems**
The following **mechanics-related problems** are solved using Newton’s Method.

### **Example 1: Beam Deflection (Cantilever Beam)**
Find the deflection \( w \) for given **force, elastic modulus, moment of inertia, and length**.

#### **Equation:**
```math
(3EI/L^3) w - F = 0
```

#### **Derivative:**
```math
\frac{d}{dw} = 3EI/L^3
```

#### **Python Code:**
```python
func_str = "(3 * E * I / L**3) * w - F"
dfunc_str = "(3 * E * I / L**3)"  # Derivative w.r.t w
variables = {"E": 200e9, "I": 1e-6, "L": 2, "F": 1000}
root = newtons_method(func_str, dfunc_str, w0=0.05, variables=variables, tol=1e-4)
```

---

### **Example 2: Buckling Load of a Column**
Find the **minimum column length \( w \) that causes buckling**.

#### **Equation:**
```math
\frac{\pi^2 E I}{w^2} - P = 0
```

#### **Derivative:**
```math
\frac{d}{dw} = -2 \frac{\pi^2 E I}{w^3}
```

#### **Python Code:**
```python
func_str = "(np.pi**2 * E * I / w**2) - P"
dfunc_str = "-2 * np.pi**2 * E * I / w**3"
variables = {"E": 200e9, "I": 5e-6, "P": 5000}
root = newtons_method(func_str, dfunc_str, w0=10, variables=variables, tol=1e-4)
```

---

### **Example 3: Natural Frequency of a Simple Pendulum**
Find the **pendulum length \( w \) that gives a 1 Hz frequency**.

#### **Equation:**
```math
\frac{1}{2\pi} \sqrt{\frac{g}{w}} - 1 = 0
```

#### **Derivative:**
```math
\frac{d}{dw} = -\frac{1}{4\pi} \frac{g}{w^{3/2} \sqrt{g}}
```

#### **Python Code:**
```python
func_str = "(1 / (2 * np.pi)) * np.sqrt(g / w) - 1"
dfunc_str = "-(1 / (4 * np.pi * np.sqrt(g))) * w**(-3/2)"
variables = {"g": 9.81}
root = newtons_method(func_str, dfunc_str, w0=10, variables=variables, tol=1e-4)
```

---

### **Example 4: Projectile Motion – Finding Time of Flight**
Find the **time \( w \) for a projectile to reach the ground**.

#### **Equation:**
```math
v_0 \sin(\theta) w - \frac{1}{2} g w^2 = 0
```

#### **Derivative:**
```math
\frac{d}{dw} = v_0 \sin(\theta) - g w
```

#### **Python Code:**
```python
func_str = "v0 * np.sin(theta) * w - 0.5 * g * w**2"
dfunc_str = "v0 * np.sin(theta) - g * w"
variables = {"v0": 20, "theta": np.pi / 4, "g": 9.81}
root = newtons_method(func_str, dfunc_str, w0=2, variables=variables, tol=1e-4)
```

---

### **Example 5: Torsional Vibration of a Shaft**
Find the **natural frequency \( w \) of a torsional vibrating shaft**.

#### **Equation:**
```math
\sqrt{\frac{K}{w}} - \omega = 0
```

#### **Derivative:**
```math
\frac{d}{dw} = -\frac{1}{2} \frac{K^{1/2}}{w^{3/2}}
```

#### **Python Code:**
```python
func_str = "np.sqrt(K / w) - omega"
dfunc_str = "-(0.5 * np.sqrt(K)) / (w**(3/2))"
variables = {"K": 1000, "omega": 50}
root = newtons_method(func_str, dfunc_str, w0=0.5, variables=variables, tol=1e-4)
```

---
