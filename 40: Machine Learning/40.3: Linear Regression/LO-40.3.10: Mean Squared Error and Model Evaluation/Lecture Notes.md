# Introduction to Regression Problems

## Learning Objectives
- Understand what regression problems are
- Distinguish regression from other ML problems
- Recognize real-world regression applications
- Identify when to use regression

## What is a Regression Problem?

**Regression:** Predicting a **continuous numerical value** based on input features.

**Key characteristic:** The output is a NUMBER on a continuous scale.

### Examples:

```python
# Regression problems (predicting numbers)
house_price = 350000        # Dollars
temperature = 72.5          # Degrees  
stock_price = 150.25        # Dollars
student_score = 85.5        # Points
sales_revenue = 125000      # Dollars
delivery_time = 45.3        # Minutes
```

## Regression vs Other Problems

| Problem Type | Output | Example |
|--------------|--------|---------|
| **Regression** | Continuous number | House price: $350,000 |
| **Classification** | Category/Class | Email: Spam or Ham |
| **Clustering** | Group assignment | Customer segment: A, B, or C |

## Real-World Regression Problems

### 1. House Price Prediction

**Input Features:**
```python
features = {
    'square_feet': 2000,
    'bedrooms': 3,
    'bathrooms': 2,
    'age_years': 10,
    'location_score': 8.5
}
```

**Output:**
```python
predicted_price = $350,000  # Continuous number!
```

**Why regression?** Price can be any value ($300k, $350k, $425k, etc.)

### 2. Temperature Forecasting

**Input Features:**
```python
features = {
    'time_of_day': 14,        # 2 PM
    'season': 'Summer',
    'humidity': 65,
    'cloud_cover': 30,
    'historical_avg': 75
}
```

**Output:**
```python
predicted_temp = 78.5°F     # Can be any temperature!
```

### 3. Student Score Prediction

**Input Features:**
```python
features = {
    'study_hours': 6,
    'attendance_%': 85,
    'previous_score': 78,
    'assignment_completion': 90
}
```

**Output:**
```python
predicted_score = 82.3      # Any score from 0-100
```

### 4. Sales Forecasting

**Input Features:**
```python
features = {
    'advertising_spend': 10000,
    'season': 'Holiday',
    'competitor_price': 25,
    'website_traffic': 50000
}
```

**Output:**
```python
predicted_sales = $125,000  # Revenue amount
```

## The Classic Example: Hours Worked vs Money Earned

**Scenario:** You work and get paid hourly.

### The Data:

| Hours Worked | Money Earned |
|--------------|--------------|
| 5 | $50 |
| 10 | $100 |
| 15 | $150 |
| 20 | ? |
| 25 | ? |

**Question:** How much for 20 hours? 25 hours?

**Pattern:** $10 per hour!

**Predictions:**
- 20 hours → $200
- 25 hours → $250

This is a **REGRESSION** problem!

![](https://images.unsplash.com/photo-1543269865-cbf427effbad?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb)

## Why "Regression"?

The term comes from "regression to the mean" in statistics.

**Simple meaning:** Finding a relationship between variables to predict continuous outputs.

## Characteristics of Regression Problems

### 1. Continuous Output
```python
# Can take infinite values in a range
price = 350000.00
price = 350000.50
price = 350000.75
# Any value possible!
```

### 2. Numerical Scale
```python
# Has magnitude and order
100 < 200 < 300
Differences meaningful: 200 - 100 = 100
```

### 3. Interpolation & Extrapolation
```python
# Can predict between known points (interpolation)
Known: 5hrs=$50, 10hrs=$100
Predict: 7hrs=$70 ✓

# Can predict beyond known range (extrapolation)
Known: up to 10hrs
Predict: 15hrs=$150 ✓
```

## When to Use Regression

### ✓ Use Regression When:

1. **Predicting quantities:**
   - How much?
   - What amount?
   - What value?

2. **Continuous output:**
   - Not just a few options
   - Many possible values

3. **Numerical relationships:**
   - Clear input→output pattern
   - Mathematical relationship

### Examples:
- Predicting house prices ✓
- Forecasting sales revenue ✓
- Estimating delivery time ✓
- Calculating loan amounts ✓

### ✗ Don't Use Regression When:

1. **Predicting categories:**
   - Is it spam? (Yes/No) → Classification
   - What type of animal? (Cat/Dog/Bird) → Classification

2. **Discrete options:**
   - Limited fixed choices → Classification

3. **Finding groups:**
   - Segment customers → Clustering

## Regression in Machine Learning Workflow

```
1. Collect Data
   Hours: [5, 10, 15]
   Money: [50, 100, 150]
   
2. Train Model (Linear Regression)
   Model learns: Money = 10 × Hours
   
3. Make Predictions
   Input: 20 hours
   Output: $200
```

## Types of Regression

While we focus on **Linear Regression**, there are other types:

**Linear Regression:** Straight line relationship
```
y = mx + b
Price = (coefficient × sqft) + base_price
```

**Polynomial Regression:** Curved relationship
```
y = ax² + bx + c
```

**Multiple Linear Regression:** Many inputs
```
Price = (c1 × sqft) + (c2 × bedrooms) + (c3 × age) + base
```

We'll focus on **simple linear regression** first!

## Summary

**Regression Problems:**
1. Predict continuous numerical values
2. Output can be any number in a range
3. Used for "how much?" questions
4. Examples: prices, temperatures, scores, revenues

**Key Points:**
- Regression = Predicting numbers
- Classification = Predicting categories
- Use when output is continuous
- Linear regression = straight line fit

**Next:** We'll learn how linear regression finds that line!

## Practice

1. Identify if regression or classification:
   - Predicting tomorrow's temperature
   - Detecting spam email
   - Estimating car value
   - Recognizing handwritten digits

2. Give 5 examples of regression problems from daily life

3. For house price prediction, what makes it a regression problem?

4. Can you use regression to predict if it will rain? Why or why not?

5. What's the key difference between predicting "house price" vs "house sold (yes/no)"?
