 # Lecture Script: Regularization in Practice

## Topic Breakdown

### 1. The Hidden Trap: Scaling
* **Instructor Note:** Write two features on the board: $x_1$ (0 to 1), $x_2$ (0 to 1,000,000).
* **Ask:** "To predict $y=10$, which weight needs to be bigger?"
    * $w_1 \approx 10$ vs $w_2 \approx 0.00001$.
* **The Problem:** The Regularization term $\lambda w^2$ sees $10^2 = 100$ and $0.00001^2 \approx 0$. It will aggressively shrink $w_1$ (the important feature) and ignore $w_2$.
* **The Fix:** **Standardization**. $z = \frac{x - \mu}{\sigma}$. Now both features range roughly from -3 to +3. The weights will be on the same scale.

### 2. Workflow: The Pipeline
* **Concept:** In Scikit-Learn, we never run regularization manually. We use a **Pipeline**.
    * Step 1: `StandardScaler`
    * Step 2: `Ridge` / `Lasso`
* **Why:** This prevents Data Leakage (calculating mean/std on test data) and ensures scaling happens automatically.

### 3. Choosing Alpha ($\lambda$)
* **Method:** We don't guess. We search.
* **Code Example:**
    ```python
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import RidgeCV
    import numpy as np

    # Data (Unscaled)
    X = np.array([[1, 1000], [2, 2000], [3, 3000]])
    y = np.array([2, 4, 6])

    # The Correct Way: Pipeline with Cross-Validation
    # alphas: The list of lambda values to try
    model = make_pipeline(
        StandardScaler(), 
        RidgeCV(alphas=[0.1, 1.0, 10.0])
    )

    model.fit(X, y)
    
    # Accessing the best alpha found
    best_alpha = model.named_steps['ridgecv'].alpha_
    print(f"Best Alpha: {best_alpha}")
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Scikit-Learn Pipeline Guide](https://scikit-learn.org/stable/modules/compose.html)
