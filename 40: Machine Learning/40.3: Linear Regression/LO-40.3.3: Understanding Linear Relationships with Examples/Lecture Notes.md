# Understanding Linear Relationships with Examples

## Learning Objectives
- Understand what a linear relationship is
- Recognize linear patterns in data
- Interpret linear relationships
- Apply linear thinking to real problems

## What is a Linear Relationship?

**Linear Relationship:** When one variable changes, the other changes by a **constant amount**.

**Key characteristic:** Forms a STRAIGHT LINE when graphed.

### Simple Example:

```
Hours worked | Money earned
-------------|-------------
1            | $10
2            | $20
3            | $30
4            | $40
```

**Pattern:** Each hour adds exactly $10!
**Graph:** Straight line!

## Characteristics of Linear Relationships

### 1. Constant Rate of Change

```python
# For every +1 in X, +constant in Y
x: 1, 2, 3, 4, 5
y: 10, 20, 30, 40, 50

# Change in Y per change in X = constant = 10
```

### 2. Straight Line Graph

When you plot points, they form (or approximate) a straight line:

```
Y
│     ●
│   ●
│ ●
● 
└───────────X
```

### 3. Predictable Pattern

Once you know the rate, you can predict any value:

```python
If pattern is +10 per hour:
7 hours → $70
10 hours → $100
25 hours → $250
```

## Real-World Linear Relationships

### Example 1: Taxi Fare

**Scenario:** Taxi charges $5 base + $2 per mile

```python
miles = [0, 1, 2, 3, 4, 5]
fare = [5, 7, 9, 11, 13, 15]

# Fare = 5 + 2 × miles
# Linear relationship!
```

**Graph:**
```
Fare ($)
15 │         ●
13 │       ●
11 │     ●
 9 │   ●
 7 │ ●
 5 ● 
   └──────────────
   0  1  2  3  4  5  Miles
```

Straight line! Linear relationship confirmed.

### Example 2: Temperature Conversion

**Celsius to Fahrenheit:** F = (9/5)C + 32

```python
celsius = [0, 10, 20, 30, 40]
fahrenheit = [32, 50, 68, 86, 104]

# Each 10°C increase = 18°F increase
# Linear!
```

### Example 3: Savings Account

**Scenario:** Start with $1000, save $200/month

```python
months = [0, 1, 2, 3, 4, 5]
savings = [1000, 1200, 1400, 1600, 1800, 2000]

# Savings = 1000 + 200 × months
# Perfect linear relationship!
```

## Non-Linear Relationships

Not all relationships are linear! Understanding the difference is crucial.

### Example: Area of Square

```python
side = [1, 2, 3, 4, 5]
area = [1, 4, 9, 16, 25]  # side²

# As side increases by 1:
# Area increases by 3, then 5, then 7, then 9
# NOT constant! NOT linear!
```

**Graph:** Curves upward (parabola)

### Example: Compound Interest

```python
years = [0, 1, 2, 3, 4]
amount = [1000, 1100, 1210, 1331, 1464]  # 10% annually

# Growth accelerates!
# NOT linear - exponential!
```

## Identifying Linear Relationships

### Test 1: Equal Spacing

```python
# Linear
x:  1    2    3    4    5
y:  10   20   30   40   50
    +10  +10  +10  +10  ← Equal steps!

# Non-linear
x:  1    2    3    4    5
y:  1    4    9    16   25
    +3   +5   +7   +9   ← Unequal steps!
```

### Test 2: Plot It

- Linear → Straight line
- Non-linear → Curved line

### Test 3: Calculate Rate

```python
# Linear: rate is constant
rate = (y2 - y1) / (x2 - x1) = constant

# Example:
(20-10)/(2-1) = 10
(30-20)/(3-2) = 10
(40-30)/(4-3) = 10  ← All same!
```

## House Price Example

**Question:** Is house price linear with square feet?

### The Data:

```python
sqft =  [1000, 1500, 2000, 2500, 3000]
price = [200k, 300k, 400k, 500k, 600k]

# Each 500 sqft adds $100k
# Linear relationship!
```

### Why Linear?

```
Price per sqft = constant = $200/sqft

1000 sqft × $200 = $200k ✓
1500 sqft × $200 = $300k ✓
2000 sqft × $200 = $400k ✓
```

**This is a linear model:** Price = $200 × sqft

## More Complex Example: Multiple Factors

### House Price with More Features:

```python
Price = (150 × sqft) + (50000 × bedrooms) + 100000

# Still linear!
# Each feature contributes proportionally
```

**Example Calculation:**
```python
sqft = 2000
bedrooms = 3

Price = (150 × 2000) + (50000 × 3) + 100000
Price = 300000 + 150000 + 100000
Price = $550,000
```

Even with multiple features, it's linear if each contributes by a **constant coefficient**.

## Approximate Linear Relationships

Real-world data is rarely perfectly linear!

### Example: Student Score vs Study Hours

```python
study_hours = [2, 4, 6, 8, 10]
actual_score = [55, 68, 79, 85, 91]

# Not perfectly linear, but close!
# We can approximate with a line
```

**The line:** Score ≈ 5 × hours + 45

```python
predicted = [55, 65, 75, 85, 95]  # Perfect line
actual = [55, 68, 79, 85, 91]      # Real data
# Close enough!
```

## Why Linear Relationships Matter for ML

### 1. Simplicity

```python
# Easy to understand
y = mx + b

# Easy to compute
prediction = slope × input + intercept
```

### 2. Interpretability

```python
# Clear meaning
"Each additional bedroom adds $50,000 to house price"
"Each extra study hour adds 5 points to score"
```

### 3. Computational Efficiency

```python
# Fast to calculate
# No complex operations
# Scales well to big data
```

### 4. Good Baseline

Even if relationship isn't perfectly linear:
- Linear model gives reasonable approximation
- Start simple, add complexity if needed

## Summary

**Linear Relationship:**
- Constant rate of change
- Straight line when graphed
- Predictable pattern
- y = mx + b form

**Examples:**
- Taxi fare vs distance
- Temperature conversion
- Savings over time
- House price vs size (approximately)

**Identifying Linear:**
1. Check if rate of change is constant
2. Plot data - should form straight line
3. Calculate slopes between points - should be equal

**Why It Matters:**
- Foundation of linear regression
- Simple and interpretable
- Computationally efficient
- Good starting point for any prediction problem

**Next:** We'll learn the mathematical formula for these lines!

## Practice

1. Identify if linear or non-linear:
   - Cost = $5 + $3 per item
   - Area = side²
   - Distance = speed × time
   - Population = initial × 1.05^years

2. Given:
```
hours: 2, 4, 6, 8
pay: $20, $40, $60, $80
```
Is this linear? If yes, what's the rate?

3. Create a real-world example of a linear relationship

4. Why isn't compound interest a linear relationship?

5. For each 100 sqft, house price increases $15k. What's the total increase for 500 sqft?
