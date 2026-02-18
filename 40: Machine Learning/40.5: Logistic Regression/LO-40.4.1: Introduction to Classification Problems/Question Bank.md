# Question Bank: Introduction to Classification Problems

## Section A: Multiple Choice Questions (MCQs)

**Q1.** Which of the following best describes the output of a classification algorithm?
A. A continuous value representing a quantity.
B. A discrete class label or category.
C. A cluster of similar data points without labels.
D. A probability distribution over infinite values.

**Q2.** Which of the following is an example of **Multi-class Classification**?
A. Detecting if an email is Spam or Not Spam.
B. Predicting if it will rain tomorrow (Yes/No).
C. Identifying if a handwritten digit is 0, 1, 2, ..., or 9.
D. Estimating the price of a second-hand car.

---

## Section B: Multiple Select Questions (MSQs)

**Q3.** Select all scenarios that represent a **Classification** problem.
A. Predicting the credit score (300-850) of a bank customer.
B. Predicting if a bank customer will default on a loan (Default/No Default).
C. Categorizing news articles into "Sports", "Politics", or "Technology".
D. Forecasting the exact temperature for the next 5 days.
E. Diagnosing a patient with "Type A", "Type B", or "No" disease.

---

## Section C: Short Answer Questions

**Q4.** Define **Binary Classification** in one sentence and provide one real-world example.

**Q5.** What is the primary difference between the target variable ($y$) in Regression versus Classification?

---

## Section D: Long Answer / Application Questions

**Q6.** You are given a dataset containing details of 1,000 houses (Square footage, Number of bedrooms, Location, Year built).
* **Case A:** You want to predict the market price of the house.
* **Case B:** You want to predict if the house will be sold within 30 days (Yes) or not (No).

Explain which machine learning task (Regression or Classification) applies to Case A and Case B, and justify your answer based on the nature of the output variable.

---

## Section E: Implementation Tasks

**Q7.** Write a Python function `classify_student(score)` that acts as a simple threshold-based classifier.
* **Input:** `score` (float between 0 and 100).
* **Logic:** If the score is 40 or above, return class "Pass". If below 40, return class "Fail".
* **Output:** The predicted class label.
