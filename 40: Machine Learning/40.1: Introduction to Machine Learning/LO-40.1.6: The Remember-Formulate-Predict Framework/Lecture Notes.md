# The Remember-Formulate-Predict Framework

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand the 3-step ML framework
- Apply Remember-Formulate-Predict to problems
- Recognize this pattern in ML applications

## How Humans Make Predictions

Let's think about how we make decisions:

**Question:** "Will a student pass an exam?"

### Step 1: Remember
We remember past situations:
- Student's performance in previous exams
- Assignment scores
- Class participation
- Study habits

### Step 2: Formulate
We create a hypothesis/rule:
> "If student consistently performed well in past exams and assignments, they are likely to pass this exam too."

### Step 3: Predict
Based on our hypothesis, we predict:
- This student will likely PASS (or FAIL)

**Note:** We may be right or wrong, but we used past experiences and reasoning!

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%204.png)

## Applying to Machine Learning

Machine Learning follows THE SAME framework!

### Step 1: Remember (Training Data)
```
Past Exam Data:
Student A: 8 hrs study, 90% attendance → PASSED
Student B: 2 hrs study, 60% attendance → FAILED  
Student C: 6 hrs study, 85% attendance → PASSED
Student D: 3 hrs study, 70% attendance → FAILED
...
```

The machine "remembers" this data.

### Step 2: Formulate (Build Model)
Machine creates a mathematical model (hypothesis):
```
Score = (0.3 × study_hours) + (0.5 × attendance) - 20

If Score > 50: PASS
Else: FAIL
```

This is the "rule" or "pattern" it discovered.

### Step 3: Predict (Use Model)
New student:
- Study hours: 7
- Attendance: 80%

```
Score = (0.3 × 7) + (0.5 × 80) - 20
Score = 2.1 + 40 - 20 = 22.1
```

**Prediction:** FAIL (Score not > 50)

## Example: House Price Prediction

### Remember
```python
Past House Sales:
House 1: 1500 sqft, 3 beds, 2 baths → $300,000
House 2: 2000 sqft, 4 beds, 3 baths → $400,000
House 3: 1200 sqft, 2 beds, 1 bath  → $250,000
...1000 more houses
```

### Formulate
Model learns pattern:
```
Price = (150 × sqft) + (20000 × bedrooms) + (15000 × bathrooms)
```

### Predict
New house: 1800 sqft, 3 beds, 2 baths
```
Price = (150 × 1800) + (20000 × 3) + (15000 × 2)
Price = 270,000 + 60,000 + 30,000
Price = $360,000
```

## Example: Dog vs Cat Classification

### Remember (Training)
- 10,000 images of dogs (labeled "dog")
- 10,000 images of cats (labeled "cat")

### Formulate (Learning)
Model identifies patterns:
- Dogs: longer snouts, floppy ears, varied sizes
- Cats: pointed ears, whiskers, compact body

### Predict (Classification)
New image → Model analyzes features → Predicts "DOG" or "CAT"

## Why This Framework Matters

**Limitations to Be Aware Of:**

1. **Past May Not Predict Future**
   - What if exam is much harder?
   - What if student had personal issues?

2. **Data Quality Matters**
   - Garbage in = Garbage out
   - Biased data = Biased predictions

3. **External Factors**
   - Student's health on exam day
   - Difficulty of specific exam
   - External circumstances

## The Framework in Action

Every ML system follows this:

| System | Remember | Formulate | Predict |
|--------|----------|-----------|---------|
| **Spam Filter** | Past emails | Spam patterns | New email → spam? |
| **Netflix** | Watch history | Preference model | Recommend shows |
| **Self-Driving** | Driving data | Road rules | Navigate safely |
| **Voice Assistant** | Speech samples | Speech patterns | Understand commands |

## Summary

1. **Remember:** Collect and store training data
2. **Formulate:** Learn patterns and create model
3. **Predict:** Apply model to new data

This framework is fundamental to ALL machine learning!

**Key Insight:** The better our "remembered" data, the better our "formulated" model, the better our "predictions"!

## Practice

1. Apply Remember-Formulate-Predict to: "Will it rain tomorrow?"
2. Why is quality of "Remember" step crucial?
3. Give example where this framework might fail
4. What's the difference between human and machine in this framework?
