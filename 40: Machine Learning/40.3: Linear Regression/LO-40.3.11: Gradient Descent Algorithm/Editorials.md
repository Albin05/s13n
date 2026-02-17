
# Editorials

## Q1
### Title
Convexity of Linear Regression

### Problem Description
Identify the shape of the Linear Regression cost function.

### Objective
Understand convergence guarantees.

### Hint
The error is squared ($e^2$). What shape is a parabola?

### Short Explanation
The Mean Squared Error function is a convex (bowl-shaped) function. This means it has only one minimum (the Global Minimum), so Gradient Descent is guaranteed to find it (given a proper learning rate).

### Detailed Explanation
* **Convex:** Has a single minimum. Like a bowl.
* **Non-Convex:** Has hills and valleys. Like a mountain range.
* Linear Regression uses MSE, which is purely quadratic ($w^2$), making it **Convex**.

---

## Q2
### Title
Single Step Implementation

### Problem Description
Calculate new weight given parameters.

### Objective
Implement the core update formula.

### Hint
$w = w - (\text{lr} \times \text{grad})$.

### Short Explanation
$10 - (0.1 \times 2) = 10 - 0.2 = 9.8$.

### Detailed Explanation
```python
def update_weight(w, gradient, learning_rate):
    return w - (learning_rate * gradient)

```

---

## Q3

### Title

Manual Calculation

### Problem Description

One step of GD on .
.

### Objective

Verify arithmetic understanding of the update rule.

### Hint

Step size = Gradient  Learning Rate.

### Short Explanation

Step = . New .

### Detailed Explanation

1. **Calculate Step:** .
2. **Update:** .
3. *Note:* Since the target is  (min of ), moving from 5 to 3 is the correct direction (downhill).

---

## Q4

### Title

Speeding Up Convergence

### Problem Description

Select methods to fix slow training.

### Objective

Understand hyperparameters and preprocessing.

### Hint

If you are taking tiny steps on a flat surface, what helps?

### Short Explanation

A, B, and D are valid. C (Decreasing LR) would make it even slower.

### Detailed Explanation

* **A (True):** Larger steps = faster movement (risk of overshooting).
* **B (True):** Feature Scaling makes the cost function spherical, allowing faster direct convergence.
* **C (False):** Smaller steps = slower.
* **D (True):** SGD updates more frequently than Batch, often leading to faster initial convergence.

---

## Q5

### Title

Training Loop Simulation

### Problem Description

Simulate convergence to .

### Objective

Code a full optimization loop.

### Hint

Loop 100 times, apply update rule.

### Short Explanation

Standard loop implementation.

### Detailed Explanation

```python
w = 0
lr = 0.1
for _ in range(100):
    gradient = w - 5
    w = w - (lr * gradient)
print(w) # Should be very close to 5

```

---

## Q6

### Title

Batch vs Stochastic

### Problem Description

Compare GD variants.

### Objective

Trade-offs between speed and stability.

### Hint

Batch = Careful but slow. SGD = Drunk but fast.

### Short Explanation

1. **Computation:** Batch calculates gradient on *all* N samples (High cost per step). SGD uses *1* sample (Low cost per step).
2. **Stability:** Batch moves smoothly and directly downhill. SGD moves noisily, zig-zagging towards the minimum, but eventually hovers around it.

```

```
