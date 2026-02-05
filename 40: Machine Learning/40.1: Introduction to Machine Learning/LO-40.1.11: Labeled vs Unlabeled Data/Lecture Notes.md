# Labeled vs Unlabeled Data

## Learning Objectives
- Distinguish between labeled and unlabeled data
- Understand when each type is used
- Recognize the importance of labels in supervised learning

## What is Labeled Data?

**Labeled Data** = Data where we KNOW the answer (have the output/label)

Think of it like flashcards:
- Front: Question/Features
- Back: Answer/Label ✓

We can see BOTH sides!

### Example: Image Classification

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%209.png)

**Labeled Image Data:**
```
Image 1: [pixels...] → Label: "DOG"
Image 2: [pixels...] → Label: "CAT"  
Image 3: [pixels...] → Label: "DOG"
Image 4: [pixels...] → Label: "CAT"
```

We KNOW what each image is!

## What is Unlabeled Data?

**Unlabeled Data** = Data where we DON'T know the answer (no label)

Like flashcards with only the front side:
- Front: Question/Features
- Back: ??? (Unknown!)

### Example: New Images

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%2010.png)

**Unlabeled Image Data:**
```
Image A: [pixels...] → Label: ???
Image B: [pixels...] → Label: ???
Image C: [pixels...] → Label: ???
```

We DON'T know what these are - that's what we want to predict!

## Visual Comparison

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%2011.png)

### Labeled Data:
```
Input (Features) | Output (Label)
----------------|---------------
[Data]          | "Known Answer"
```

### Unlabeled Data:
```
Input (Features) | Output (Label)
----------------|---------------
[Data]          | ???
```

## Dog vs Cat Example

### Labeled Training Data:

Tell the computer what each image is:

**Image 1:** 
- Features: Long ears, wagging tail, more teeth, muscular, larger paws
- Label: **DOG** ✓

**Image 2:**
- Features: Sharp ears, whiskers, small paws, compact body
- Label: **CAT** ✓

### Unlabeled New Data:

Computer must predict:

**Image 3:**
- Features: [analyzes image]
- Label: ??? → Model predicts: **DOG**

## Detailed Feature Comparison

### Dog (Labeled Example):
- Lengthy Ears
- Wagging Tail
- More Teeth
- More Muscular  
- Larger Paws

### Cat (Labeled Example):
- Sharp Ears
- Whiskers
- Small Paws
- Sleek Body
- Retractable Claws

### Unknown Animal (Unlabeled):
- Has whiskers
- Sharp ears
- Small paws
→ Model predicts: **CAT**

## Real-World Example: Email Classification

### Labeled Training Emails:

```python
# Email 1
email_1 = {
    'from': 'shopping@deals.com',
    'subject': 'FREE OFFER!!!',
    'num_links': 10,
    'label': 'SPAM'  # ← We labeled this!
}

# Email 2
email_2 = {
    'from': 'boss@company.com',
    'subject': 'Meeting at 2pm',
    'num_links': 0,
    'label': 'HAM'  # ← We labeled this!
}

# ... 10,000 more labeled emails
```

### Unlabeled New Email:

```python
# New email arrives
new_email = {
    'from': 'unknown@site.com',
    'subject': 'CLICK HERE NOW!!!',
    'num_links': 8,
    'label': ???  # ← Don't know yet!
}

# Model predicts based on training
prediction = model.predict(new_email)
# → 'SPAM'
```

## Why Do We Need Both?

### Labeled Data (Training Phase)
**Purpose:** Teach the model

- Model learns from labeled examples
- Sees patterns: "emails with many links are usually spam"
- Builds understanding of features → labels relationship

**Requirement:** Need MANY labeled examples
- Image recognition: 100,000+ labeled images
- Spam detection: 10,000+ labeled emails
- Medical diagnosis: 1,000+ labeled patient cases

### Unlabeled Data (Prediction Phase)
**Purpose:** Use the model

- Apply learned patterns to new data
- Make predictions on unknown cases
- This is the actual goal!

## The Machine Learning Flow

```
1. TRAINING PHASE:
   Labeled Data → ML Algorithm → Model
   (Know answers)

2. PREDICTION PHASE:
   Unlabeled Data → Model → Predictions
   (Don't know answers)
```

## Challenge: Getting Labeled Data

### Problem:
Labeling data is expensive and time-consuming!

**Examples:**
- **Images:** Someone must look at each image and label it
  - 100,000 images × 10 seconds each = 277 hours!

- **Medical:** Expert doctors must review each case
  - Expensive and slow

- **Text:** Human must read and categorize
  - Boring and tedious

### Solutions:
1. **Crowdsourcing:** Pay many people small amounts
2. **Active Learning:** Model asks for labels only when uncertain
3. **Semi-supervised:** Use small labeled + large unlabeled data
4. **Transfer Learning:** Use pre-labeled data from similar problems

## Common Scenarios

### Scenario 1: Fully Supervised Learning
- Have: Lots of labeled data
- Use: Train model directly
- Example: Spam detection with labeled email database

### Scenario 2: Semi-Supervised Learning  
- Have: Little labeled + lots unlabeled data
- Use: Hybrid approaches
- Example: Photo organization (few labeled, many unlabeled)

### Scenario 3: Unsupervised Learning
- Have: Only unlabeled data
- Use: Find patterns without labels
- Example: Customer segmentation

## Summary

1. **Labeled Data** = Data + Known Answers
   - Used for training
   - Expensive to create
   - Required for supervised learning

2. **Unlabeled Data** = Data without Answers
   - Used for prediction
   - Easy to collect
   - What we want to predict on

3. **ML Process:**
   - Train on labeled data
   - Predict on unlabeled data

4. **Challenge:** Getting enough labeled data
5. **Solution:** Various labeling strategies

## Practice

1. Give 3 examples of labeled data
2. Give 3 examples of unlabeled data
3. Why is labeled data expensive to create?
4. In a house price prediction system:
   - What would be labeled data?
   - What would be unlabeled data?
5. How much labeled data do we typically need?
