# Lecture Script: Train-Test Split

## Topic Breakdown

### 1. Why do we split data?
* **Instructor Note:** Ask, "If I give you the exam questions beforehand, is it a fair test of your knowledge?"
* **Why:** We need to measure **Generalization**. If we train and test on the same data, the model can cheat by memorizing (Overfitting). We need a "Hold-out" set that the model has *never* seen to fairly evaluate its performance.

### 2. How does it work?
* **Mechanism:**
    * We shuffle the data randomly (to ensure the test set represents the whole dataset).
    * We slice it based on a ratio (e.g., 80% Train, 20% Test).
    * **Training Phase:** `model.fit(X_train, y_train)`
    * **Testing Phase:** `model.predict(X_test)` $\to$ Compare with `y_test`.
* **Important Parameters:**
    * `test_size`: Percentage to hold back (e.g., 0.2).
    * `random_state`: A seed value (e.g., 42) to ensure the random shuffle is the same every time we run the code (Reproducibility).
    * `stratify`: Ensures the Train and Test sets have the same proportion of classes (e.g., if 30% of data is "Cat", the test set should also be 30% "Cat").

### 3. How do we implement it?
* **Method:** We use `sklearn.model_selection.train_test_split`.
* **Code Example:**
    ```python
    from sklearn.model_selection import train_test_split
    import pandas as pd

    # Mock Data
    X = pd.DataFrame({'Age': [20, 30, 40, 50, 60], 'Salary': [20k, 30k, 40k, 50k, 60k]})
    y = [0, 0, 1, 1, 1] # Labels

    # The Split
    # random_state=42 ensures we get the same split every time
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"Train shapes: {X_train.shape}, {y_train.shape}")
    print(f"Test shapes: {X_test.shape}, {y_test.shape}")
    ```

* **Visual Aid:**
    !

* **Demo URL:**
    [Visualizing Data Splitting](https://scikit-learn.org/stable/visualizations.html)
