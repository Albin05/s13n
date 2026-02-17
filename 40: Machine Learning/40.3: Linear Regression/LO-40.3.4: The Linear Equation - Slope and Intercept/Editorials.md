
# Editorials

## Q1
### Title
Geometric Transformations

### Problem Description
Identify how to shift a line up.

### Objective
Visualize the effect of parameters.

### Hint
Slope rotates; Intercept shifts.

### Short Explanation
Increasing the Intercept ($\theta_0$) adds a constant value to every $y$, shifting the entire line vertically upwards.

### Detailed Explanation
* **Slope:** Changes angle.
* **Intercept:** Changes vertical position. To move up, add to the intercept.
* **Answer:** D.

---

## Q2
### Title
Deriving Line Parameters

### Problem Description
Calculate m and c from two points.

### Objective
Implement analytic geometry formulas.

### Hint
Rise over Run for slope. Substitute for intercept.

### Short Explanation
Calculate $m$, then solve $y = mx + c$ for $c$.

### Detailed Explanation
```python
def get_line_params(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    if x2 - x1 == 0: return None # Vertical line
    
    m = (y2 - y1) / (x2 - x1)
    c = y1 - (m * x1)
    return m, c

```

---

## Q3

### Title

Slope Calculation

### Problem Description

Find slope between  and .

### Objective

Basic arithmetic.

### Hint

.

### Short Explanation

.

### Detailed Explanation

1. **Rise ( change):** .
2. **Run ( change):** .
3. **Slope:** .

---

## Q4

### Title

Origin Passing Lines

### Problem Description

Identify lines with .

### Objective

Link algebraic form to geometric property.

### Hint

If , is ?

### Short Explanation

A and C have an intercept of 0. B has intercept 1. D has intercept -5.

### Detailed Explanation

* **A:** . Yes.
* **B:** . No.
* **C:** . Yes.
* **D:** . No.

---

## Q5

### Title

Generating Linear Data

### Problem Description

Create data following .

### Objective

Data simulation.

### Hint

Use `numpy` vectorization.

### Short Explanation

Create range X, apply formula.

### Detailed Explanation

```python
import numpy as np
def generate_linear_data():
    X = np.arange(0, 11) # 0 to 10
    Y = 2.5 * X + 10
    return Y

```

---

## Q6

### Title

Interpreting Negative Parameters

### Problem Description

Explain negative slope/intercept in Housing context.

### Objective

Real-world interpretation of math.

### Hint

Slope = Impact. Intercept = Baseline.

### Short Explanation

* **Negative Slope:** Distance from City Center. As distance increases (), price () decreases.
* **Negative Intercept:** Often problematic physically (a house cannot have a negative price at size 0). However, it might be a mathematical artifact of the line of best fit for valid ranges (e.g., for houses  sq ft). A house of size 0 implies no house, so the model might predict  just to fit the trend of larger houses correctly.

```

```
