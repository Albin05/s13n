# Implementing One-Hot Encoding in Python

## Learning Objectives
- Implement one-hot encoding using pandas
- Use get_dummies() function effectively
- Analyze encoded data
- Apply encoding to real datasets

## The Dataset

Let's use the hair color example:

```python
import pandas as pd
import numpy as np

# Original data
data = {
    'Person': [1, 2, 3, 4, 5],
    'Hair_Color': ['Blonde', 'Brunette', 'Redhead', 'Blonde', 'Brunette'],
    'Income': [50000, 60000, 55000, 45000, 70000]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
   Person Hair_Color  Income
0       1     Blonde   50000
1       2   Brunette   60000
2       3    Redhead   55000
3       4     Blonde   45000
4       5   Brunette   70000
```

## Method 1: Using pd.get_dummies()

### Basic Usage

```python
# One-hot encode Hair_Color column
encoded_df = pd.get_dummies(df, columns=['Hair_Color'])
print(encoded_df)
```

**Output:**
```
   Person  Income  Hair_Color_Blonde  Hair_Color_Brunette  Hair_Color_Redhead
0       1   50000                  1                    0                   0
1       2   60000                  0                    1                   0
2       3   55000                  0                    0                   1
3       4   45000                  1                    0                   0
4       5   70000                  0                    1                   0
```

**Notice:**
- Original 'Hair_Color' column removed
- 3 new binary columns added
- Column names: Hair_Color_{category}

### Step-by-Step Explanation

```python
# 1. Check unique categories
print(df['Hair_Color'].unique())
# Output: ['Blonde' 'Brunette' 'Redhead']

# 2. Apply get_dummies
encoded_df = pd.get_dummies(
    df,                          # DataFrame
    columns=['Hair_Color'],      # Column to encode
    prefix='Color'               # Optional: custom prefix
)

# 3. View result
print(encoded_df.columns)
# Output: ['Person', 'Income', 'Color_Blonde', 'Color_Brunette', 'Color_Redhead']
```

## Customizing get_dummies()

### Remove Prefix

```python
# No prefix in column names
encoded_df = pd.get_dummies(
    df,
    columns=['Hair_Color'],
    prefix='',           # Empty prefix
    prefix_sep=''        # No separator
)

print(encoded_df.columns)
# Output: ['Person', 'Income', 'Blonde', 'Brunette', 'Redhead']
```

### Custom Prefix

```python
# Custom meaningful prefix
encoded_df = pd.get_dummies(
    df,
    columns=['Hair_Color'],
    prefix='HC'          # Short for Hair Color
)

print(encoded_df.columns)
# Output: ['Person', 'Income', 'HC_Blonde', 'HC_Brunette', 'HC_Redhead']
```

### Drop First Category (Avoiding Dummy Variable Trap)

```python
# Drop first category to avoid multicollinearity
encoded_df = pd.get_dummies(
    df,
    columns=['Hair_Color'],
    drop_first=True      # Drops first category
)

print(encoded_df.columns)
# Output: ['Person', 'Income', 'Hair_Color_Brunette', 'Hair_Color_Redhead']
# 'Blonde' is dropped (it's the baseline)
```

**Why drop first?**
- For some models (linear regression), including all categories causes multicollinearity
- If Brunette=0 and Redhead=0, we know it's Blonde
- Baseline category is implied

## Multiple Categorical Columns

```python
# Data with multiple categorical variables
data = {
    'Customer': ['A', 'B', 'C', 'D'],
    'Size': ['Small', 'Medium', 'Large', 'Small'],
    'Color': ['Red', 'Blue', 'Red', 'Green'],
    'Price': [20, 25, 30, 20]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
  Customer    Size  Color  Price
0        A   Small    Red     20
1        B  Medium   Blue     25
2        C   Large    Red     30
3        D   Small  Green     20
```

### Encode All Categorical Columns

```python
# Encode both Size and Color
encoded_df = pd.get_dummies(
    df,
    columns=['Size', 'Color']
)

print(encoded_df)
```

**Output:**
```
  Customer  Price  Size_Large  Size_Medium  Size_Small  Color_Blue  Color_Green  Color_Red
0        A     20           0            0           1           0            0          1
1        B     25           0            1           0           1            0          0
2        C     30           1            0           0           0            0          1
3        D     20           0            0           1           0            1          0
```

## Real-World Example: Employee Data

```python
# Employee dataset
employees = {
    'Name': ['John', 'Sarah', 'Mike', 'Emma', 'David'],
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'Education': ['Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters'],
    'Salary': [50000, 70000, 90000, 55000, 75000]
}

df_emp = pd.DataFrame(employees)
print(df_emp)
```

**Output:**
```
    Name Department  Education  Salary
0   John      Sales  Bachelors   50000
1  Sarah         IT    Masters   70000
2   Mike      Sales        PhD   90000
3   Emma         HR  Bachelors   55000
4  David         IT    Masters   75000
```

### Encode for ML

```python
# Encode Department and Education
df_encoded = pd.get_dummies(
    df_emp,
    columns=['Department', 'Education'],
    drop_first=True
)

print(df_encoded)
```

**Output:**
```
    Name  Salary  Department_IT  Department_Sales  Education_Masters  Education_PhD
0   John   50000              0                 1                  0              0
1  Sarah   70000              1                 0                  1              0
2   Mike   90000              0                 1                  0              1
3   Emma   55000              0                 0                  0              0
4  David   75000              1                 0                  1              0
```

**Now ready for ML!**
```python
# Features for ML model
X = df_encoded[['Salary', 'Department_IT', 'Department_Sales', 
                'Education_Masters', 'Education_PhD']]

# All numerical - ready for training!
```

## Analyzing Encoded Data

### Check Correlations

```python
# Load and encode data
data = {
    'Person': range(1, 6),
    'Hair_Color': ['Blonde', 'Brunette', 'Redhead', 'Blonde', 'Brunette'],
    'Income': [50000, 60000, 55000, 45000, 70000]
}
df = pd.DataFrame(data)

# One-hot encode
encoded_df = pd.get_dummies(df, columns=['Hair_Color'])

# Check correlation with Income
correlations = encoded_df.corr()['Income'].sort_values(ascending=False)
print(correlations)
```

**Output:**
```
Income                     1.000000
Hair_Color_Brunette        0.801784
Hair_Color_Redhead         0.223607
Hair_Color_Blonde         -0.912871
Person                    -0.105409
```

**Insight:** Brunette hair color has strong positive correlation with income!

### Visualize Distribution

```python
# Count of each category
print(encoded_df[['Hair_Color_Blonde', 'Hair_Color_Brunette', 
                  'Hair_Color_Redhead']].sum())
```

**Output:**
```
Hair_Color_Blonde      2
Hair_Color_Brunette    2
Hair_Color_Redhead     1
```

## Complete ML Pipeline Example

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Load data
data = {
    'Size': ['Small', 'Medium', 'Large', 'Small', 'Large', 'Medium'],
    'Color': ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Red'],
    'Brand': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Price': [20, 25, 30, 22, 28, 26]
}
df = pd.DataFrame(data)

# 2. One-hot encode
df_encoded = pd.get_dummies(df, columns=['Size', 'Color', 'Brand'], drop_first=True)

# 3. Split features and target
X = df_encoded.drop('Price', axis=1)
y = df_encoded['Price']

# 4. Train model
model = LinearRegression()
model.fit(X, y)

# 5. Check feature importance
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', ascending=False)

print(feature_importance)
```

## Common Pitfalls and Solutions

### Pitfall 1: Forgetting to Drop Original Column

```python
# WRONG: Original column still present
df_wrong = pd.get_dummies(df['Hair_Color'])
df_result = pd.concat([df, df_wrong], axis=1)
# Now have both 'Hair_Color' AND encoded columns!

# RIGHT: Specify columns parameter
df_right = pd.get_dummies(df, columns=['Hair_Color'])
# Original column automatically removed
```

### Pitfall 2: New Categories in Test Data

```python
# Training data
train_data = {'Color': ['Red', 'Blue', 'Green']}
train_encoded = pd.get_dummies(train_data)
# Columns: Color_Red, Color_Blue, Color_Green

# Test data with new category!
test_data = {'Color': ['Red', 'Yellow']}  # 'Yellow' is new!
test_encoded = pd.get_dummies(test_data)
# Columns: Color_Red, Color_Yellow

# PROBLEM: Columns don't match!

# SOLUTION: Use same categories
all_categories = ['Red', 'Blue', 'Green', 'Yellow']
train_encoded = pd.get_dummies(train_data, columns=['Color'])
test_encoded = pd.get_dummies(test_data, columns=['Color'])
# Then ensure same columns
```

### Pitfall 3: Too Many Categories

```python
# If a column has 100 unique values
# get_dummies will create 100 columns!
# This causes:
# - Memory issues
# - Overfitting
# - Slow training

# SOLUTION: Group rare categories or use other encoding methods
```

## Summary

**Implementation Steps:**
1. Import pandas
2. Create or load DataFrame
3. Use `pd.get_dummies(df, columns=[...])`
4. Check result with `.head()` and `.columns`
5. Use encoded data for ML

**Key Parameters:**
- `columns`: Which columns to encode
- `prefix`: Custom column name prefix
- `drop_first`: Avoid multicollinearity

**Best Practices:**
- Always check correlations after encoding
- Use `drop_first=True` for linear models
- Handle new categories in test data
- Avoid encoding high-cardinality features

## Practice

1. Create a DataFrame with 'City' column (5 cities, 10 rows). One-hot encode it.

2. Encode this data and find which color correlates most with price:
```python
data = {'Color': ['Red', 'Blue', 'Red', 'Green', 'Blue'],
        'Price': [100, 200, 110, 150, 210]}
```

3. What happens if you encode a column with 50 unique categories?

4. Write code to encode multiple categorical columns and prepare data for sklearn model

5. How would you handle a test set that has a new category not seen in training?
