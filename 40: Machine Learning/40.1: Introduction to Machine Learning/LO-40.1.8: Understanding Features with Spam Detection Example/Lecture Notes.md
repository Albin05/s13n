# Understanding Features with Spam Detection Example

## Learning Objectives
- Understand what features are in machine learning
- Identify good features for a problem
- Apply feature selection to spam detection
- Recognize feature importance

## The Spam Detection Challenge

You receive an email from Bob. Is it spam or ham (not spam)?

### Initial Simple Approach

**Basic Model:**
> "6 out of 10 Bob's emails are spam, so this one is probably spam too"

**Problem:** We're treating all of Bob's emails the same way!

Can we do better? YES - by looking at FEATURES!

## What Are Features?

**Feature:** Any property or characteristic of the data that helps make predictions.

### Features in Spam Emails

**When does Bob send spam?**

Possible features to examine:
1. **Day of week** - Does he send spam on weekends?
2. **Time of day** - Spam at night?
3. **File size** - Large attachments?
4. **Number of links** - Many links = spam?
5. **Spelling mistakes** - Poor grammar?
6. **Specific words** - Contains "FREE", "CLICK", "BUY"?
7. **Number of recipients** - Mass email?

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%205.png)

## Feature Analysis Example

### Feature 1: Day of Week
```python
Monday:    Spam=1, Ham=2
Tuesday:   Spam=0, Ham=3  
Wednesday: Spam=2, Ham=1
Thursday:  Spam=1, Ham=2
Friday:    Spam=0, Ham=3
Saturday:  Spam=1, Ham=1
Sunday:    Spam=1, Ham=0
```

**Insight:** Sunday emails from Bob are usually spam!

### Feature 2: File Attachments
![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%207.png)

```python
No attachment:     Spam=2, Ham=8
Small (<1MB):      Spam=1, Ham=5
Medium (1-10MB):   Spam=2, Ham=1
Large (>10MB):     Spam=5, Ham=0
```

**Insight:** Large files → likely spam!

## Building a Better Model

### Using Multiple Features

**Simple Model (No Features):**
```
from_bob == True → 60% spam
```

**Better Model (With Features):**
```python
if from_bob AND day=="Sunday" AND file_size>10MB:
    spam_probability = 95%
elif from_bob AND num_links>5:
    spam_probability = 80%
elif from_bob:
    spam_probability = 60%
```

## Feature Representation

Features are represented as **x_i** (x with subscript i)

**Example Email Feature Vector:**
```python
email_features = {
    'x1_size_kb': 15000,        # 15MB
    'x2_num_links': 8,
    'x3_spelling_errors': 12,
    'x4_day': 'Sunday',
    'x5_time_hour': 15,         # 3 PM
    'x6_word_buy_count': 5,
    'x7_word_free_count': 3,
    'x8_num_recipients': 1
}
```

## Complex Multi-Feature Model

```python
spam_score = 0

if email['size_kb'] > 10000:
    spam_score += 20
    
if email['spelling_errors'] > 10:
    spam_score += 15
    
if email['day'] == 'Sunday':
    spam_score += 10
    
if email['time_hour'] > 15:  # After 3 PM
    spam_score += 5
    
if email['word_buy_count'] > 5:
    spam_score += 25

if spam_score > 40:
    prediction = "SPAM"
else:
    prediction = "HAM"
```

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%208.png)

## Is Number of Recipients a Feature?

**Question:** Should we use "number of recipients" as a feature?

**Analysis:**
- Mass emails (>10 recipients) → Often spam
- Personal emails (1 recipient) → Usually ham

**Answer:** YES! It's a useful feature.

## Important Insights About Features

### More Features ≠ Always Better

**Good Features:**
- Relevant to the problem
- Actually correlate with outcome
- Available at prediction time

**Bad/Useless Features:**
- Random noise
- No correlation with outcome
- Example: "Color of Bob's shirt" probably doesn't affect spam!

### Feature Engineering is Crucial

The quality of features often matters MORE than the algorithm!

**Example:**
- Poor features + Best algorithm = Poor model
- Good features + Simple algorithm = Good model

## Practical Example: House Price Prediction

**Features for house prices:**
```python
house_features = {
    'square_feet': 2000,
    'num_bedrooms': 3,
    'num_bathrooms': 2,
    'age_years': 10,
    'distance_to_downtown_km': 5,
    'has_garage': True,
    'neighborhood_crime_rate': 2.5,
    'school_rating': 8.5
}
```

**Good features?** YES - all affect price!

**Useless features:**
- Color of mailbox
- Previous owner's name
- Street name length

## Summary

1. **Features** = Properties that help make predictions
2. Multiple features → Better predictions
3. Choose relevant, meaningful features
4. Represent features as x₁, x₂, x₃, ...
5. Feature quality matters MORE than quantity
6. Feature engineering is key to good ML

## Practice

1. List 5 features for predicting student exam performance
2. List 5 features for predicting if a customer will buy a product
3. Which is a better feature for spam detection: (a) email size or (b) sender's shoe size? Why?
4. Create a feature vector for predicting movie success
5. Why might "day of week" be a useful feature for spam detection?
