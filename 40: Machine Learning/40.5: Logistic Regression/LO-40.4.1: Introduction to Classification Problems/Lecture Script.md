# Lecture Script: Introduction to Classification Problems

## Topic: The Need for Classification

### Why (Importance)
Imagine you are building a security system for an airport. It's not enough to calculate a "risk score" as a random number; you need to make a definitive decision: **Safe** or **Suspicious**.
Real-world decision-making often boils down to discrete choices.
* Will this customer churn? (Yes/No)
* Is this transaction fraudulent? (Yes/No)
* Which digit is written here? (0-9)

We need a mathematical framework that doesn't just give us a trend line (like Regression) but draws a boundary to separate these groups.

### What (Concept)
**Classification** is the process of predicting a discrete class label ($y$) based on input features ($X$).

* **Input ($X$):** The features (e.g., word count in an email, pixel intensity in an image).
* **Output ($y$):** A category.
    * $y \in \{0, 1\}$ (Binary Classification)
    * $y \in \{0, 1, 2, ..., k\}$ (Multi-class Classification)

**Key Difference from Regression:**
* **Regression:** Predicts "How much?" (Continuous). Example: Predicting house price ($500k, $505k...).
* **Classification:** Predicts "Which one?" (Discrete). Example: Predicting if a house will sell (Yes/No).

### How (Method / Example)
How do we classify data mathematically? We look for a **Decision Boundary**.

Consider a dataset of students with two features:
1.  Hours Studied
2.  Attendance %

We want to classify them as **Pass (1)** or **Fail (0)**.

**Step 1: Plot the data.**
Imagine plotting students on a graph. You might see that students with high attendance and high study hours cluster at the top-right (Pass), while others cluster at the bottom-left (Fail).

**Step 2: Draw a line.**
A classifier tries to draw a line (or a curve) that separates these two clusters.
* Everything on one side of the line is predicted as "Pass".
* Everything on the other side is predicted as "Fail".

**Code Example (Python/Pseudo):**
```python
# Simple concept of thresholding a regression output to make it a classifier
prediction_score = 0.75 # Assume this is a probability output from a model
threshold = 0.5

if prediction_score >= threshold:
    print("Class: 1 (Pass)")
else:
    print("Class: 0 (Fail)")
