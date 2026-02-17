
# Editorials

## Q1
### Title
Residual Plots

### Problem Description
Identify the best plot for checking linearity.

### Objective
Visual diagnostics.

### Hint
If the model fits well, the errors should be random noise.

### Short Explanation
**Residual Plot:** If the residuals show a pattern (like a curve or a U-shape), it means the linear model failed to capture some non-linear trend. If they are random noise, the linear model is appropriate.

### Detailed Explanation
* **Histogram:** Shows distribution, not relationship.
* **Pie Chart:** Useless for continuous data.
* **Residual Plot:** Specifically designed to show what the model *missed*.

---

## Q2
### Title
Plotting Residuals

### Problem Description
Code a visualizer for errors.

### Objective
Matplotlib skills.

### Hint
Use `plt.vlines` or `plt.plot([x, x], [y1, y2])`.

### Short Explanation
Iterate through points and draw lines.

### Detailed Explanation
```python
import matplotlib.pyplot as plt

def plot_residuals(x, y, model):
    y_pred = model(x)
    plt.scatter(x, y, label='Data')
    plt.plot(x, y_pred, color='red', label='Line')
    
    # Draw vertical lines
    plt.vlines(x, y, y_pred, colors='green', linestyles='dashed', label='Residuals')
    
    plt.legend()
    plt.show()

```

---

## Q3

### Title

Calculating Residual Squared

### Problem Description

Point: . Line: .
Calculate .

### Objective

Compute the geometric area of the error square.

### Hint

Find predicted  first.

### Short Explanation

Prediction: . Actual: 10. Difference: 1. Squared: 1.

### Detailed Explanation

1. **Prediction ():** .
2. **Actual ():** .
3. **Residual:** .
4. **Squared Residual:** .

---

## Q4

### Title

Visual Diagnostics

### Problem Description

Identify signs of poor fitting.

### Objective

Interpret residual patterns.

### Hint

Randomness is good. Patterns are bad.

### Short Explanation

A and D are bad signs. B and C are characteristics of a good/valid linear regression.

### Detailed Explanation

* **A (Bad):** A U-shape means the data is curved (parabola), but you fitted a straight line.
* **B (Good):** Random noise means the model captured the signal.
* **C (Good):** The best fit line always passes through the centroid .
* **D (Bad):** Outliers can drag the line away from the main cluster.

---

## Q5

### Title

Visualizing RSS

### Problem Description

Draw squares representing error.

### Objective

Visualizing the "Least Squares" concept.

### Hint

Use `matplotlib.patches.Rectangle`.

### Short Explanation

Advanced plotting task.

### Detailed Explanation

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

x = [1, 2, 4]; y = [1, 3, 3]
line_y = [1, 2, 4] # y=x

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(x, line_y)

for i in range(3):
    resid = y[i] - line_y[i]
    # Draw a square of size resid * resid
    rect = patches.Rectangle((x[i], line_y[i]), resid, resid, alpha=0.3, color='red')
    ax.add_patch(rect)
    
plt.axis('equal')
plt.show()

```

---

## Q6

### Title

Vertical vs Perpendicular

### Problem Description

Why minimize Vertical distance?

### Objective

Conceptual depth of OLS (Ordinary Least Squares).

### Hint

Are we predicting X or Y?

### Short Explanation

We are predicting  given . The error is "how wrong was our prediction of ?".

* **Vertical Distance:** Measures error in  only. This assumes  is known precisely.
* **Perpendicular Distance:** Measures error in both  and . This is used in **Total Least Squares** or PCA, not standard Regression.
* Since our goal is to get the best , we minimize the vertical error.

```

```
