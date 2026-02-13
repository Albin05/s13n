# Understanding Features

## Definition
A **Feature** (or variable/attribute) is an individual measurable property of the data. In a dataset table, rows are examples, and columns are **Features**.

## The Spam Detection Example
To train a model to detect spam, we transform raw text into numerical inputs.

| Raw Email | Feature 1: `has_money` | Feature 2: `num_caps` | Feature 3: `bad_sender` | Label |
| :--- | :--- | :--- | :--- | :--- |
| "Hi mom..." | 0 | 0 | 0 | Not Spam |
| "WIN MONEY!!!" | 1 | 10 | 1 | **Spam** |
| "Meeting at 5" | 0 | 1 | 0 | Not Spam |

## Types of Features
1.  **Numerical:** Direct numbers (e.g., Length of email, Number of recipients).
2.  **Categorical:** Discrete groups (e.g., Sender Domain: `gmail.com`, `yahoo.com`, `sketchy.net`).
3.  **Binary:** True/False (e.g., Contains attachment?).

## Importance of Feature Selection
Not all data is useful.
* **Noise:** Features that don't help predict the target (e.g., the timestamp of the email might be irrelevant).
* **Signal:** Features that strongly correlate with the target (e.g., specific keywords).

## Visual Summary
