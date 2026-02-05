# Introduction to Categorical Variables

## Learning Objectives
- Understand what categorical variables are
- Distinguish categorical from numerical variables
- Recognize different types of categorical data
- Understand why ML models can't directly use categories

## What Are Categorical Variables?

**Categorical Variable:** A variable that takes on values from a limited set of categories or groups.

Think of it as: **Labels** or **Names** rather than **Numbers**

### Examples:

```python
# Categorical variables
gender = 'Male' or 'Female' or 'Other'
color = 'Red' or 'Blue' or 'Green'
size = 'Small' or 'Medium' or 'Large'
country = 'USA' or 'India' or 'China' or ...
education = 'High School' or 'Bachelors' or 'Masters' or 'PhD'
```

These are **categories**, not numbers!

## Categorical vs Numerical Variables

### Numerical Variables
Variables that are **numbers** with mathematical meaning:

```python
age = 25                    # Can add, subtract
price = 350000              # Can calculate average
temperature = 72            # Can find difference
height = 175                # Can multiply
income = 50000              # Mathematical operations make sense
```

**Key:** Mathematical operations are meaningful!
- Average age = (25 + 30 + 35) / 3 = 30 ✓

### Categorical Variables
Variables that are **categories** or **labels**:

```python
color = 'Blue'              # Can't add colors!
city = 'Boston'             # Can't multiply cities!
car_brand = 'Toyota'        # Can't average brands!
blood_type = 'O+'           # Can't subtract types!
movie_genre = 'Action'      # Can't do math!
```

**Key:** Mathematical operations are meaningless!
- Average color = ('Red' + 'Blue' + 'Green') / 3 = ??? ✗

## Real-World Example: Employee Data

```python
employees = [
    {
        'name': 'John',                    # Categorical
        'age': 25,                         # Numerical
        'department': 'Sales',             # Categorical
        'salary': 50000,                   # Numerical
        'gender': 'Male',                  # Categorical
        'years_experience': 3,             # Numerical
        'education': 'Bachelors',          # Categorical
        'performance_score': 8.5           # Numerical
    },
    # ... more employees
]
```

**Categorical:** name, department, gender, education
**Numerical:** age, salary, years_experience, performance_score

## Types of Categorical Variables

### 1. Nominal Categories
Categories with **no inherent order**

```python
# Colors - no ranking
color = ['Red', 'Blue', 'Green', 'Yellow']
# Red is not "better" than Blue

# Cities - no order
city = ['Boston', 'Chicago', 'Austin', 'Seattle']
# Boston is not "higher" than Chicago

# Blood type - no hierarchy
blood_type = ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']

# Car brand - no ranking
brand = ['Toyota', 'Honda', 'Ford', 'BMW']
```

### 2. Ordinal Categories
Categories with **natural order** or ranking

```python
# Education level - clear order!
education = ['High School' < 'Bachelors' < 'Masters' < 'PhD']

# Size - ordered
size = ['Small' < 'Medium' < 'Large' < 'Extra Large']

# Rating - ranked
rating = ['Poor' < 'Fair' < 'Good' < 'Excellent']

# Grade - ordered
grade = ['F' < 'D' < 'C' < 'B' < 'A']

# Customer tier - hierarchy
tier = ['Bronze' < 'Silver' < 'Gold' < 'Platinum']
```

## The ML Problem with Categories

**Big Problem:** Most ML algorithms work with **NUMBERS**, not **CATEGORIES**!

### Example: Linear Regression

```python
# ML algorithm expects:
price = (coefficient1 × feature1) + (coefficient2 × feature2) + ...

# This works:
price = (150 × square_feet) + (50000 × bedrooms) + ...
# 150 × 2000 + 50000 × 3 = 450,000

# This DOESN'T work:
price = (coefficient × color) + ...
# coefficient × 'Blue' = ??? 
# Can't multiply by 'Blue'!
```

### Why Categories Don't Work:

1. **Can't do math:**
   ```python
   'Red' + 'Blue' = ???
   'Tokyo' × 2 = ???
   'PhD' - 'Masters' = ???
   ```

2. **No magnitude:**
   ```python
   Is 'Blue' > 'Red'? 
   Is 'Toyota' bigger than 'Honda'?
   Makes no sense!
   ```

3. **Algorithms need numbers:**
   ```python
   model.fit(X, y)
   # X must be numerical matrix
   # Can't have 'Male', 'Female' in X
   ```

## Example Problem: Predicting Income

### Dataset:

```python
data = [
    {'gender': 'Male', 'education': 'Bachelors', 'income': 50000},
    {'gender': 'Female', 'education': 'Masters', 'income': 70000},
    {'gender': 'Male', 'education': 'PhD', 'income': 90000},
    {'gender': 'Female', 'education': 'Bachelors', 'income': 55000}
]
```

### Can't directly use:
```python
# This won't work!
model.fit(
    X = [['Male', 'Bachelors'], ['Female', 'Masters'], ...],
    y = [50000, 70000, ...]
)
# Error: Can't compute with 'Male' and 'Bachelors'!
```

### Need to convert to numbers somehow!

**That's what we'll learn next!**

## Identifying Categorical Variables

### Quick Test:

Ask yourself:
1. Can I do meaningful math with this? 
   - YES → Numerical
   - NO → Categorical

2. Is it a label/name/category?
   - YES → Categorical
   - NO → Numerical

3. Does it have a fixed set of options?
   - YES → Probably categorical
   - NO → Probably numerical

### Practice Examples:

| Variable | Type | Why? |
|----------|------|------|
| temperature (°F) | Numerical | Can calculate average |
| country | Categorical | Can't do math with countries |
| price ($) | Numerical | Can add, multiply |
| t-shirt size | Categorical | S/M/L are labels |
| distance (miles) | Numerical | Can measure, compare |
| favorite color | Categorical | Colors are categories |
| number of children | Numerical | Count, can average |
| marital status | Categorical | Single/Married are labels |

## Categorical Variables in Real Applications

### E-Commerce:

```python
product_data = {
    'category': 'Electronics',        # Categorical
    'brand': 'Apple',                 # Categorical
    'price': 999,                     # Numerical
    'color': 'Space Gray',            # Categorical
    'size': 'Large',                  # Categorical (or Ordinal)
    'rating': 4.5,                    # Numerical
    'in_stock': True,                 # Categorical (Boolean)
    'shipping_method': 'Express'      # Categorical
}
```

### Healthcare:

```python
patient_data = {
    'blood_type': 'O+',               # Categorical
    'gender': 'Female',               # Categorical
    'age': 45,                        # Numerical
    'diagnosis': 'Diabetes',          # Categorical
    'severity': 'Moderate',           # Categorical (Ordinal)
    'blood_pressure': 120,            # Numerical
    'treatment': 'Medication',        # Categorical
    'smoker': 'Yes'                   # Categorical
}
```

### Banking:

```python
loan_data = {
    'loan_type': 'Home',              # Categorical
    'employment_status': 'Employed',  # Categorical
    'income': 75000,                  # Numerical
    'credit_score': 720,              # Numerical
    'education': 'Masters',           # Categorical (Ordinal)
    'marital_status': 'Married',      # Categorical
    'loan_amount': 250000,            # Numerical
    'loan_approved': True             # Categorical (Boolean)
}
```

## Why Understanding This Matters

1. **Data Preprocessing:** Need to handle categoricals differently
2. **Model Selection:** Some models handle categories better
3. **Feature Engineering:** Must convert categories to numbers
4. **Performance:** Proper handling improves accuracy
5. **Interpretation:** Understanding what features mean

## Summary

**Categorical Variables:**
- Represent categories/labels/groups
- Cannot do meaningful math
- Come in two types: Nominal (no order) and Ordinal (has order)
- ML models need them converted to numbers
- Common in real-world data

**Key Distinction:**
- Numerical = Can do math (age, price, height)
- Categorical = Labels/categories (color, gender, brand)

**Next Step:**
We need to convert categorical variables to numerical form.
That's called **Encoding**!

## Practice

1. Classify each as categorical or numerical:
   - Movie genre
   - Student GPA
   - Car color
   - Number of employees
   - Job title
   - Temperature
   - Zip code (tricky!)

2. For each categorical variable, identify if nominal or ordinal:
   - T-shirt size
   - Blood type
   - Customer satisfaction rating
   - City name

3. Why can't we directly use 'Male' and 'Female' in a linear regression?

4. Give 5 examples of categorical variables in a movie database
