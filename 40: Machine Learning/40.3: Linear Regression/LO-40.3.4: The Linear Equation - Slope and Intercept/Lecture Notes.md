# The Linear Equation - Slope and Intercept

## Learning Objectives
- Understand the linear equation y = mx + b
- Master the concepts of slope and intercept
- Calculate slope and intercept from data
- Interpret slope and intercept in context

## The Linear Equation

**The Formula:** y = mx + b

Where:
- **y** = output (predicted value)
- **x** = input (feature)
- **m** = slope (rate of change)
- **b** = y-intercept (starting value)

This simple formula describes ANY straight line!

## Understanding Slope (m)

**Slope:** How much y changes when x increases by 1

Think of it as:
- Rate of change
- Steepness of line
- "Rise over run"

### Formula:
```
slope (m) = (y2 - y1) / (x2 - x1)
slope = rise / run
slope = change in y / change in x
```

### Example: Hourly Pay

```python
# Data
hours:  1   2   3   4
pay:    10  20  30  40

# Calculate slope
m = (20 - 10) / (2 - 1) = 10/1 = 10

# Meaning: $10 per hour!
```

**Equation:** pay = 10 × hours + 0

### Positive vs Negative Slope

**Positive Slope (m > 0):**
```
Y
│    /
│  /
│/
└────────X

# As X increases, Y increases
# Example: More study hours → Higher score
```

**Negative Slope (m < 0):**
```
Y
││  │    └────────X

# As X increases, Y decreases
# Example: More age → Lower reaction time
```

**Zero Slope (m = 0):**
```
Y
│────────
│
│
└────────X

# Y doesn't change with X
# Horizontal line
```

## Understanding Y-Intercept (b)

**Y-Intercept:** The value of y when x = 0

Think of it as:
- Starting point
- Base value
- Where line crosses Y-axis

### Example: Taxi Fare

```python
# Taxi: $5 base + $2 per mile
fare = 2 × miles + 5

# When miles = 0:
fare = 2 × 0 + 5 = $5

# The intercept is $5 (base fare)
```

### Visual:

```
Fare ($)
15 │         ●
13 │       ●
11 │     ●
 9 │   ●
 7 │ ●
 5 ●  ← Y-intercept = 5
   └──────────────
   0  1  2  3  4  5  Miles
```

Point at (0, 5) is the y-intercept!

## Complete Examples

### Example 1: House Prices

**Data:**
```python
sqft:  1000  1500  2000  2500
price: 250k  325k  400k  475k
```

**Calculate Slope:**
```python
m = (325k - 250k) / (1500 - 1000)
m = 75k / 500
m = $150 per sqft
```

**Calculate Intercept:**
```python
Using point (1000, 250k):
250k = 150 × 1000 + b
250k = 150k + b
b = 100k
```

**Final Equation:**
```python
price = 150 × sqft + 100,000

# Interpretation:
# - Each sqft adds $150 (slope)
# - Base price is $100k (intercept)
```

### Example 2: Temperature Conversion

**Celsius to Fahrenheit:** F = 1.8C + 32

**Breaking it down:**
- **Slope (1.8):** Each 1°C = 1.8°F increase
- **Intercept (32):** 0°C = 32°F (freezing point)

**Examples:**
```python
C = 0:  F = 1.8(0) + 32 = 32°F
C = 10: F = 1.8(10) + 32 = 50°F
C = 100: F = 1.8(100) + 32 = 212°F (boiling)
```

### Example 3: Salary Prediction

**Data Analyst Salaries:**

```python
# years_experience vs salary
experience: [0, 1, 2, 3, 4, 5]
salary:     [50k, 53k, 56k, 59k, 62k, 65k]

# Calculate slope
m = (53k - 50k) / (1 - 0) = 3k per year

# Calculate intercept (at experience = 0)
b = 50k

# Equation
salary = 3000 × experience + 50000
```

**Interpretation:**
- **Slope ($3k):** Each year adds $3k to salary
- **Intercept ($50k):** Starting salary with 0 experience

## Calculating from Two Points

Given any two points, you can find the equation!

**Formula:**
```
1. Calculate slope: m = (y2 - y1) / (x2 - x1)
2. Use point-slope form: y - y1 = m(x - x1)
3. Solve for y: y = mx + b
```

**Example:**

Points: (2, 30) and (5, 45)

**Step 1: Slope**
```
m = (45 - 30) / (5 - 2)
m = 15 / 3
m = 5
```

**Step 2: Find b using one point**
```
Using (2, 30):
30 = 5(2) + b
30 = 10 + b
b = 20
```

**Step 3: Final Equation**
```
y = 5x + 20
```

**Verify with other point (5, 45):**
```
y = 5(5) + 20 = 25 + 20 = 45 ✓
```

## Multiple Variables (Preview)

Linear regression extends to multiple inputs:

```python
# One variable
price = m × sqft + b

# Multiple variables
price = m1 × sqft + m2 × bedrooms + m3 × age + b

# Still linear!
# Each variable has its own slope (coefficient)
```

**Example:**
```python
price = 150 × sqft + 50000 × bedrooms - 5000 × age + 100000

# Interpretation:
# - Each sqft adds $150
# - Each bedroom adds $50k
# - Each year of age subtracts $5k
# - Base price is $100k
```

## Interpreting Slope and Intercept

### Slope Interpretation:

**Template:** "For each unit increase in [x], [y] changes by [m]"

**Examples:**
```python
y = 10x + 5
# "For each unit increase in x, y increases by 10"

salary = 3000 × experience + 50000
# "For each year of experience, salary increases by $3,000"

temperature_F = 1.8 × temperature_C + 32
# "For each 1°C increase, Fahrenheit increases by 1.8°F"
```

### Intercept Interpretation:

**Template:** "When [x] is zero, [y] is [b]"

**Examples:**
```python
y = 10x + 5
# "When x is 0, y is 5"

fare = 2 × miles + 5
# "When miles is 0, fare is $5 (base fare)"

salary = 3000 × experience + 50000
# "With 0 years experience, salary is $50,000"
```

## Special Cases

### Case 1: Intercept = 0

```python
y = mx + 0  or simply  y = mx

# Line passes through origin (0, 0)
# Example: distance = speed × time (starting at 0)
```

### Case 2: Slope = 0

```python
y = 0 × x + b  or simply  y = b

# Horizontal line
# y doesn't depend on x
# Example: Flat tax rate regardless of income bracket
```

### Case 3: Vertical Line

```python
x = constant

# Cannot be written as y = mx + b
# Undefined slope (division by zero)
# Not a function!
```

## Summary

**Linear Equation:** y = mx + b

**Slope (m):**
- Rate of change
- How much y changes per unit x
- Steepness of line
- rise / run

**Intercept (b):**
- Starting value
- y when x = 0
- Where line crosses y-axis

**Calculating:**
- Slope: m = (y2 - y1) / (x2 - x1)
- Intercept: Solve b = y - mx using any point

**Interpretation:**
- Slope: "Each unit of x changes y by m"
- Intercept: "When x = 0, y = b"

**Next:** We'll learn how machines find the best m and b for data!

## Practice

1. Given y = 5x + 10:
   - What's the slope?
   - What's the intercept?
   - What's y when x = 3?

2. Find equation given points (1, 8) and (3, 14)

3. Interpret: price = 200 × sqft + 50000
   - What's the meaning of 200?
   - What's the meaning of 50000?

4. Calculate slope:
```
x: 2, 4, 6, 8
y: 10, 20, 30, 40
```

5. A line passes through (0, 5) with slope 3. What's the equation?
