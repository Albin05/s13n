
# Editorials

## Q1
### Title
Categorizing Algorithms

### Problem Description
Classify Random Forest within the AI/ML/DL hierarchy.

### Objective
Apply the hierarchy definitions to specific algorithms.

### Hint
Random Forest learns from data (ML) but does not use Neural Networks (not DL).

### Short Explanation
Random Forest is a Machine Learning algorithm. Since ML is a subset of AI, it is both AI and ML. It is not Deep Learning.

### Detailed Explanation
1.  **AI:** Yes, it mimics intelligence.
2.  **ML:** Yes, it learns from data patterns.
3.  **DL:** No, it uses Decision Trees, not Neural Networks.
* **Answer:** B (AI and ML).

---

## Q2
### Title
Class Hierarchy Simulation

### Problem Description
Use Python inheritance to model the AI > ML > DL relationship.

### Objective
Visualize the "subset" relationship using Object-Oriented Programming logic.

### Hint
`class Child(Parent):`

### Short Explanation
Create the classes and check inheritance.

### Detailed Explanation
```python
class AI:
    pass

class ML(AI):
    pass

class DL(ML):
    pass

chatgpt = DL()
print(isinstance(chatgpt, AI)) # Output: True

```

This proves that every instance of Deep Learning is inevitably an instance of Artificial Intelligence.

---

## Q3

### Title

Set Theory in AI

### Problem Description

Count how many sets a DL model belongs to.

### Objective

Reinforce the nesting doll concept.

### Hint

If you live in Paris, you also live in France and Europe.

### Short Explanation

A DL model belongs to D. Since D  M  A, it belongs to all three. Answer: 3.

### Detailed Explanation

*  (It is Deep Learning).
* Since ,  (It is Machine Learning).
* Since ,  (It is AI).
* Total sets: 3.

---

## Q4

### Title

Deep Learning Use Cases

### Problem Description

Identify tasks requiring Deep Learning's complexity.

### Objective

Distinguish between problems solvable by simple ML and those needing DL.

### Hint

DL excels at "Perception" tasks (Vision, Audio) with unstructured data.

### Short Explanation

A and C involve complex, unstructured data (Images, Audio) where DL shines. B is math. D is simple tabular data suited for standard ML.

### Detailed Explanation

* **A (DL):** MRI scans are pixels. DL (CNNs) is needed to extract features.
* **B (None):** Basic arithmetic.
* **C (DL):** Speech and Language are complex and sequential (RNNs/Transformers).
* **D (ML):** Tabular data with few columns is usually better/faster with Linear Regression or Random Forests.

---

## Q5

### Title

Keyword Classification Logic

### Problem Description

Classify text descriptions into AI, ML, or DL.

### Objective

Implement a simple rule-based classifier (which ironically is "AI" but not "ML").

### Hint

Check for specific substrings in order of specificity (DL first).

### Short Explanation

Check DL keywords, then ML keywords, then AI keywords.

### Detailed Explanation

```python
def classify_tech(text):
    text = text.lower()
    if "neural network" in text or "layers" in text:
        return "DL"
    elif "learning" in text or "data" in text or "statistical" in text:
        return "ML"
    elif "rule" in text or "if-else" in text:
        return "AI"
    else:
        return "Unknown"

```

---

## Q6

### Title

The Deep Learning Revolution

### Problem Description

Explain why DL is distinct regarding Feature Extraction and Scale.

### Objective

Deep dive into the technical differentiator of DL.

### Hint

In ML, you tell the computer "Look for ears". In DL, the computer figures out ears are important.

### Short Explanation

DL automates feature extraction and scales with massive data.

### Detailed Explanation

1. **Feature Extraction:** In traditional ML, a human expert must hand-craft features (e.g., edge detection filters for images). In DL, the early layers of the neural network *learn* these features automatically from raw data.
2. **Data Scale:** Traditional ML algorithms often "plateau" (stop improving) after a certain amount of data. DL models are "data hungry" and continue to improve as you feed them more data, making them viable for "Big Data" problems like Google Search or Self-Driving Cars.

```

```
