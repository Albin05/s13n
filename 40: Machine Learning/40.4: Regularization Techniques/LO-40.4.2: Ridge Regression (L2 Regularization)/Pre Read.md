# Ridge Regression (L2 Regularization)

## Concept
**Ridge Regression** is a variation of Linear Regression that includes **L2 Regularization**.
* **Standard Regression:** Minimizes the *Error* (MSE).
* **Ridge Regression:** Minimizes the *Error* + a **Penalty** based on the *square of the weights*.

$$Cost = \text{MSE} + \lambda \sum_{j=1}^{p} w_j^2$$

## What does it do?
It forces the model to keep the weights ($w$) as small as possible.
* If a weight is large (e.g., $w=100$), the penalty is huge ($100^2 = 10,000$).
* The model prefers to have many small weights (e.g., all $w \approx 1$) rather than one huge weight. This reduces the model's sensitivity to any single feature, preventing overfitting.

## Real-World Analogy: The Group Project
Imagine a team of 5 people working on a project.
* **Standard Regression:** One "Superstar" does 99% of the work ($w_1 = 99$), and the others do nothing ($w_{2-5} = 0$). If the Superstar gets sick (noise in that feature), the project fails.
* **Ridge Regression:** The teacher creates a rule that punishes anyone doing too much. The workload gets distributed evenly ($w_{1-5} \approx 20$). If one person gets sick, the project still succeeds. This is a robust model.

## Visualization


## External Resources
* [Article: Ridge Regression Explained](https://example.com/ridge-regression)
* [Video: L1 vs L2 Regularization](https://example.com/l1-l2-video)
