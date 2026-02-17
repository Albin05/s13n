# Lecture Script: Regression vs Classification

## Topic Breakdown

### 1. Why do we need to distinguish them?
* **Instructor Note:** Ask the class, "If I want to predict if a student passes or fails, is that the same math as predicting their exact score out of 100?"
* **Why:** The math changes completely.
    * **Regression** minimizes "Distance" (Error).
    * **Classification** maximizes "Probability" or "Separation" (Accuracy).
    * You cannot use Mean Squared Error to evaluate a Cat/Dog classifier!

### 2. What are the key differences?
* **Output Type:**
    * Regression $\to$ Continuous Number ($-\infty$ to $+\infty$).
    * Classification $\to$ Discrete bucket (Class A, Class B).
* **Evaluation Metrics:**
    * Regression $\to$ MSE, MAE, $R^2$.
    * Classification $\to$ Accuracy, Precision, Recall, F1-Score.
* **Visual Geometry:**
    * Regression $\to$ A line fitting *through* the data.
    * Classification $\to$ A line separating the data *between* classes (Decision Boundary).

### 3. How do we code them?
* **Method:** In libraries like Scikit-Learn, we use different classes (e.g., `LinearRegression` vs `LogisticRegression`).
* **Code Example:**
    ```python
    # 1. REGRESSION (Predicting a number)
    # Input: Years Experience -> Output: Salary
    reg_model.fit(X, y_numbers)
    print(reg_model.predict([[5]])) 
    # Output: [50000.50] (Continuous)

    # 2. CLASSIFICATION (Predicting a class)
    # Input: Hours Studied -> Output: Pass(1)/Fail(0)
    clf_model.fit(X, y_classes)
    print(clf_model.predict([[5]])) 
    # Output: [1] (Discrete)
    ```

* **Visual Aid:**
    [Image of side-by-side plots: Regression fit line vs Classification separation line]

* **Demo URL:**
    [Playground: Classification vs Regression](https://playground.tensorflow.org/) - *Toggle between "Classification" and "Regression" modes to see how the output changes.*
