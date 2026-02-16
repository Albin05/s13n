# Lecture Script: Cross-Validation Strategies

## Topic Breakdown

### 1. Why isn't Train-Test Split enough?
* **Instructor Note:** Draw a dataset with a cluster of "easy" points at the end. If we split 80/20 sequentially, the test set is just the easy points.
* **Why:** A single split is subject to **Variance**. The accuracy score depends heavily on *which* points ended up in the test set. Cross-Validation reduces this variance by testing on *every* point exactly once.

### 2. What are the strategies?
* **K-Fold CV:**
    * Split data into $K$ bins (usually 5 or 10).
    * Iteratively hold out one bin for testing.
    * *Pros:* Robust. *Cons:* Takes $K$ times longer to run.
* **Stratified K-Fold:**
    * Ensures each fold has the same percentage of samples for each class.
    * *Essential* for imbalanced datasets (e.g., 99% benign, 1% fraud).
* **Leave-One-Out (LOOCV):**
    * $K$ = Number of Rows. Train on all but one. Test on that one.
    * *Pros:* Max training data. *Cons:* Extremely slow.

### 3. How do we implement it?
* **Method:** `sklearn.model_selection.cross_val_score` handles the looping for us.
* **Code Example:**
    ```python
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression
    
    # 1. Setup Model and Data
    model = LogisticRegression()
    # X, y defined previously
    
    # 2. Run 5-Fold CV
    # This runs the training process 5 times!
    scores = cross_val_score(model, X, y, cv=5)
    
    print(f"Individual Scores: {scores}")
    print(f"Average Accuracy: {scores.mean():.2f}")
    ```

* **Visual Aid:**
    !

* **Demo URL:**
    [Scikit-Learn Cross-Validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)
