# Moving Lines - Adjusting Slope and Intercept

## Learning Objectives
- Understand how changing slope affects the line
- Understand how changing intercept affects the line
- Learn to adjust lines toward data points
- Apply adjustment rules

## How Lines Move

A line is defined by: **y = mx + b**

Changing **m** (slope) or **b** (intercept) moves the line!

## Adjusting the Slope (m)

### Increasing Slope

```
Y          Y          Y
│  /       │    /     │      /
│ /        │   /      │     /
│/         │  /       │    /
└──X       └──X       └──X

m=0.5      m=1        m=2
```

**Effect:** Line rotates counterclockwise (gets steeper)

### Decreasing Slope

```
Y          Y          Y
│    \     │  \       ││     \    │   \      │ │      \   │    \     │  └──X       └──X       └──X

m=2        m=1        m=0.5
```

**Effect:** Line rotates clockwise (gets flatter)

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%205.png)

### Example: Adjusting for a Point Above the Line

```
Y
│     ● (3, 50) ← Point above line
│    /
│   / y = 10x + 5 (current line)
│  /
│ /
└────────X
```

**Point:** (3, 50)  
**Current prediction:** y = 10(3) + 5 = 35  
**Actual:** 50  
**Error:** 50 - 35 = 15 (too low!)

**Fix:** Increase slope!

```python
# New line with higher slope
y = 12x + 5  # Increased from 10 to 12

# New prediction for (3, ?)
y = 12(3) + 5 = 41  # Closer to 50!
```

## Adjusting the Y-Intercept (b)

### Increasing Intercept

```
Y
│  _____ b=3
│ _____ b=2
│_____ b=1
└──────X
```

**Effect:** Line moves UP (parallel shift)

### Decreasing Intercept

```
Y
│_____ b=1
│ _____ b=0
│  _____ b=-1
└──────X
```

**Effect:** Line moves DOWN (parallel shift)

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%206.png)

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%207.png)

### Example: Adjusting for a Point Above the Line

```
Y
│     ● (3, 50) ← Point above line
│    /
│   / y = 10x + 10 (current line)
│  /
│ /
└────────X
```

**Current prediction:** y = 10(3) + 10 = 40  
**Actual:** 50  
**Error:** 50 - 40 = 10 (too low!)

**Fix:** Increase intercept!

```python
# New line with higher intercept
y = 10x + 15  # Increased from 10 to 15

# New prediction
y = 10(3) + 15 = 45  # Closer to 50!
```

## Moving Line Toward a Point

### Point Above Line

```
Y
│     ● Target point
│    /│ ← Need to move UP
│   / ● Current line prediction
│  /
└────────X
```

**Actions:**
- Increase slope (rotate counterclockwise) OR
- Increase intercept (shift up) OR
- Both!

### Point Below Line

```
Y
│   / ● Current line prediction
│  /│ ← Need to move DOWN
│ /  ● Target point
└────────X
```

**Actions:**
- Decrease slope (rotate clockwise) OR
- Decrease intercept (shift down) OR
- Both!

## The Four Quadrants Rule

Given point position relative to line:

```
        Above │ Above
        Left  │ Right
    ──────────┼──────────
        Below │ Below
        Left  │ Right
```

### Quadrant 1: Above-Right (x > avg, y > predicted)

```
Y
│           ●
│         /
│       /
│     /
└────────X
```
**Adjustment:** Increase slope

### Quadrant 2: Above-Left (x < avg, y > predicted)

```
Y
│   ●
│     │       │         └────────X
```
**Adjustment:** Increase intercept

### Quadrant 3: Below-Left (x < avg, y < predicted)

```
Y
│         /
│       /
│     /
│   ●
└────────X
```
**Adjustment:** Decrease intercept

### Quadrant 4: Below-Right (x > avg, y < predicted)

```
Y
│       /
│     /
│   /
│           ●
└────────X
```
**Adjustment:** Decrease slope

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%208.png)

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%209.png)

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%2010.png)

## Step-by-Step Adjustment Example

### Initial Setup:

```python
# Current line
y = 5x + 10

# Data point
x = 4, y_actual = 50

# Prediction
y_predicted = 5(4) + 10 = 30

# Error
error = 50 - 30 = 20 (too low!)
```

### Adjustment Strategy:

**Step 1: Adjust Slope**
```python
# Increase slope by small amount
new_slope = 5 + 1 = 6
y = 6x + 10

# New prediction
y = 6(4) + 10 = 34  # Better! (was 30)
```

**Step 2: Adjust Intercept**
```python
# Also increase intercept
new_intercept = 10 + 5 = 15
y = 6x + 15

# New prediction
y = 6(4) + 15 = 39  # Even better! (was 34)
```

**Step 3: Continue Adjusting**
```python
# Keep iterating until close enough
# Final: y = 8x + 18
y = 8(4) + 18 = 50  # Perfect!
```

## Adjustment Amounts

### Small Adjustments

```python
# Gentle changes
slope_new = slope_old + 0.01
intercept_new = intercept_old + 0.1
```

**Pros:** Stable, precise  
**Cons:** Slow to converge

### Large Adjustments

```python
# Aggressive changes
slope_new = slope_old + 1.0
intercept_new = intercept_old + 10
```

**Pros:** Fast convergence  
**Cons:** May overshoot, unstable

### The Right Balance

Use **learning rate** (η) to control adjustment size:

```python
# η (eta) = learning rate (small number like 0.01)
slope_new = slope_old + η × adjustment
intercept_new = intercept_old + η × adjustment
```

## Real Example: House Prices

### Iteration 1:

```python
# Line: price = 50 × sqft + 100k
# Point: (2000 sqft, $400k)
predicted = 50 × 2000 + 100k = $200k
error = 400k - 200k = $200k (way off!)

# Adjust slope: 50 → 80
# Adjust intercept: 100k → 150k
```

### Iteration 2:

```python
# Line: price = 80 × sqft + 150k
# Point: (2000 sqft, $400k)
predicted = 80 × 2000 + 150k = $310k
error = 400k - 310k = $90k (better!)

# Adjust slope: 80 → 90
# Adjust intercept: 150k → 180k
```

### Iteration 10:

```python
# Line: price = 100 × sqft + 200k
# Point: (2000 sqft, $400k)
predicted = 100 × 2000 + 200k = $400k
error = 400k - 400k = $0 (perfect!)
```

## Summary

**Adjusting Slope:**
- Increase slope → Line rotates counterclockwise (steeper)
- Decrease slope → Line rotates clockwise (flatter)
- Use when: Points systematically above/below at certain x values

**Adjusting Intercept:**
- Increase intercept → Line shifts UP
- Decrease intercept → Line shifts DOWN
- Use when: All points consistently above/below line

**Adjustment Rules:**
- Point above line → Increase slope/intercept
- Point below line → Decrease slope/intercept
- Adjust by small amounts for stability

**Process:**
1. Calculate prediction error
2. Determine adjustment direction
3. Update slope and/or intercept
4. Repeat until error minimized

**Next:** We'll learn about learning rate - controlling adjustment size!

## Practice

1. Current line: y = 3x + 5. Point (2, 20) is above. Should you increase or decrease:
   - Slope?
   - Intercept?

2. If line is y = 10x + 50, and you increase intercept to 60, draw the change

3. Point (5, 30). Line predicts 25. What's the error? Adjust line toward point.

4. Describe what happens when you:
   - Increase slope from 2 to 4
   - Decrease intercept from 10 to 5

5. Given y = 2x + 3, adjust for point (3, 15)
