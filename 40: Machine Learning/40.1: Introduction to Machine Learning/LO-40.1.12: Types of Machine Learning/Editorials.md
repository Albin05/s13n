# Editorials

## Q1
### Title
Algorithm Input Requirements

### Problem Description
Identify the algorithm that trains without a target variable ($y$).

### Objective
Distinguish between Supervised and Unsupervised algorithms.

### Hint
Clustering algorithms look for patterns in $X$ alone.

### Short Explanation
Linear Regression, Logistic Regression, and Decision Trees are Supervised (require labels). K-Means is Unsupervised (no labels).

### Detailed Explanation
* **Linear Regression:** Predicts $y$ given $X$.
* **K-Means:** Groups $X$ into clusters. No $y$ needed.
* **Logistic Regression:** Classifies $X$ into $y$.
* Therefore, K-Means is the answer.

---

## Q2
### Title
Training Wrapper Logic

### Problem Description
Create a function that prints the training type based on the presence of labels.

### Objective
Implement simple logic to differentiate ML types programmatically.

### Hint
Use a standard `if/else` check on the `labels` argument.

### Short Explanation
Check if `labels is None`.

### Detailed Explanation
```python
def start_training(data, labels=None):
    if labels is not None:
        print("Starting Supervised Training")
        # train_model(data, labels)
    else:
        print("Starting Unsupervised Training")
        # train_model(data)

```

---

## Q3

### Title

Reinforcement Learning Reward Calculation

### Problem Description

Calculate total reward: (+10 for win), (-1 per step), (-50 for loss). Agent takes 15 steps + Win.

### Objective

Understand the accumulation of rewards in RL.

### Hint

Total = (Steps * StepPenalty) + FinalOutcomeReward.

### Short Explanation

Steps: . Win: . Total: .

### Detailed Explanation

1. **Step Penalty:** The agent took 15 steps. Each step costs -1. Total step penalty = .
2. **Terminal Reward:** The agent won. Reward = .
3. **Total Reward:** .

---

## Q4

### Title

Identifying Supervised Scenarios

### Problem Description

Select tasks suitable for Supervised Learning.

### Objective

Map real-world problems to ML categories.

### Hint

Look for prediction or classification based on historical examples.

### Short Explanation

A and C are correct. B is Clustering (Unsupervised). D is Reinforcement Learning.

### Detailed Explanation

* **A (Supervised):** Prediction (Regression) using labeled history (prices).
* **B (Unsupervised):** Finding groups (Clustering) without predefined labels.
* **C (Supervised):** Classification (Diagnosis) using labeled history (patient records).
* **D (RL):** Learning via trial-and-error interaction.

---

## Q5

### Title

Classifying ML Scenarios

### Problem Description

Map three specific scenarios to their ML types.

### Objective

Apply definitions of ML types to descriptions.

### Hint

A = Labeled Prediction. B = Pattern Finding. C = Interaction/Game.

### Short Explanation

A: Supervised, B: Unsupervised, C: RL.

### Detailed Explanation

```python
classification = {
    'A': 'Supervised',   # Historical labels available
    'B': 'Unsupervised', # No labels, finding structure
    'C': 'RL'            # Interaction and feedback
}
print(classification)

```

---

## Q6

### Title

Hybrid Approaches (Fraud Detection)

### Problem Description

Explain Fraud Detection as both Supervised and Unsupervised.

### Objective

Understand that one problem can be solved in multiple ways depending on data.

### Hint

Do you have a list of known fraud cases (Supervised) or are you looking for weird transactions (Unsupervised)?

### Short Explanation

* **Supervised:** Uses a dataset of past transactions labeled "Fraud" or "Legit" to train a classifier.
* **Unsupervised:** Uses raw transaction data to find "Outliers" (anomalies) that differ significantly from normal behavior, without knowing for sure if they are fraud.

### Detailed Explanation

1. **Supervised Approach:** We treat it as a **Classification** problem. We need a history of known fraud. The model learns the specific patterns of those frauds. *Pro:* High accuracy on known fraud types. *Con:* Misses new types of fraud not in the training set.
2. **Unsupervised Approach:** We treat it as an **Anomaly Detection** problem. We model "normal" behavior. Anything that deviates significantly (e.g., huge purchase at 3 AM) is flagged. *Pro:* Can catch new, unseen fraud types. *Con:* Higher false positives (flagging weird but legit transactions).

