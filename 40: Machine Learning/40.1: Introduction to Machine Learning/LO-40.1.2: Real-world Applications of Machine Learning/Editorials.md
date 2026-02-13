
# Editorials

## Q1
### Title
Identifying Non-ML Tasks

### Problem Description
Select the task that does not require Machine Learning.

### Objective
Distinguish between deterministic calculations and probabilistic predictions.

### Hint
If a calculator can do it perfectly every time with a simple formula, it's not ML.

### Short Explanation
Calculating a shopping cart total is a deterministic sum ($A + B + C$). There is no pattern to learn, just math to execute.

### Detailed Explanation
* **A (Prediction):** Stock markets are volatile and require pattern recognition (ML).
* **B (Calculation):** Summing prices is exact arithmetic. No learning is involved.
* **C (Diagnosis):** Interpreting X-rays is a complex visual task (ML/Computer Vision).
* **D (NLP):** Speech is noisy and complex (ML/NLP).

---

## Q2
### Title
Simple Intent Classification

### Problem Description
Classify text based on keyword presence.

### Objective
Demonstrate a basic rule-based approach that precedes ML text classification.

### Hint
Use Python's `in` operator to check for substrings.

### Short Explanation
Check for specific keywords and return the corresponding category label.

### Detailed Explanation
```python
def classify_intent(text):
    text = text.lower()
    if "money" in text or "refund" in text:
        return "Refund"
    elif "broken" in text or "error" in text:
        return "Technical"
    else:
        return "General"

```

---

## Q3

### Title

Counting System Flags

### Problem Description

Calculate total positive predictions given True Positives and False Positives.
True Positives (Correctly flagged): 50
False Positives (Incorrectly flagged): 5

### Objective

Understand basic confusion matrix terminology.

### Hint

Total Flags = Correct Flags + Incorrect Flags.

### Short Explanation

.

### Detailed Explanation

The system "raised a flag" in two cases:

1. When it was actually fraud (50 times).
2. When it was actually safe but the system thought it was fraud (5 times).
Total flags raised = .

---

## Q4

### Title

Computer Vision Scenarios

### Problem Description

Select scenarios involving visual data processing.

### Objective

Map industry applications to ML domains.

### Hint

Look for tasks that involve "seeing" or processing images/video.

### Short Explanation

A and C involve cameras and image processing. B is Audio/NLP. D is Recommender Systems (Data mining).

### Detailed Explanation

* **A (True):** Detecting stop signs requires analyzing video feeds (Computer Vision).
* **B (False):** Understanding voice is Audio Processing / NLP.
* **C (True):** Identifying defects requires analyzing images of parts (Computer Vision).
* **D (False):** Recommendations rely on user history data, not visual data.

---

## Q5

### Title

Simple Recommendation Logic

### Problem Description

Find items in `user2`'s list that are missing from `user1`'s list.

### Objective

Implement a basic collaborative filtering concept ("User 1 is like User 2, so recommend what User 2 has").

### Hint

Use Python sets for easy difference calculation: `set(user2) - set(user1)`.

### Short Explanation

Convert lists to sets and find the difference.

### Detailed Explanation

```python
def get_recommendations(history):
    u1_items = set(history['user1'])
    u2_items = set(history['user2'])
    
    # Items in U2 that are NOT in U1
    recs = u2_items - u1_items
    return list(recs)

```

* User 1 has {A, B}
* User 2 has {B, C}
* Difference: {C} -> Recommend 'C' to User 1.

---

## Q6

### Title

ML in Healthcare

### Problem Description

Explain the impact of ML on healthcare with examples.

### Objective

Discuss high-impact real-world applications.

### Hint

Think about X-rays, drug discovery, and patient monitoring.

### Short Explanation

ML helps in early diagnosis (Radiology), personalized treatment (Genomics), and drug discovery.

### Detailed Explanation

1. **Medical Imaging (Diagnosis):** ML algorithms (CNNs) analyze X-rays, MRIs, and CT scans to detect tumors or fractures with accuracy often exceeding human doctors.
2. **Predictive Analytics:** Models predict patient deterioration (e.g., sepsis) hours before it happens by monitoring vital signs, allowing early intervention.
3. **Drug Discovery:** ML simulates molecular interactions to find potential new drugs faster than traditional lab testing.

```

```
