
# Editorials

## Q1
### Title
Feature Correlation

### Problem Description
Identify the most predictive feature for spam.

### Objective
Understand Feature Importance.

### Hint
Which attribute is unique to spam? Almost all emails (spam or not) contain "the" or are sent on Tuesdays.

### Short Explanation
"Wire Transfer" + "Unknown Sender" is a very strong indicator of a scam/spam. The other options are common in normal emails too.

### Detailed Explanation
* **A ("the"):** Appears in 100% of English emails. Zero predictive power.
* **B (Length):** Both spam and normal emails can be long. Weak predictor.
* **C (Context):** High correlation with financial scams. Strong predictor.
* **D (Day):** Spam is sent every day. Weak predictor.

---

## Q2
### Title
Caps Lock Feature

### Problem Description
Calculate the ratio of uppercase letters.

### Objective
Implement a specific feature extractor.

### Hint
Count uppercase chars and divide by total length.

### Short Explanation
Iterate through the string, check `isupper()`.

### Detailed Explanation
```python
def get_caps_ratio(text):
    if len(text) == 0: return 0
    upper_count = sum(1 for char in text if char.isupper())
    return upper_count / len(text)

```

---

## Q3

### Title

Matrix Dimensions

### Problem Description

Calculate total cells in a Feature Matrix.
Rows (Emails): 50
Columns (Features): 10

### Objective

Understand the shape of ML data structures.

### Hint

Rows  Columns.

### Short Explanation

.

### Detailed Explanation

The dataset is a matrix (table).

* **Height:** Number of samples (50).
* **Width:** Number of features (10).
* **Total values:** .

---

## Q4

### Title

Valid Features

### Problem Description

Select relevant attributes for car pricing.

### Objective

Distinguish signal from noise.

### Hint

Does the attribute affect the value?

### Short Explanation

A, B, and C affect the price. D (Dog's name) is irrelevant noise.

### Detailed Explanation

* **A (Color):** Red cars might cost more/less. Relevant.
* **B (Mileage):** High mileage lowers price. Very Relevant.
* **C (Age):** Older cars are cheaper. Very Relevant.
* **D (Dog):** Completely unrelated to the car's value.

---

## Q5

### Title

Banned Word Counter

### Problem Description

Count occurrences of keywords in text.

### Objective

Feature extraction based on vocabulary.

### Hint

Loop through banned words and use `text.count()`.

### Short Explanation

Standard string search.

### Detailed Explanation

```python
def count_banned(text):
    text = text.lower()
    banned = ['win', 'free', 'money']
    count = 0
    for word in banned:
        count += text.count(word)
    return count

```

---

## Q6

### Title

Garbage In, Garbage Out

### Problem Description

Explain the impact of poor feature selection.

### Objective

Highlight the critical role of features.

### Hint

The model only knows what you show it.

### Short Explanation

If the features (Input) do not contain the information needed to make a decision (Signal), the model (Output) will fail, no matter how smart the algorithm is.

### Detailed Explanation

* **The Concept:** A model is a mathematical function that maps Inputs  Outputs.
* **The Scenario:** If you only give the model the "First Letter" of an email, it tries to predict Spam based on whether the email starts with 'H' or 'W'. Since both spam and normal emails start with these letters, the model cannot distinguish them.
* **Result:** The model is effectively guessing. The quality of the output is limited by the quality of the input features.

```

```
