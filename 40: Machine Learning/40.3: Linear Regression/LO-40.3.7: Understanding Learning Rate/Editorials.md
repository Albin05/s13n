
# Editorials

## Q1
### Title
Interpreting Loss Curves

### Problem Description
Identify the ideal loss curve shape.

### Objective
Visual diagnostics of training.

### Hint
We want rapid learning initially, then fine-tuning.

### Short Explanation
**B (Hockey Stick):** Rapid descent means the model is learning the obvious patterns quickly. Flattening means it is fine-tuning the weights near the optimum.

### Detailed Explanation
* **A:** Not learning.
* **B:** Optimal.
* **C:** Diverging (LR too high).
* **D:** Unstable (LR too high).

---

## Q2
### Title
Step Calculation

### Problem Description
Calculate the delta for update.

### Objective
Basic implementation.

### Hint
Step = Gradient $\times$ Learning Rate.

### Short Explanation
$5.0 \times 0.1 = 0.5$.

### Detailed Explanation
```python
def calculate_step(gradient, lr):
    return gradient * lr

```

---

## Q3

### Title

Update Rule Calculation

### Problem Description

Apply .
.

### Objective

Arithmetic verification.

### Hint

Watch the signs! Minus a negative is a positive.

### Short Explanation

Step = .
New .

### Detailed Explanation

1. **Step Size:** .
2. **Update:** .
3. *Note:* The gradient was negative (slope down to the left), so we moved right (increased ), which is correct.

---

## Q4

### Title

LR Strategies

### Problem Description

Select valid methods for tuning LR.

### Objective

Advanced optimization concepts.

### Hint

We always want to minimize loss (go downhill), so C is wrong.

### Short Explanation

A, B, and D are standard practices. C moves uphill (maximization), which increases error.

### Detailed Explanation

* **A (Decay):** Helps converge precisely.
* **B (Grid Search):** Standard tuning method.
* **C (Negative):** Gradient Descent follows the negative gradient. Making LR negative would cancel this out and go uphill.
* **D (Adaptive):** Used in Adam/RMSProp.

---

## Q5

### Title

Simulating Divergence

### Problem Description

Show that `lr > 1.0` causes divergence on  starting at 10.

### Objective

Code simulation of failure.

### Hint

Gradient of  is .

### Short Explanation

.
Grad=. Step=. .
Grad=. Step=. .
Magnitude grows: .

### Detailed Explanation

```python
w = 10
lr = 1.1
for i in range(3):
    grad = 2 * w
    w = w - (lr * grad)
    print(w)
# Output: -12.0, 14.4, -17.28 (Oscillating and growing)

```

---

## Q6

### Title

Analogy of Decay

### Problem Description

Explain LR Decay using parking analogy.

### Objective

Intuitive understanding of scheduling.

### Hint

Do you park at 60mph?

### Short Explanation

* **Beginning (Highway):** You are far from the destination. You drive fast (Large LR) to cover distance quickly. Precision doesn't matter yet.
* **End (Parking Spot):** You are very close. If you keep driving at 60mph, you will crash or overshoot the spot. You must slow down (Small LR) to inch into the perfect position.
* **In ML:** Large LR explores the landscape quickly; Small LR settles into the minimum without bouncing out.

```

```
