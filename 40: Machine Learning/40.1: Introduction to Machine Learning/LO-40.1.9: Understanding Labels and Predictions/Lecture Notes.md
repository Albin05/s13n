# Understanding Labels and Predictions

## Learning Objectives
- Define what a label is in machine learning
- Understand the relationship between features and labels
- Distinguish between training labels and predictions
- Apply label concepts to real problems

## What is a Label?

**Label:** The thing we're predicting - the **y** variable.

The label is:
- The output/answer we want
- The target variable
- What the model learns to predict

**Representation:** Typically represented by variable **y**

## Examples of Labels

### Classification Labels (Categories)

| Problem | Features (x) | Label (y) |
|---------|-------------|-----------|
| Email Classification | Sender, size, words | Spam or Ham |
| Animal Recognition | Ears, tail, size | Cat or Dog |
| Loan Approval | Income, credit score | Approve or Deny |
| Medical Diagnosis | Symptoms, test results | Disease or Healthy |

### Regression Labels (Numbers)

| Problem | Features (x) | Label (y) |
|---------|-------------|-----------|
| House Prices | Size, location, age | Price ($) |
| Temperature | Time, location, season | Temperature (°F) |
| Stock Prices | Historical data, volume | Price ($) |
| Crop Yield | Rainfall, soil, fertilizer | Yield (tons) |

## Labels in Training vs Prediction

### During Training (Learning Phase)
```python
# Training data WITH labels
training_data = [
    {'features': [5, 8, 3], 'label': 'PASS'},   # We KNOW the answer
    {'features': [2, 4, 1], 'label': 'FAIL'},
    {'features': [7, 9, 4], 'label': 'PASS'},
]

# Model LEARNS from these labeled examples
model.train(training_data)
```

### During Prediction (Using Phase)
```python
# New data WITHOUT labels
new_student = {'features': [6, 7, 3], 'label': ???}

# Model PREDICTS the label
prediction = model.predict(new_student)  # → 'PASS'
```

## The Full Picture

```
TRAINING PHASE:
Input (Features + Labels) → Algorithm → Model

PREDICTION PHASE:  
Input (Features only) → Model → Predicted Label
```

## Detailed Example: Email Spam Detection

### Training Data (With Labels)

```python
# Email 1
features_1 = {
    'from': 'bob@email.com',
    'size_kb': 150,
    'num_links': 10,
    'has_word_free': True
}
label_1 = 'SPAM'  # ← We KNOW this

# Email 2
features_2 = {
    'from': 'alice@work.com',
    'size_kb': 20,
    'num_links': 1,
    'has_word_free': False
}
label_2 = 'HAM'  # ← We KNOW this

# ... 10,000 more labeled emails
```

### Model Learning

The model learns patterns:
```
Pattern discovered:
IF num_links > 5 AND has_word_free == True:
    → Probably SPAM
```

### New Email (Prediction)

```python
# New email arrives (NO label)
new_email = {
    'from': 'unknown@site.com',
    'size_kb': 200,
    'num_links': 8,
    'has_word_free': True
}

# Model predicts label
predicted_label = model.predict(new_email)
# → 'SPAM'
```

## Why Labels Matter

### 1. Labels Define the Problem

**What you label determines what the model predicts!**

Examples:
- Label emails as spam/ham → Spam detector
- Label emails as work/personal → Email categorizer
- Label emails by sentiment → Sentiment analyzer

### 2. Label Quality = Model Quality

**Bad Labels:**
```python
{'features': [large_file, many_links], 'label': 'HAM'}  # ← Wrong!
```
Model learns incorrectly!

**Good Labels:**
```python
{'features': [large_file, many_links], 'label': 'SPAM'}  # ← Correct!
```
Model learns correctly!

### 3. Need Many Labeled Examples

The model needs MANY examples to learn:
- Email spam: Need 1000s of labeled emails
- Image recognition: Need 100,000s of labeled images
- Medical diagnosis: Need 1000s of labeled patient cases

## Types of Labels

### Binary Labels (2 options)
```python
- Yes/No
- Spam/Ham
- Pass/Fail
- True/False
- 0/1
```

### Multi-class Labels (>2 options)
```python
- Animal type: Dog, Cat, Bird, Fish
- Grade: A, B, C, D, F
- Sentiment: Positive, Neutral, Negative
```

### Continuous Labels (numbers)
```python
- House price: $150,000 to $5,000,000
- Temperature: -20°F to 120°F
- Stock price: Any positive number
```

## Label vs Prediction

**Label:** The TRUE answer (what actually happened)

**Prediction:** What the model THINKS the answer is

**Goal:** Make predictions match labels as closely as possible!

```python
true_label = 'SPAM'
predicted_label = 'SPAM'
# ✓ Correct prediction!

true_label = 'HAM'
predicted_label = 'SPAM'  
# ✗ Wrong prediction (False Positive)
```

## Common Mistakes

**❌ Mistake 1:** Confusing features with labels
```python
# WRONG
label = 'large_file'  # This is a feature!

# RIGHT
label = 'SPAM'  # This is what we predict!
```

**❌ Mistake 2:** Not having enough labels
```python
training_data = [
    {features: [...], label: 'SPAM'},
    {features: [...], label: 'HAM'}
]
# Only 2 examples! Need 1000s!
```

**❌ Mistake 3:** Inconsistent labeling
```python
# Same features, different labels!
{features: [large, many_links], label: 'SPAM'}
{features: [large, many_links], label: 'HAM'}  # Confuses model!
```

## Summary

1. **Label** = What we're trying to predict (y)
2. **Features** = What we use to predict (x)
3. During training: Have both features AND labels
4. During prediction: Have features, predict label
5. Label quality is crucial for model quality
6. Need MANY labeled examples for good learning

## Practice

1. For each problem, identify the label:
   - Predicting house prices
   - Classifying images of animals
   - Detecting credit card fraud
   - Recommending movies

2. What's the difference between a label and a prediction?

3. Why do we need labels during training but not during prediction?

4. Give an example of:
   - Binary label problem
   - Multi-class label problem
   - Continuous label problem
