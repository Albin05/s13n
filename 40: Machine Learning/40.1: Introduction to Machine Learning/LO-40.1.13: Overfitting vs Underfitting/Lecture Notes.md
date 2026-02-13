# Overfitting vs Underfitting

## Key Definitions
* **Generalization:** The ability of a model to perform well on new, unseen data.
* **Noise:** Random variations in data that do not represent the true pattern.
* **Signal:** The true underlying pattern in the data.

## Comparison Table

| Feature | Underfitting | Overfitting | Good Fit |
| :--- | :--- | :--- | :--- |
| **Complexity** | Too Low | Too High | Balanced |
| **Training Error** | High | Extremely Low | Low |
| **Testing Error** | High | High | Low |
| **Analogy** | "Clueless" | "Memorizer" | "Learner" |
| **Solution** | Increase complexity, Add features | Decrease complexity, Regularize, More data | N/A |

## The "Goldilocks" Zone
We want a model that is "just right."
1.  **Too Simple:** Fails to capture the trend.
2.  **Too Complex:** Captures the noise.
3.  **Just Right:** Captures the trend, ignores the noise.

## Visualizing Error Curves
* As model complexity increases, **Training Error** always goes down.
* **Testing Error** goes down initially, hits a minimum (Sweet Spot), and then starts going up again (Overfitting).
