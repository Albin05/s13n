# Question Bank: Labels and Predictions

## Q1 (MCQ)
**Problem:** In a dataset of emails used for spam detection, the column containing "Spam" or "Not Spam" is known as the:
A. Feature Vector
B. Attribute
C. Target / Label
D. Prediction

## Q2 (Coding)
**Problem:** Write a function `calculate_mae(y_true, y_pred)` that calculates the Mean Absolute Error.
Formula: $\frac{1}{n} \sum |y_{true} - y_{pred}|$
**Input:** `y_true = [10, 20]`, `y_pred = [12, 18]`
**Output:** `2.0`

## Q3 (NAT)
**Problem:** You have 100 predictions.
* 80 predictions matched the label exactly.
* 20 predictions did not match.
What is the Accuracy of the model in percentage?

## Q4 (MSQ)
**Problem:** Which of the following statements about **Labels** are true?
A. Labels are required for Supervised Learning.
B. Unsupervised Learning algorithms (like Clustering) do not require labels.
C. Labels are always numerical.
D. Obtaining labels can be the most expensive part of an ML project.

## Q5 (Coding)
**Problem:** You are building a checker. Write a function `check_accuracy(predictions, labels)` that returns the percentage of matches.
**Input:** `preds = ['A', 'B', 'A']`, `labels = ['A', 'A', 'A']`
**Output:** `66.66` (or `0.66`)

## Q6 (Subjective)
**Problem:** Explain the difference between "Training Accuracy" and "Test Accuracy" in terms of Labels. Why might a model have high accuracy when comparing Predictions to Training Labels, but low accuracy when comparing Predictions to Test Labels?
