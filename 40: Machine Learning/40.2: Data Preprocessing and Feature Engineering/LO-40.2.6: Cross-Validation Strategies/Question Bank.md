# Question Bank: Cross-Validation

## Q1 (MCQ)
**Problem:** In Leave-One-Out Cross-Validation (LOOCV) on a dataset with $N$ samples, what is the size of the Training set in each iteration?
A. $N$
B. $N/2$
C. $N - 1$
D. $1$

## Q2 (Coding)
**Problem:** Write a Python snippet using `sklearn` to create a `StratifiedKFold` object with 3 splits. Then, iterate through `X` and `y` to print the indices of the train and test sets for each fold.
**Input:** Arrays `X` (10 rows), `y` (10 labels).
**Output:** Print indices.

## Q3 (NAT)
**Problem:** You perform 10-Fold Cross-Validation on a model. The 10 accuracy scores are: `[0.80, 0.82, 0.78, 0.81, 0.79, 0.85, 0.77, 0.83, 0.80, 0.81]`. What is the reported Mean Accuracy of the model?

## Q4 (MSQ)
**Problem:** Which of the following are benefits of Cross-Validation over a single Train-Test split?
A. It provides a better estimate of how the model will perform on unseen data.
B. It reduces the variance of the performance estimate.
C. It is computationally faster.
D. It allows every data point to be used for both training and testing (at different times).

## Q5 (Coding)
**Problem:** Implement "Leave-One-Out" manually. Write a loop that iterates through a list `data = [10, 20, 30]`. In each iteration, `test` is the current element, and `train` is the list of all other elements. Print `train` and `test`.

## Q6 (Subjective)
**Problem:** Explain the computational trade-off of K-Fold Cross-Validation. If training a Deep Neural Network takes 1 hour, and you want to perform 10-Fold CV, how long will it take? Is this always feasible?
