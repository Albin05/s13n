# Lecture Script: Understanding Labels and Predictions

## Topic Breakdown

### 1. Why do we distinguish them?
* **Instructor Note:** Ask students, "If you don't know the correct answer, can you grade a test?"
* **Why:** We cannot train a model without **Labels** (Supervised Learning). We cannot evaluate a model without comparing its **Predictions** to those Labels.

### 2. What are they?
* **Label ($y$):**
    * The "Target" variable.
    * Example: In a house price dataset, the column "Price" is the label.
    * *Note:* In the real world, getting labels is expensive (requires humans to tag images, doctors to diagnose X-rays).
* **Prediction ($\hat{y}$ or `y_hat`):**
    * The output of the mathematical function $f(x)$.
    * It is an *estimate*, never a guarantee.

### 3. How do we use them?
* **Training Phase:** We show the model both $x$ (Features) and $y$ (Label). The model adjusts itself to minimize the gap between $\hat{y}$ and $y$.
* **Inference Phase:** We only have $x$. The model generates $\hat{y}$. We *don't* know $y$ (that's why we need the model!).
* **Code Example:**
    Calculating the error between Truth and Guess.

    ```python
    # 1. THE LABELS (Truth)
    y_true = [100, 200, 300]

    # 2. THE PREDICTIONS (Model's Guess)
    y_pred = [110, 190, 300]

    # 3. THE ERROR (Difference)
    for t, p in zip(y_true, y_pred):
        error = t - p
        print(f"True: {t}, Pred: {p}, Error: {error}")
        # Output:
        # Error: -10 (Overshot)
        # Error: 10 (Undershot)
        # Error: 0 (Perfect)
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Visualizing Residuals](https://example.com/residuals-demo) - *Show the physical distance between the point (Label) and the line (Prediction).*
