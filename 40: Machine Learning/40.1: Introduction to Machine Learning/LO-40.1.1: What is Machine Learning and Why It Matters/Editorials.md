
# Editorials

## Q1
### Title
AI vs ML Hierarchy

### Problem Description
Identify the correct relationship between Artificial Intelligence and Machine Learning.

### Objective
Clarify the taxonomy of the field.

### Hint
Think of Russian nesting dolls. AI is the big one.

### Short Explanation
Machine Learning is a sub-field (subset) of Artificial Intelligence. Deep Learning is a subset of Machine Learning.

### Detailed Explanation
* **AI:** Any technique that enables computers to mimic human intelligence.
* **ML:** A subset of AI that uses statistical methods to enable machines to improve with experience.
* **Answer:** A.

---

## Q2
### Title
Simple Linear Model

### Problem Description
Implement a function representing the rule $y = 2x + 1$.

### Objective
Demonstrate that a "Model" is just a mathematical function.

### Hint
Return `2 * x + 1`.

### Short Explanation
The code simply implements the mathematical relationship.

### Detailed Explanation
```python
def predict_rule(x):
    return 2 * x + 1

```

In a real ML scenario, the computer would figure out the `2` and `1` numbers on its own from data.

---

## Q3

### Title

Accuracy Calculation

### Problem Description

Calculate percentage accuracy: 900 correct out of 1000.

### Objective

Basic metric calculation.

### Hint

(Correct / Total) * 100.

### Short Explanation

. .

### Detailed Explanation

Accuracy is the most basic metric for classification models.


---

## Q4

### Title

ML Use Cases

### Problem Description

Identify problems requiring ML vs Deterministic Algorithms.

### Objective

Distinguish between solvable (math) and learnable (pattern) problems.

### Hint

If there is a strict formula (like ), you don't need ML.

### Short Explanation

A and C require ML. B and D are solved by exact algorithms/formulas.

### Detailed Explanation

* **A (True):** Handwriting varies infinitely; no formula exists. Needs ML.
* **B (False):** Area = . Exact formula exists. No ML needed.
* **C (True):** User preference is complex and changing. Needs ML.
* **D (False):** Shortest path is a solved logic problem (Graph Theory). No ML needed.

---

## Q5

### Title

Simple Training Logic

### Problem Description

Calculate a ratio from data and apply it to a new input.

### Objective

Simulate a very basic "Training" and "Prediction" phase.

### Hint

Calculate `avg(prices) / avg(sizes)` to get the rate.

### Short Explanation

Find the rate per sq ft, then multiply by 2500.

### Detailed Explanation

```python
def predict_price(sizes, prices, new_size):
    # Training: Finding the pattern (rate)
    avg_price = sum(prices) / len(prices)
    avg_size = sum(sizes) / len(sizes)
    rate = avg_price / avg_size # roughly 0.2
    
    # Prediction: Applying the pattern
    return rate * new_size

```

---

## Q6

### Title

Explicit vs Learned Programming

### Problem Description

Explain the definition of ML using a Spam Filter example.

### Objective

Test conceptual understanding of the paradigm shift.

### Hint

Explicit = Hardcoded rules. Learned = Statistical patterns.

### Short Explanation

Explicit programming requires a human to write rules like "If 'Viagra' then Spam". ML feeds 1000 emails to an algorithm, and the computer figures out that "Viagra" usually appears in Spam.

### Detailed Explanation

* **Explicitly Programmed:** A human programmer must anticipate every possible spam keyword (`"Free"`, `"Winner"`, `"Click here"`). If spammers change to `"W1nner"`, the code fails until the human updates it.
* **Machine Learning:** We feed the computer labeled examples. The computer notices that emails containing `"W1nner"` are marked as spam by users. It updates its own internal rules (model) automatically. We did not program the rule for `"W1nner"`; the machine learned it.

```

```
