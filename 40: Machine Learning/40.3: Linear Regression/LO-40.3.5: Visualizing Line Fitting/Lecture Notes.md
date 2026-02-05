# Visualizing Line Fitting

## Learning Objectives
- Understand what "fitting a line" means
- Visualize how lines fit data points
- Recognize good vs poor fits
- Interpret residuals visually

## What is Line Fitting?

**Line Fitting:** Finding the best straight line that represents the pattern in data points.

**Goal:** Draw a line that passes as close to all points as possible.

## The House Price Example

### The Data:

```python
sqft:  [1000, 2000, 3000, 4000, 5000, 6000, 7000]
price: [300k, 400k, 500k, 600k, 700k, 800k, 900k]
```

### Plotting the Points:

```
Price ($k)
900 │                              ●
800 │                         ●
700 │                    ●
600 │               ●
500 │          ●
400 │     ●
300 │ ●
    └─────────────────────────────────
    0    1k   2k   3k   4k   5k   6k   7k  sqft
```

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled.png)

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%201.png)

### Now Fit a Line:

```
Price ($k)
900 │                              ●
800 │                         ●  /
700 │                    ●  /
600 │               ●  /
500 │          ●  /
400 │     ●  /
300 │ ●  /
    └─────────────────────────────────
```

**The line equation:** price = 100 × sqft + 200,000

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%202.png)

## Good Fit vs Poor Fit

### Example of Good Fit:

```
Y
│     ●
│   ● │ ●
│ ●  line  ●
● ___│_____ ●
  │   ●   │
  Points close to line!
```

**Characteristics:**
- Points cluster around line
- Small distances from line to points
- Line captures the trend

### Example of Poor Fit:

```
Y
│ ●
│         ●
│ ●           ● 
│_______________ line
│     ●
│ ●       ●
  Points far from line!
```

**Characteristics:**
- Points scattered
- Large distances from line
- Line misses the pattern

## Residuals: Measuring Fit Quality

**Residual:** Distance from a point to the line (vertical distance)

```
Y
│     ● actual
│     │ ← residual (error)
│     │
│     ◆ predicted (on line)
│    /
│   /
│  /line
└────────────X
```

**Formula:** Residual = Actual Y - Predicted Y

### Example Calculation:

```python
# Point: (2000 sqft, $450k actual)
# Line: price = 100 × sqft + 200k

predicted = 100 × 2000 + 200000 = $400k
actual = $450k

residual = 450k - 400k = $50k
# Point is $50k ABOVE the line
```

## The Goal of Fitting

**Find the line where:**
- Sum of all residuals is minimized
- Line passes as close to all points as possible
- Best represents the overall pattern

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%203.png)

## Different Possible Lines

For the same data, we could draw many lines:

### Line 1: Too Steep

```python
price = 150 × sqft + 100k

Price ($k)
│                           ●
│                      ●  /
│                 ●  /
│            ●  /
│       ●  /  ← Line too steep!
│  ●  /
│ /
```
**Problem:** Underestimates low prices, overestimates high prices

### Line 2: Too Flat

```python
price = 50 × sqft + 400k

Price ($k)
│     ●
│     ●     ●
│____________ ← Line too flat!
│ ●   ●
│ ●       ●
```
**Problem:** Doesn't capture the upward trend

### Line 3: Just Right

```python
price = 100 × sqft + 200k

Price ($k)
│                 ●
│             ●  /
│         ●  /
│     ●  /  ← Perfect fit!
│ ●  /
│ /
```
**Success:** Minimizes overall error

## The Machine Learning Process

### Step 1: Start with Random Line

```python
# Random guess
price = 50 × sqft + 500k
```

![Untitled](../../../../Machine%20Learning/Linear%20Regression/Untitled%204.png)

### Step 2: Calculate Errors

```python
For each point:
    error = actual - predicted
    
# Point 1: (1000, 300k)
predicted = 50 × 1000 + 500k = 550k
error = 300k - 550k = -250k  # Way off!
```

### Step 3: Adjust Line

```python
# Make line less steep
# Lower the intercept
# New line: price = 80 × sqft + 300k
```

### Step 4: Repeat

```python
# Calculate new errors
# Adjust again
# Keep iterating until errors minimized
```

### Final Result:

```python
# After many iterations
price = 100 × sqft + 200k  # Optimal line!
```

## Visual Example: Student Scores

### Data:

```python
study_hours = [2, 3, 4, 5, 6, 7, 8]
scores = [55, 62, 68, 75, 82, 88, 93]
```

### Initial Random Line:

```
Score
100│
   │         ●
 80│       ●
   │     ●       Line too low!
 60│   ●  /
   │ ● /
 40│ /
   └────────────
     2  4  6  8  hours
```

### After Adjustment:

```
Score
100│               ●
   │           ●  /
 80│       ●  /
   │     ●  /  ← Better fit!
 60│   ●  /
   │ ●  /
 40│ /
   └────────────
     2  4  6  8  hours
```

### Final Fitted Line:

```
Score
100│               ●
   │           ●
 80│       ●  
   │     ●  All points close to line!
 60│   ●  
   │ ●  
 40│
   └────────────
     2  4  6  8  hours

score = 6 × hours + 43
```

## Multiple Data Scenarios

### Scenario 1: Perfect Linear Data

```
Y
│     ●
│   ● 
│ ●
●
```
**Easy!** Line passes through all points perfectly.

### Scenario 2: Noisy Data

```
Y
│   ● ●
│ ●  ●  ●
● ●   ●
```
**Challenging!** Line must approximate, can't hit all points.

### Scenario 3: Non-Linear Data

```
Y
│       ●
│     ●  ●
│   ●      ●
│ ●
●
```
**Problem!** Straight line can't capture curve. Need polynomial regression.

## Interpreting the Fitted Line

Once we have the best line, we can:

### 1. Make Predictions

```python
# Line: price = 100 × sqft + 200k
# Predict for 3500 sqft:
price = 100 × 3500 + 200k = $550k
```

### 2. Understand Relationships

```python
# Slope = 100
# Meaning: Each sqft adds $100 to price
```

### 3. Check Fit Quality

```python
# If most points close to line → Good fit
# If points scattered → Poor fit
```

## Summary

**Line Fitting:**
- Finding best line through data points
- Goal: Minimize distances from points to line
- Visual representation of the model

**Key Concepts:**
- Residuals = distances from points to line
- Good fit = small residuals
- Poor fit = large residuals

**Process:**
1. Plot data points
2. Try different lines
3. Calculate errors
4. Choose line with smallest errors

**Visual Indicators of Good Fit:**
- Points cluster around line
- No systematic pattern in residuals
- Line captures overall trend

**Next:** We'll learn how to adjust lines mathematically!

## Practice

1. Draw residuals for 3 points given a line

2. Which line fits better? Why?
   - Line A: Half points above, half below
   - Line B: All points above line

3. If actual = $300k and predicted = $350k, what's the residual?

4. What does it mean if residuals are all positive?

5. Sketch: data points and a line that fits poorly
