# Lecture Script: Understanding Features and Feature Selection

## Topic Breakdown

### 1. Why do we need to select features?
* **Instructor Note:** Write "Garbage In, Garbage Out" on the board.
* **Why:** More data is not always better. Adding irrelevant features (noise) confuses the model.
    * **Curse of Dimensionality:** As features increase, data becomes sparse, and models need exponentially more data to learn.
    * **Overfitting:** The model learns patterns in the noise (e.g., "People named 'Bob' are more likely to crash cars" - a coincidence).
    * **Performance:** Fewer features = Faster training and inference.

### 2. What are the methods?
* **Filter Methods:**
    * *What:* Select features based on statistical scores (e.g., Correlation) *before* training the model.
    * *Pros:* Fast, model-agnostic.
    * *Cons:* Ignores interactions between features.
* **Wrapper Methods:**
    * *What:* Train the model with a subset of features, check accuracy, add/remove features, and repeat (e.g., RFE).
    * *Pros:* Finds the best subset for *that specific* model.
    * *Cons:* Very slow (computationally expensive).
* **Embedded Methods:**
    * *What:* The algorithm itself selects features during training (e.g., Lasso Regression).
    * *Pros:* Good balance of accuracy and speed.

### 3. How do we implement it?
* **Method:** We use statistical tests (ANOVA/Chi-Square) or model-based selection.
* **Code Example:**
    Removing low-variance features (features that are almost constant).

    ```python
    from sklearn.feature_selection import VarianceThreshold

    # Data: 
    # Col 1: Varied (Useful)
    # Col 2: Constant (Useless - everyone has value 1)
    X = [[0, 1, 0], 
         [0, 1, 1], 
         [1, 1, 0]]

    # Threshold 0: Remove columns with 0 variance (constants)
    selector = VarianceThreshold(threshold=0)
    X_new = selector.fit_transform(X)

    print(X_new)
    # Output: Column 2 is removed.
    ```

* **Visual Aid:**
    !

* **Demo URL:**
    [Feature Selection Playground](https://example.com/fs-playground)
