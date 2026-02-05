# Understanding Features and Feature Selection

## Learning Objectives
- Understand what makes a good feature
- Learn how to select relevant features
- Recognize feature importance in ML models
- Apply feature selection to real problems

## What Makes a Good Feature?

Remember: **Features** are the input variables (x) that we use to make predictions.

But not all features are equally useful!

### Good vs Bad Features

**Good Features:**
✓ Relevant to the prediction
✓ Correlate with the output
✓ Available at prediction time
✓ Measurable/quantifiable
✓ Not redundant

**Bad Features:**
✗ Random or irrelevant
✗ No correlation with output
✗ Not available when needed
✗ Difficult to measure
✗ Duplicate information

## Example: Predicting House Prices

### Good Features:

```python
good_features = {
    'square_feet': 2000,           # Size matters!
    'num_bedrooms': 3,             # More rooms = higher price
    'num_bathrooms': 2,            # Bathrooms add value
    'age_years': 10,               # Newer = pricier
    'distance_downtown_km': 5,     # Location matters
    'has_garage': True,            # Amenities count
    'neighborhood_crime_rate': 2.1,# Safety affects price
    'school_rating': 8.5,          # Schools matter
    'lot_size_sqft': 5000          # Land size matters
}
```

**Why good?** All directly affect house value!

### Bad Features:

```python
bad_features = {
    'previous_owner_name': 'John Smith',    # Irrelevant!
    'street_name_length': 15,               # Random!
    'mailbox_color': 'blue',                # Doesn't matter!
    'house_number': 123,                    # No correlation!
    'seller_shoe_size': 10,                 # Ridiculous!
}
```

**Why bad?** No connection to house price!

## Feature Selection Process

### Step 1: Brainstorm Possible Features

For student exam prediction:
```python
possible_features = [
    'study_hours_per_day',
    'attendance_percentage',
    'previous_exam_scores',
    'assignment_completion',
    'participation_score',
    'sleep_hours',
    'favorite_color',          # ← Probably irrelevant!
    'shoe_size',               # ← Definitely irrelevant!
    'distance_from_school',
    'parents_education_level'
]
```

### Step 2: Evaluate Relevance

Ask: "Does this feature logically affect the outcome?"

**Relevant:**
- study_hours_per_day ✓ (more study = better)
- attendance_percentage ✓ (present = learn)
- previous_exam_scores ✓ (past performance indicator)
- assignment_completion ✓ (practice helps)

**Irrelevant:**
- favorite_color ✗ (no logical connection)
- shoe_size ✗ (completely unrelated)

### Step 3: Check Correlation

Look at data to verify:

```python
# Strong correlation (good features)
study_hours vs pass_rate: 0.85 correlation ✓
attendance vs pass_rate: 0.78 correlation ✓

# Weak correlation (bad features)
shoe_size vs pass_rate: 0.02 correlation ✗
favorite_color vs pass_rate: 0.01 correlation ✗
```

### Step 4: Remove Redundant Features

If two features tell the same information, keep only one:

```python
# Redundant pair:
feature_a = 'house_area_sqft'      # 2000 sqft
feature_b = 'house_area_sqm'       # 185.8 sqm

# They're the same thing! Keep one:
keep: 'house_area_sqft'
remove: 'house_area_sqm'
```

## Real-World Example: Email Spam Detection

### Comprehensive Feature Set:

```python
email_features = {
    # Size features
    'total_size_bytes': 15000,
    'subject_length': 45,
    'body_length': 500,
    
    # Content features
    'num_exclamation_marks': 5,
    'num_question_marks': 0,
    'num_capital_words': 12,
    'spelling_mistakes': 8,
    
    # Link features
    'num_links': 10,
    'num_external_links': 8,
    'has_shortened_url': True,
    
    # Word features
    'contains_free': True,
    'contains_click': True,
    'contains_urgent': True,
    'contains_winner': True,
    
    # Sender features
    'sender_reputation_score': 0.2,
    'sender_domain_age_days': 15,
    'sender_email_typos': True,
    
    # Timing features
    'sent_hour': 3,              # 3 AM
    'is_weekend': True,
    
    # Recipient features
    'num_recipients': 1000,       # Mass email!
    'is_in_contacts': False
}
```

### Feature Importance Analysis:

```python
# Most important features (strong predictors)
1. num_links (high links = spam)
2. contains_free (word "FREE" = spam)
3. sender_reputation (low reputation = spam)
4. num_recipients (mass email = spam)
5. spelling_mistakes (errors = spam)

# Less important features
8. subject_length (weak correlation)
9. sent_hour (some correlation)
10. is_weekend (minimal impact)
```

## Feature Selection Techniques

### 1. Domain Knowledge
Use your understanding of the problem:

**Predicting student performance:**
- Include: study time, attendance ✓
- Exclude: hair color, shoe size ✗

### 2. Correlation Analysis
Measure relationship with output:

```python
Feature             | Correlation with Pass
--------------------|---------------------
study_hours         | 0.85  ← Strong!
attendance          | 0.78  ← Strong!
sleep_hours         | 0.45  ← Moderate
distance_to_school  | 0.12  ← Weak
favorite_color      | 0.01  ← None!
```

Keep features with correlation > 0.3

### 3. Feature Importance from Models
Train a model and see which features it uses most:

```python
Random Forest Feature Importance:
1. square_feet:     0.35  (35% importance)
2. location:        0.25  (25% importance)
3. age:             0.15  (15% importance)
4. bedrooms:        0.12  (12% importance)
5. bathrooms:       0.08  (8% importance)
6. others:          0.05  (5% importance)
```

### 4. Dimensionality Reduction
If you have TOO many features (100+), use techniques like PCA to reduce.

## Common Feature Selection Mistakes

### Mistake 1: Using Too Many Features
```python
# BAD: 50 features for 100 data points
# Model overfits!

# GOOD: 5-10 features for 100 data points
# Model generalizes better
```

**Rule of Thumb:** Need at least 10x more data points than features

### Mistake 2: Including Irrelevant Features
```python
# Predicting house prices
bad_features = ['seller_name', 'listing_date', 'photo_quality']
# These don't affect actual value!
```

### Mistake 3: Feature Leakage
Including information not available at prediction time:

```python
# BAD: Predicting if customer will buy
features = {'customer_bought': True}  # ← This IS what we're predicting!

# GOOD: Use features available BEFORE purchase
features = {'browsing_time': 300, 'cart_items': 3, 'previous_purchases': 5}
```

### Mistake 4: Ignoring Data Availability
```python
# Feature: 'real_time_stock_price'
# Problem: May not be available when we need to predict!

# Better: 'previous_day_stock_price'
# Available when making prediction
```

## Summary

**Good Features Are:**
1. Relevant to the problem
2. Correlated with output
3. Available at prediction time
4. Easy to measure
5. Not redundant

**Feature Selection Process:**
1. Brainstorm possible features
2. Evaluate logical relevance
3. Check statistical correlation
4. Remove redundant features
5. Test model performance

**Key Principles:**
- Quality > Quantity
- More features ≠ Better model
- Domain knowledge crucial
- Avoid feature leakage
- Ensure data availability

## Practice

1. For predicting movie success, list 5 good features and explain why
2. For predicting restaurant rating, identify which features are bad: 
   - food_quality, chef_shoe_size, cleanliness, price_range, owner_name
3. Why is "customer_purchased" a bad feature for predicting if customer will purchase?
4. Calculate: If you have 500 data points, what's a reasonable number of features? Why?
5. Give an example of two redundant features in house price prediction
