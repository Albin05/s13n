# Title: Introduction to Classification Problems - Editorials

## Problem Description (Q1)
Identify which of the following scenarios is a classification problem:
A. Predicting the price of a house based on square footage.
B. Forecasting the daily temperature for the next week.
C. Determining if an incoming email is "Spam" or "Not Spam".
D. Estimating the total sales revenue for the next quarter.

## Objective
To distinguish between regression (continuous output) and classification (discrete output) tasks.

## Hint
Look for the output variable. Is it a specific category/label or a continuous number?

## Short Explanation
Option C is the correct answer because the output is a discrete label (Spam/Not Spam). Options A, B, and D involve predicting continuous numerical values, which are regression problems.

## Detailed Explanation
In Supervised Learning, tasks are generally divided into Regression and Classification based on the nature of the target variable ($y$).
* **Regression:** The target variable is continuous (e.g., price, temperature, revenue).
* **Classification:** The target variable is categorical or discrete (e.g., Yes/No, Cat/Dog/Bird).

In Option C, the goal is to map an email to one of two categories. Therefore, it is a binary classification problem.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q2)
Given a dataset of patient records, we want to predict if a patient has diabetes (1) or not (0). What type of classification is this?

## Objective
To understand the definition of Binary Classification.

## Hint
Count the number of possible classes in the target variable.

## Short Explanation
This is a Binary Classification problem because there are only two possible outcomes: Diabetes (1) or No Diabetes (0).

## Detailed Explanation
Classification tasks can be categorized by the number of output classes:
1.  **Binary Classification:** The target has exactly two classes (e.g., 0 or 1, True or False).
2.  **Multi-class Classification:** The target has more than two classes (e.g., Red, Green, or Blue).

Since the problem specifies only two states (Diabetes/No Diabetes), it falls under Binary Classification.

## Constraints / Edge Cases
Edge cases include scenarios where the boundary is ambiguous, but technically, the label set remains binary.
