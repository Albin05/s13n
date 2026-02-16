# Train-Test Split

## The Golden Rule
**NEVER** train on your Test data.
If the model sees the Test data during the learning phase, this is called **Data Leakage**. The evaluation metrics will be artificially high, but the model will fail in production.

## Standard Ratios
There is no fixed rule, but common splits are:
* **80/20:** Standard for medium datasets.
* **70/30:** When data is scarce.
* **90/10 or 99/1:** For massive datasets (Big Data), where even 1% is enough to test thoroughly.

## Key Terminology
1.  **X_train / y_train:** The features and labels used to build the model.
2.  **X_test / y_test:** The features and labels used to evaluate the model.
3.  **Random State:** A number that seeds the random number generator.
    * *Without it:* You get a different split every time (hard to debug).
    * *With it:* You get the exact same split every time (Reproducible).

## Stratification
If your dataset is imbalanced (e.g., 90% Healthy, 10% Sick):
* A random split might put *all* sick people in the Train set and none in the Test set.
* **Stratified Split:** Forces the Test set to also have 10% Sick people.
* Code: `train_test_split(..., stratify=y)`

## Visual Summary
!
