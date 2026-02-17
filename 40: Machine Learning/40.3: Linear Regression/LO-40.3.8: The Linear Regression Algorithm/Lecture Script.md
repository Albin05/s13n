# Lecture Script: The Linear Regression Algorithm

## Topic Breakdown

### 1. Putting it all together
* **Instructor Note:** Draw the three pillars on the board: Model ($y=wx+b$), Cost ($J$), Optimizer ($\nabla$).
* **Why:** The algorithm isn't magic. It's just these three math equations talking to each other in a loop.
    * The **Model** makes a prediction.
    * The **Cost** judges the prediction.
    * The **Optimizer** fixes the Model based on the judgment.

### 2. The Algorithm Steps
* **Initialization:** $w=0, b=0$. (Or random).
* **Forward Pass:** Compute $\hat{y} = wx + b$.
* **Loss Computation:** Compute $J = \frac{1}{n}\sum(y - \hat{y})^2$.
* **Backward Pass (Gradient):**
    * $\frac{\partial J}{\partial w} = \frac{-2}{n} \sum x(y - \hat{y})$
    * $\frac{\partial J}{\partial b} = \frac{-2}{n} \sum (y - \hat{y})$
* **Update Step:**
    * $w = w - \alpha \cdot \frac{\partial J}{\partial w}$
    * $b = b - \alpha \cdot \frac{\partial J}{\partial b}$

### 3. Implementing the Class
* **Method:** We will write a Python class that looks like Scikit-Learn's.
* **Code Example:**
    ```python
    import numpy as np

    class SimpleLinearRegression:
        def __init__(self, learning_rate=0.01, epochs=1000):
            self.lr = learning_rate
            self.epochs = epochs
            self.w = 0
            self.b = 0
            
        def fit(self, X, y):
            n = len(y)
            for _ in range(self.epochs):
                # 1. Forward Pass
                y_pred = self.w * X + self.b
                
                # 2. Compute Gradients
                dw = (-2/n) * np.sum(X * (y - y_pred))
                db = (-2/n) * np.sum(y - y_pred)
                
                # 3. Update Parameters
                self.w -= self.lr * dw
                self.b -= self.lr * db
                
        def predict(self, X):
            return self.w * X + self.b

    # Usage
    model = SimpleLinearRegression()
    model.fit(np.array([1, 2, 3]), np.array([2, 4, 6]))
    print(f"Slope: {model.w}, Intercept: {model.b}")
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Linear Regression Visualization](https://www.geogebra.org/m/cCkgwzjZ)
