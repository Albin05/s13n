# Regression vs Classification

## Learning Objectives
- Clearly distinguish regression from classification
- Identify output types
- Choose correct approach for problems
- Understand when to use each

## The Fundamental Difference

**Regression:** Predict a **CONTINUOUS NUMBER**
**Classification:** Predict a **CATEGORY/CLASS**

Think of it this way:
- Regression answers: "How much?"
- Classification answers: "Which type?"

## Visual Comparison

### Regression Output:
```
Price: $350,000
       $350,001
       $350,002
       ...
       $450,000
```
**Infinite possibilities between values!**

### Classification Output:
```
Type: Spam
      Ham
```
**Fixed, discrete options only!**

## Side-by-Side Examples

### Example 1: Student Performance

**Regression:**
```python
# Predicting exact score
input: study_hours = 6
output: score = 82.5   # Any number 0-100
```

**Classification:**
```python
# Predicting pass/fail
input: study_hours = 6
output: result = "PASS"  # Only two options
```

### Example 2: Weather

**Regression:**
```python
# Temperature prediction
input: time, humidity, pressure
output: temperature = 72.5°F  # Continuous
```

**Classification:**
```python
# Rain prediction
input: time, humidity, pressure
output: will_rain = "Yes"  # Category
```

### Example 3: Real Estate

**Regression:**
```python
# House price
features = {sqft: 2000, beds: 3}
output: price = $350,000  # Continuous value
```

**Classification:**
```python
# House type
features = {sqft: 2000, beds: 3}
output: type = "Single Family"  # Category
```

## Detailed Comparison Table

| Aspect | Regression | Classification |
|--------|-----------|----------------|
| **Output Type** | Continuous number | Discrete category |
| **Example Outputs** | 72.5, 350000, 85.3 | Spam/Ham, Cat/Dog, Yes/No |
| **Question** | How much? How many? | Which one? What type? |
| **Scale** | Can be any value | Fixed set of options |
| **Graph** | Line or curve | Decision boundaries |
| **Metrics** | MSE, RMSE, MAE | Accuracy, Precision, Recall |
| **Algorithms** | Linear Reg, Polynomial Reg | Logistic Reg, Decision Trees |

## Common Real-World Problems

### Regression Problems:

1. **Financial:**
   - Stock price: $150.25
   - Loan amount: $25,000
   - Sales revenue: $1.2M
   - Interest rate: 3.5%

2. **Physical:**
   - Temperature: 72.5°F
   - Distance: 15.3 miles
   - Weight: 180.5 lbs
   - Height: 5.8 feet

3. **Business:**
   - Customer lifetime value: $5,432
   - Conversion rate: 2.3%
   - Website traffic: 50,234 visits
   - Processing time: 45.2 seconds

### Classification Problems:

1. **Binary (2 classes):**
   - Email: Spam or Ham
   - Customer: Will churn or Won't churn
   - Loan: Approved or Denied
   - Disease: Present or Absent

2. **Multi-class (>2 classes):**
   - Animal: Cat, Dog, Bird, Fish
   - Grade: A, B, C, D, F
   - Priority: Low, Medium, High
   - Department: Sales, IT, HR, Finance

## The Same Data, Different Problems

You can frame the SAME dataset as regression OR classification!

### Dataset: Student Performance

```python
student_data = {
    'study_hours': 6,
    'attendance': 85,
    'assignments_done': 8
}
```

**As Regression:**
```python
# Predict exact score
output = 82.5  # Continuous
```

**As Classification:**
```python
# Predict grade category
output = "B"   # Discrete (A, B, C, D, F)
```

**As Binary Classification:**
```python
# Predict pass/fail
output = "PASS"  # Discrete (PASS, FAIL)
```

## When Boundaries Blur

### Ordinal Classification
Sometimes classification has order:

```python
# Customer satisfaction
output = "Very Satisfied"  # 5 ordered categories
# Poor < Fair < Good < Very Good < Excellent
```

This looks numerical but is still classification!
- Fixed options (not continuous)
- Can't be 3.5 (between Good and Very Good)

### Discretized Regression
Sometimes we bin continuous values:

```python
# Original regression: age = 25.5 years
# Discretized: age_group = "Young Adult"  # 18-30

# Still really regression data!
# Just converted for convenience
```

## How to Decide?

Ask these questions:

### 1. What is the output?
- Number that can vary continuously → **Regression**
- Category from fixed set → **Classification**

### 2. Can there be values between?
- Yes (72.3°F, 72.4°F possible) → **Regression**
- No (only Spam or Ham, nothing between) → **Classification**

### 3. Does mathematical difference make sense?
- Yes ($300k - $200k = $100k meaningful) → **Regression**
- No (Cat - Dog = ??? nonsense) → **Classification**

### 4. Are you predicting quantity or type?
- Quantity (how much, how many) → **Regression**
- Type (which one, what kind) → **Classification**

## Practical Exercise

Classify each as Regression or Classification:

1. **Predicting house price**
   - Output: $350,000 (continuous number)
   - Answer: **Regression**

2. **Spam email detection**
   - Output: Spam (category)
   - Answer: **Classification**

3. **Student final score**
   - Output: 85.5 (continuous)
   - Answer: **Regression**

4. **Movie genre identification**
   - Output: Action (category)
   - Answer: **Classification**

5. **Expected delivery time**
   - Output: 45.3 minutes (continuous)
   - Answer: **Regression**

6. **Credit card fraud detection**
   - Output: Fraudulent (category)
   - Answer: **Classification**

7. **Restaurant rating prediction**
   - Tricky! Depends on output:
   - If: 4.5 stars (continuous) → **Regression**
   - If: "Excellent" (category) → **Classification**

## Impact on Model Choice

Your problem type determines algorithm:

### For Regression:
- Linear Regression
- Polynomial Regression
- Ridge/Lasso Regression
- Support Vector Regression

### For Classification:
- Logistic Regression (despite name!)
- Decision Trees
- Random Forest
- SVM for Classification

**Can't mix!**
- Don't use classification algorithms for regression
- Don't use regression algorithms for classification

## Summary

**Regression:**
- Continuous numerical output
- Infinite possible values
- "How much?" questions
- Example: Predicting price

**Classification:**
- Discrete categorical output
- Fixed set of options
- "Which type?" questions
- Example: Identifying spam

**Key Rule:**
- Can be any number between values → Regression
- Must be one of fixed options → Classification

**Remember:**
The type of output determines your approach!

## Practice

1. For each, state Regression or Classification and why:
   - Predicting stock price tomorrow
   - Detecting if transaction is fraudulent
   - Estimating number of sales
   - Categorizing customer feedback
   - Forecasting temperature

2. Can "customer satisfaction score (1-5)" be both? Explain.

3. Give 3 examples where same data could be framed as regression OR classification

4. Why can't you average categories in classification?

5. Create a problem that could be either regression or classification depending on how you frame it
