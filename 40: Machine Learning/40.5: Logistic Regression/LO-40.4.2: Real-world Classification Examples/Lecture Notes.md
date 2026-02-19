# Real-world Classification Examples

## Key Domains of Classification

### 1. Spam Detection (Cybersecurity)
* **Type:** Binary Classification.
* **Input Features ($X$):** Text content (keywords), sender metadata, email formatting.
* **Output Classes ($y$):** Spam / Not Spam.

### 2. Fraud Detection (Finance)
* **Type:** Binary Classification.
* **Input Features ($X$):** Transaction amount, location, time of day, user's typical purchasing habits.
* **Output Classes ($y$):** Fraudulent / Legitimate.
* **Note:** This is typically an *imbalanced classification* problem because fraud is rare compared to normal transactions.

### 3. Medical Diagnosis (Healthcare)
* **Type:** Binary or Multi-class Classification.
* **Input Features ($X$):** Patient vitals, lab test results, imaging data.
* **Output Classes ($y$):** Disease Positive / Disease Negative.
* **Note:** High accuracy is critical, with a specific focus on minimizing False Negatives.

### 4. Customer Churn (Business/Marketing)
* **Type:** Binary Classification.
* **Input Features ($X$):** Subscription length, usage metrics, number of customer service complaints.
* **Output Classes ($y$):** Will Churn (Leave) / Will Retain (Stay).

## Mapping a Business Problem
When faced with a real-world problem, ask:
1.  **What are we predicting?** If it is a category or a choice, it is classification.
2.  **What data do we have?** These become your input features ($X$).

## Code Snippet: Exploring a Real-world Dataset
```python
from sklearn.datasets import load_breast_cancer
import pandas as pd

# Load data
cancer_data = load_breast_cancer()

# View features
df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
print(df.head()) # Shows features like mean radius, mean texture, etc.

# View target (0 = malignant, 1 = benign)
print(cancer_data.target[:5])
