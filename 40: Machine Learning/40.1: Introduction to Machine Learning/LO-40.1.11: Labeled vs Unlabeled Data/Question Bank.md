# Question Bank: Labeled vs Unlabeled Data

## Q1 (MCQ)
**Problem:** You are building a spam filter. You have a dataset of 5,000 emails, where each email is marked as either "Spam" or "Not Spam". This dataset is:
A. Unlabeled
B. Reinforced
C. Labeled
D. Unstructured

## Q2 (Coding)
**Problem:** You are given a Python list of tuples. Each tuple contains a list of features and a string. Write a function that separates this into two lists: `X` (features) and `y` (labels).
**Input:** `[([1, 2], 'A'), ([3, 4], 'B')]`
**Output:** `X = [[1, 2], [3, 4]]`, `y = ['A', 'B']`

## Q3 (NAT)
**Problem:** A dataset has 100 rows. 20 rows have missing target values (labels). If we drop the rows with missing labels to perform Supervised Learning, how many rows of labeled data remain?

## Q4 (MSQ)
**Problem:** Which of the following scenarios involve **Unlabeled Data**?
A. Grouping customers by purchasing behavior without knowing customer segments beforehand.
B. Predicting if a transaction is fraudulent based on past known fraud cases.
C. Reducing the dimensionality of a dataset using PCA.
D. Training a neural network to recognize cats using a dataset of images with "Cat" tags.

## Q5 (Coding)
**Problem:** You have a dictionary of unlabeled data. Write a function to manually "label" the data based on a rule: if the value is greater than 50, label it 1, else label it 0. Return the new labeled list.
**Input:** `{'a': 45, 'b': 60, 'c': 10}`
**Output:** `[{'val': 45, 'label': 0}, {'val': 60, 'label': 1}, {'val': 10, 'label': 0}]`

## Q6 (Subjective)
**Problem:** A startup wants to build an AI to detect defects in manufacturing. They have 1 million images of products but no information on which ones are defective. Explain the problem they face regarding data types and propose a solution.
