
# Editorials

## Q1
### Title
Rotation Direction

### Problem Description
Identify the change that flattens the line.

### Objective
Visualize slope magnitude.

### Hint
Higher slope = Steeper. Lower slope = Flatter.

### Short Explanation
Changing $m$ from 5 to 2 reduces the steepness, effectively rotating the line clockwise towards the horizontal axis.

### Detailed Explanation
* **A:** 2 to 5 makes it steeper (Counter-Clockwise).
* **B:** 5 to 2 makes it flatter (Clockwise).
* **C/D:** Changes to $c$ are vertical shifts, not rotations.

---

## Q2
### Title
Line Shifting Logic

### Problem Description
Adjust intercept to shift line.

### Objective
Implement translation logic.

### Hint
Only $c$ changes. $m$ stays the same.

### Short Explanation
New Intercept = Old Intercept + Shift.

### Detailed Explanation
```python
def shift_line(m, c, shift_amount):
    return m, c + shift_amount

```

---

## Q3

### Title

Slope Adjustment

### Problem Description

Change  to be parallel to .

### Objective

Understand parallel lines have equal slopes.

### Hint

Target slope is 5. Current is 3.

### Short Explanation

Target . Current . Change = .

### Detailed Explanation

Parallel lines share the same slope. We need to change our slope from 3 to 5. The difference is 2.

---

## Q4

### Title

Adjustment Effects

### Problem Description

Map parameter changes to geometric effects.

### Objective

Conceptual verification.

### Hint

Intercept is vertical, Slope is angular.

### Short Explanation

All statements (A, B, C, D) are correct descriptions of linear adjustments.

### Detailed Explanation

* **A/B:**  controls vertical offset.
* **C/D:**  controls steepness (rate of change).

---

## Q5

### Title

Pivot Simulation

### Problem Description

Rotate line around intercept.

### Objective

Visualize rotation fixed at .

### Hint

Intercept  remains 2. Slopes are 1 and 3.

### Short Explanation

Compare  vs .

### Detailed Explanation

```python
x = 5
c = 2
# Line 1
y1 = 1 * x + c  # 7
# Line 2
y2 = 3 * x + c  # 17
print(f"Y at x=5 changed from {y1} to {y2}")

```

---

## Q6

### Title

Seesaw Analogy

### Problem Description

Map seesaw physics to linear equation.

### Objective

Intuitive understanding of parameters.

### Hint

Fulcrum = Pivot point.

### Short Explanation

1. **Fulcrum Height:** The Intercept (). It determines the baseline height of the system.
2. **Plank Angle:** The Slope (). It determines the rate of rise/fall.
3. **Effect:** If you lift the fulcrum (increase Intercept) without changing the angle (constant Slope), both ends of the seesaw move up by exactly the same amount. This is a parallel shift.

```

```
