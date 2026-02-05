# Types of Machine Learning

## Learning Objectives
- Identify the three main types of ML
- Understand when to use each type
- Distinguish between supervised, unsupervised, and reinforcement learning

## The Three Main Types

Machine Learning has 3 main branches:

1. **Supervised Learning** - Learning with a teacher
2. **Unsupervised Learning** - Learning without a teacher  
3. **Reinforcement Learning** - Learning by trial and error

## 1. Supervised Learning

**Definition:** Learning from labeled data (data with known answers)

### Key Characteristics:
- Have input (features) AND output (labels)
- Like a teacher showing correct answers
- Model learns from examples
- Goal: Predict labels for new data

### Analogy: Learning Math
- Teacher gives problems WITH answers
- You learn from correct solutions
- Practice many examples
- Finally solve new problems alone

![Untitled](../../../../Machine%20Learning/Introduction%20to%20ML/Untitled%2012.png)

### The Process:

**Remember:** Model sees labeled training data
```
Email 1: [features] → SPAM
Email 2: [features] → HAM
Email 3: [features] → SPAM
...
```

**Formulate:** Model learns pattern
```
"If many_links AND word_free: → SPAM"
```

**Predict:** Apply to new data
```
New Email: [features] → Predict: SPAM
```

### Two Types of Supervised Learning:

**A) Regression** - Predict NUMBERS
- House prices: Predict $350,000
- Temperature: Predict 75°F
- Stock prices: Predict $150.50
- Student score: Predict 85/100

**B) Classification** - Predict CATEGORIES
- Email: SPAM or HAM
- Animal: CAT or DOG
- Customer: WILL CHURN or WON'T CHURN
- Medical: DISEASE or HEALTHY

### Quick Test:

| Problem | Regression or Classification? |
|---------|------------------------------|
| House price prediction | Regression (number) |
| Credit fraud detection | Classification (fraud/not fraud) |
| Email spam detection | Classification (spam/ham) |
| Customer churn | Classification (yes/no) |
| Drug recommendation | Classification (drug A/B/C) |
| Task deadline prediction | Regression (days) |
| Animal recognition | Classification (cat/dog/bird) |

### When to Use Supervised Learning:

✓ You have labeled training data
✓ Want to predict specific outcomes
✓ Clear input-output relationship
✓ Examples: Spam detection, image classification, price prediction

## 2. Unsupervised Learning

**Definition:** Learning from unlabeled data (no known answers)

### Key Characteristics:
- Have input (features) but NO labels
- No teacher/correct answers
- Model finds patterns on its own
- Goal: Discover hidden structure

### Analogy: Organizing Toys
- You have mixed toys
- No one tells you how to group them
- You notice: cars, dolls, blocks
- Group similar items together

### Common Tasks:

**A) Clustering** - Group similar items
```
Customers:
- Group 1: Young, high income, online shoppers
- Group 2: Older, medium income, store shoppers  
- Group 3: Students, low income, bargain hunters
```

**B) Dimensionality Reduction** - Simplify data
```
100 features → 10 most important features
```

**C) Anomaly Detection** - Find unusual items
```
Normal transactions: $10, $20, $15, $25
Anomaly: $10,000 ← Suspicious!
```

### Example: Customer Segmentation

```python
# Unlabeled customer data
customers = [
    [age=25, income=50k, spending=2k],
    [age=24, income=55k, spending=2.5k],
    [age=60, income=80k, spending=1k],
    [age=62, income=75k, spending=1.2k],
    ...
]

# Model finds 3 groups (no labels given!)
Group A: Young, high spending
Group B: Older, low spending
Group C: Middle age, medium spending
```

### When to Use Unsupervised Learning:

✓ Don't have labeled data
✓ Want to explore data structure
✓ Find natural groupings
✓ Examples: Customer segmentation, recommendation systems, data compression

## 3. Reinforcement Learning

**Definition:** Learning by trial and error with rewards/penalties

### Key Characteristics:
- Agent takes actions in environment
- Gets rewards (good) or penalties (bad)
- Learns which actions lead to best outcomes
- Goal: Maximize total reward

### Analogy: Training a Dog
- Dog tries action (sit, stay, roll)
- Good action → Get treat (reward!)
- Bad action → No treat (penalty)
- Dog learns: sitting → treats!

### The Process:

```
1. Agent observes state
2. Agent takes action
3. Environment gives reward/penalty
4. Agent learns from result
5. Repeat → Gets better over time
```

### Example: Game Playing

**Teaching AI to play chess:**
```
Try move → Win game → +100 reward
Try move → Lose game → -100 penalty
Try move → Still playing → 0

After millions of games:
AI learns winning strategies!
```

### Example: Self-Driving Car

```
State: Car position, road conditions, traffic
Actions: Accelerate, brake, turn, stop

Rewards:
+10: Stay in lane
+50: Reach destination
-100: Hit obstacle
-50: Break traffic rule

Car learns safe driving through experience!
```

### When to Use Reinforcement Learning:

✓ Sequential decision-making
✓ Long-term reward maximization  
✓ Learning from interaction
✓ Examples: Game AI, robotics, self-driving cars, trading

## Comparison Table

| Aspect | Supervised | Unsupervised | Reinforcement |
|--------|-----------|--------------|---------------|
| **Data** | Labeled | Unlabeled | Reward signals |
| **Teacher** | Yes | No | Environment |
| **Goal** | Predict labels | Find patterns | Maximize reward |
| **Example** | Spam detection | Clustering | Game playing |
| **Training** | Past examples | Current data | Trial and error |

## Which Type to Use?

**Use Supervised if:**
- Have labeled data
- Want specific predictions
- Examples: classification, regression

**Use Unsupervised if:**
- No labeled data
- Explore data structure
- Examples: clustering, dimensionality reduction

**Use Reinforcement if:**
- Sequential decisions
- Feedback from actions
- Examples: games, robotics

## Summary

**Three Types:**
1. **Supervised** = Learning with teacher (labeled data)
   - Regression: Predict numbers
   - Classification: Predict categories

2. **Unsupervised** = Learning without teacher (unlabeled data)
   - Clustering: Find groups
   - Patterns: Discover structure

3. **Reinforcement** = Learning by doing (rewards/penalties)
   - Actions: Try and learn
   - Goals: Maximize rewards

**Most Common:** Supervised learning (this course focuses here!)

## Practice

1. Classify each as supervised, unsupervised, or reinforcement:
   - Predicting house prices
   - Teaching robot to walk
   - Grouping customers by behavior
   - Email spam detection
   - Game playing AI
   - Finding similar songs

2. For house price prediction:
   - Which type of ML?
   - Regression or classification?
   - Why?
