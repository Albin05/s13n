# Question Bank: Categorical Variables

## Q1 (MCQ)
**Problem:** Which encoding technique creates a new binary column for every unique category in a feature?
A. Label Encoding
B. Ordinal Encoding
C. One-Hot Encoding
D. Frequency Encoding

## Q2 (Coding)
**Problem:** You have a list of categories: `['Low', 'Medium', 'High', 'Medium', 'Low']`. Write a function using a Python dictionary to map these to `1, 2, 3` respectively.
**Input:** The list.
**Output:** `[1, 2, 3, 2, 1]`.

## Q3 (NAT)
**Problem:** A dataset has a categorical feature "City" with 5 unique values (New York, Paris, London, Tokyo, Berlin). If we use **One-Hot Encoding** on this feature, how many *new* columns will be added to the dataset? (Assume we do not drop the first category).

## Q4 (MSQ)
**Problem:** Which of the following are examples of **Nominal** variables?
A. Zip Code.
B. Review Rating (1-5 stars).
C. Dog Breed (Poodle, Bulldog, Beagle).
D. Education Level (High School, PhD).

## Q5 (Coding)
**Problem:** Using Pandas, write a snippet to check the number of unique values (cardinality) in a column named `'Category'` of dataframe `df`.
**Input:** `df` with column `'Category'`.
**Output:** An integer.

## Q6 (Subjective)
**Problem:** Explain why "Zip Code" (e.g., 90210, 10001) is technically a Categorical variable, even though it looks like a number. Why might treating it as a standard numerical variable (like Age or Price) be a mistake?
