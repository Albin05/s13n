# Editorials

## Q1
### Title
Diagnosing High Bias

### Problem Description
Both training and validation errors are high.

### Objective
Identify symptoms of Underfitting.

### Hint
If the student fails the practice test AND the real test, did they study enough?

### Short Explanation
High error on both datasets means the model hasn't learned the patterns at all. This is Underfitting.

### Detailed Explanation
* **Underfitting:** High Bias. The model is too simple to capture the underlying structure of the data. Result: Poor performance everywhere.
* **Overfitting:** High Variance. Good performance on Train, bad on Test.
* **Answer:** B (Underfitting).

---

## Q2
### Title
Detecting Overfitting Logic

### Problem Description
Check for large gap between training and test error.

### Objective
Implement a programmatic check for overfitting.

### Hint
Compare the two error values against the thresholds provided.

### Short Explanation
Check `if train_err < 0.05 and test_err > 0.20`.

### Detailed Explanation
```python
def check_overfitting(train_err, test_err):
    if train_err < 0.05 and test_err > 0.20:
        print("Overfitting")
    else:
        print("Normal")
```
Q3
Title

Generalization Gap Calculation

Problem Description

Calculate the change in the gap between Train and Test accuracy.
Initial: Train 100, Test 60.
Final: Train 90, Test 75.

Objective

Quantify the improvement in generalization.

Hint

Gap = Train - Test. Calculate Initial Gap, Final Gap, then the difference.

Short Explanation

Initial Gap: 40. Final Gap: 15. Difference: 25.

Detailed Explanation

Initial Gap: 100%−60%=40%

Final Gap: 90%−75%=15%

Decrease: 40−15=25 percentage points.

Q4
Title

Prevention Techniques

Problem Description

Select methods to stop Overfitting.

Objective

Identify regularization and validation strategies.

Hint

Anything that simplifies the model or checks its performance on unseen data helps.

Short Explanation

A, B, and C are correct. D (adding noise) can sometimes help but is not a standard "technique" in the same way; usually, we want clean data. (Though data augmentation is a valid technique, "adding noise" blindly is risky).

Detailed Explanation

A (True): Cross-validation helps assess generalization.

B (True): Regularization penalizes complex models.

C (True): Pruning simplifies decision trees.

D (False/Debatable): While noise injection is a technique, in this context, we usually want more data, not just noise.

Q5
Title

Model Diagnosis Function

Problem Description

Classify model state based on accuracy scores.

Objective

Translate definitions into conditional logic.

Hint

Follow the if/else logic exactly as described.

Short Explanation

Standard conditional checks.

Detailed Explanation

Python
def diagnose_model(train_score, test_score):
    if train_score < 0.6:
        return "Underfitting"
    elif train_score > 0.9 and test_score < 0.7:
        return "Overfitting"
    else:
        return "Good Fit"
Q6
Title

Bias-Variance Tradeoff

Problem Description

Explain the relationship between Complexity, Bias, and Variance.

Objective

Connect the concepts of Over/Underfitting to statistical theory.

Hint

Simple models assume too much (Bias). Complex models vary too much (Variance).

Short Explanation

Underfitting = High Bias (Too assumptions). Overfitting = High Variance (Too sensitive).
+1

Detailed Explanation

Bias: The error introduced by approximating a real-world problem with a simplified model. High Bias → Underfitting.

Variance: The error introduced by the model's sensitivity to small fluctuations in the training set. High Variance → Overfitting.

Tradeoff: As we increase complexity, Bias decreases (model fits better) but Variance increases (model becomes unstable). We must find the optimal balance.
