
# Lecture Notes: The Linear Regression Algorithm

## The Iterative Approach (Gradient Descent)
Most modern ML libraries (TensorFlow, PyTorch) use this approach because it scales to massive datasets.

**Pseudocode:**
```text
Initialize weights randomly
Repeat until convergence:
    1. Calculate Predictions (y_hat)
    2. Calculate Error (y - y_hat)
    3. Calculate Gradient (Slope of error)
    4. Update Weights (w = w - learning_rate * gradient)

```

## The Analytical Approach (Normal Equation)

For Linear Regression specifically, there is a closed-form solution that finds the perfect  and  instantly without loops or learning rates.


**Comparison:**
| Feature | Gradient Descent | Normal Equation |
| :--- | :--- | :--- |
| **Speed** | Fast for large  | Slow for large  (Matrix Inversion is ) |
| **Hyperparameters** | Learning Rate (), Epochs | None |
| **Feature Scaling** | **Required** | Not Required |
| **Usage** | Deep Learning, Big Data | Small Statistical Models |

## Key Assumptions of Linear Regression

To trust the results, your data must meet these criteria:

1. **Linearity:** The relationship between  and  is actually linear.
2. **Independence:** Observations are independent of each other.
3. **Homoscedasticity:** The variance of error is constant across all .
4. **Normality:** The residuals (errors) are normally distributed.

