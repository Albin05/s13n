# Understanding Models and Algorithms

## Learning Objectives
- Define what a model is in machine learning
- Understand what an algorithm does
- Distinguish between models and algorithms
- Apply these concepts to real examples

## Key Terms in Machine Learning

### What is a Model?

A **model** is a set of rules that represent our data and can be used to make predictions.

Think of it like a recipe:
- Recipe = Model
- Ingredients = Data
- Cooking process = Algorithm
- Final dish = Prediction

**Example:**
```
Model for spam detection:
IF (word_count["free"] > 3) AND (num_links > 5):
    prediction = "SPAM"
ELSE:
    prediction = "NOT SPAM"
```

### What is an Algorithm?

An **algorithm** is a procedure or set of steps used to solve a problem or perform a computation.

**The goal of an algorithm is to build a model.**

**Analogy:**
- Algorithm = Construction process
- Model = The house built
- Data = Building materials

## Spam vs Ham Example

### The Scenario
Bob sends you emails. 6 out of 10 are spam.

### Creating a Model

**Rule (Model):**
> "If email is from Bob, there's 60% chance it's spam"

**Note:** This rule may be wrong, but it's the best we can come up with given our data!

### Making a Prediction

New email from Bob arrives:
- 60% likely spam
- 40% likely ham (not spam)
- Safer to predict: SPAM

**We may be wrong!** But we made the best prediction with available knowledge.

## Can We Do Better?

Yes! Let's analyze emails more:

### When Bob sends emails:
![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%205.png)

Maybe day matters?

### File attachments:
![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%206.png)

Large files → spam?

### Better Model:
```python
if (day == "Sunday") AND (file_size > 10MB) AND (from_bob == True):
    prediction = "SPAM"
    confidence = 85%
```

## Features

**Feature:** Any property or characteristic of data that the model uses to make predictions.

Features are represented by **x_i**

**Examples in spam detection:**
- Email size (KB)
- Number of spelling mistakes
- Day of week
- Time sent
- Number of appearances of word "buy"
- Number of recipients

```python
features = {
    'size_kb': 150,
    'spelling_mistakes': 10,
    'day': 'Sunday',
    'time': '15:30',
    'word_buy_count': 4,
    'num_recipients': 1
}
```

### Improved Model with Features:
```
IF (size > 10KB) AND 
   (spelling_mistakes > 10) AND 
   (day == "Sunday") AND 
   (time > "3pm") AND 
   (word_buy_count > 10):
    prediction = "SPAM"
```

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%208.png)

## Labels

**Label:** The thing we're predicting - the **y** variable.

The label is the output/answer we want.

**Examples:**
- Email: Spam or Ham
- Animal: Cat or Dog  
- House: Price ($)
- Student: Pass or Fail

## Algorithm → Model → Prediction Flow

```
1. Algorithm (Process)
   ↓
2. Model (Rules learned)
   ↓  
3. Prediction (Output)
```

**Example:**
```
1. Linear Regression Algorithm
   ↓
2. Model: y = 2x + 3
   ↓
3. Prediction: When x=5, y=13
```

## Summary

1. **Model** = Set of rules for predictions
2. **Algorithm** = Process to build the model
3. **Features** = Properties used for predictions (x)
4. **Labels** = What we're predicting (y)
5. More features → potentially better model (but not always!)

## Practice

1. What's the difference between a model and an algorithm?
2. List 5 features for predicting house prices
3. What is the label in a spam detection problem?
4. Why do we need features?
