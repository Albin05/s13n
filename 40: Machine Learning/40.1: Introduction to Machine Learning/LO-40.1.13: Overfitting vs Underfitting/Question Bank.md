# Question Bank: Overfitting vs Underfitting

## Q1 (MCQ)
**Problem:** You are training a linear regression model. You notice that both your training error and validation (test) error are very high. What is the most likely diagnosis?
A. The model is overfitting.
B. The model is underfitting.
C. You need more data points.
D. The learning rate is too low.

## Q2 (Coding)
**Problem:** You have a function `get_error(model, data)` that returns the error rate. Write a script that checks if a model is overfitting. Assume overfitting if Training Error is < 0.05 and Test Error is > 0.20. Print "Overfitting" or "Normal".

## Q3 (NAT)
**Problem:** A decision tree has a training accuracy of 100% and a test accuracy of 60%. If we prune the tree (reduce complexity) and the test accuracy increases to 75%, by how many percentage points did the generalization gap (Train Acc - Test Acc) decrease? (Assume Train Acc drops to 90%).

## Q4 (MSQ)
**Problem:** Which of the following techniques are commonly used to prevent **Overfitting**?
A. Cross-Validation.
B. Regularization (L1/L2).
C. Pruning (for Decision Trees).
D. Adding more noise to the training data.

## Q5 (Coding)
**Problem:** Implement a function `diagnose_model(train_score, test_score)` where scores are between 0 and 1 (higher is better).
* If `train_score < 0.6`: return "Underfitting"
* If `train_score > 0.9` and `test_score < 0.7`: return "Overfitting"
* Else: return "Good Fit"

## Q6 (Subjective)
**Problem:** Explain the concept of the "Bias-Variance Tradeoff" in relation to Overfitting and Underfitting. How does increasing model complexity affect Bias and Variance?
