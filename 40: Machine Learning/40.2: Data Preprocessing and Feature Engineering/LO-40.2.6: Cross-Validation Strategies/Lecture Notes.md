# Cross-Validation Strategies

## K-Fold Cross Validation
* **Process:** Split dataset into $K$ consecutive folds. Each fold is used once as a validation while the $K-1$ remaining folds form the training set.
* **Result:** We get $K$ accuracy scores. We report the Mean ($\mu$) and Standard Deviation ($\sigma$).
* **Common K:** 5 or 10.

## Stratified K-Fold
* **Problem with standard K-Fold:** Random splitting might result in a fold with zero samples of a minority class.
* **Solution:** Stratification enforces the class distribution in each split matches the original dataset.
* **Use Case:** Classification problems, especially imbalanced ones.

## Leave-One-Out (LOOCV)
* **Process:** For a dataset size $N$, we create $N$ folds. Each fold has size 1.
* **Use Case:** Very small datasets (e.g., < 50 rows) where we can't afford to waste 20% for testing.
* **Cost:** Very high computation ($N$ training runs).

## Time Series Split
* **Constraint:** We cannot peek into the future. We cannot train on 2024 data to predict 2023.
* **Process:**
    * Fold 1: Train [Jan], Test [Feb]
    * Fold 2: Train [Jan, Feb], Test [Mar]
    * Fold 3: Train [Jan, Feb, Mar], Test [Apr]
* **Key:** The training set *grows*, and the test set is always *after* the training set.

## Visual Summary
!
