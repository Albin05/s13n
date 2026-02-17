
# Editorials

## Q1
### Title
Identifying Intercepts

### Problem Description
Identify the constant term in $y = mx + c$.

### Objective
Map equation components to definitions.

### Hint
The intercept stands alone (no x attached).

### Short Explanation
In $y = 5x - 2$, the term without $x$ is $-2$. This is the Y-Intercept ($c$).

### Detailed Explanation
* $m$ (Slope) = 5
* $c$ (Intercept) = -2

---

## Q2
### Title
Linear Equation Implementation

### Problem Description
Implement $y = mx + c$.

### Objective
Basic coding of the formula.

### Hint
Return `m * x + c`.

### Short Explanation
Standard arithmetic.

### Detailed Explanation
```python
def calculate_y(x, m, c):
    return (m * x) + c

```

For input `(4, 2, 1)`: .

---

## Q3

### Title

Negative Slope Calculation

### Problem Description

Calculate time after training.
Start: 60 mins.
Rate: -2 mins/hour.
Hours: 5.

### Objective

Apply linear logic with a negative slope.

### Hint

.

### Short Explanation

.

### Detailed Explanation

1. **Intercept ():** 60 (Baseline).
2. **Slope ():** -2 (Decreases by 2 per hour).
3. **Equation:**  minutes.

---

## Q4

### Title

Identifying Non-Linearity

### Problem Description

Select relationships that do not form a straight line.

### Objective

Distinguish Linear from Polynomial/Exponential.

### Hint

Look for squares or exponents.

### Short Explanation

A and C are non-linear. B and D are linear.

### Detailed Explanation

* **A (Non-Linear):** . Quadratic curve (Parabola).
* **B (Linear):** Cost increases proportionally to weight.
* **C (Non-Linear):** Exponential growth (). J-Curve.
* **D (Linear):** . Straight line.

---

## Q5

### Title

Linearity Check

### Problem Description

Check if slope is constant across points.

### Objective

Algorithmic verification of linearity.

### Hint

Calculate  for all adjacent pairs.

### Short Explanation

Calculate slopes between consecutive points. If all are equal, it's linear.

### Detailed Explanation

```python
def check_linearity(x, y):
    if len(x) < 2: return True
    # Calculate first slope
    slope = (y[1] - y[0]) / (x[1] - x[0])
    
    for i in range(2, len(x)):
        current_slope = (y[i] - y[i-1]) / (x[i] - x[i-1])
        if current_slope != slope:
            return False
    return True

```

---

## Q6

### Title

Forcing Linearity

### Problem Description

Why is fitting a line to a curve bad?

### Objective

Discuss "Underfitting" (High Bias).

### Hint

Draw a U-shape. Try to put a straight stick through it.

### Short Explanation

A straight line has a constant rate of change. A curve has a changing rate. Fitting a line to a curve results in **Underfitting**.

### Detailed Explanation

* **Example:** Bacterial Growth (Exponential).
* If you fit a straight line to the early slow growth, the line will vastly **underestimate** the explosion in growth later on.
* If you fit it to the later growth, it will overestimate the beginning.


* **Result:** The model captures the "average" trend but is wrong almost everywhere else.

```

```
