# Lecture Script: Deriving the Logistic Regression Equation

## Topic: Building the Final Model

### Why (Importance)
Up until now, we have looked at disconnected mathematical puzzle pieces. We know lines fail for classification. We know Sigmoid squishes numbers. We know exponents kill negative values. Now, we must assemble these pieces into a single, cohesive equation. This equation is the engine of Logistic Regression, and understanding it is mandatory for writing the code that powers neural networks and classification algorithms.

### What (Concept)
In Machine Learning, a "hypothesis" $h_\theta(x)$ is the function our model uses to make predictions. 
For Linear Regression, the hypothesis was simple: $h_\theta(x) = \theta^T x$.
For Logistic Regression, we wrap that linear hypothesis inside the Sigmoid function $g(z)$.

Therefore:
$$h_\theta(x) = g(\theta^T x)$$

Substituting the Sigmoid formula:
$$h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$$

**Interpretation:**
What does this equation actually output? It outputs a probability. Specifically:
$$h_\theta(x) = P(y=1 | x ; \theta)$$
Read as: "The probability that the target $y$ equals $1$, given the features $x$, parameterized by the weights $\theta$."

### How (Method / Example)
Let's walk through the end-to-end mathematical pipeline using an example. 
Imagine we are predicting if a student passes ($y=1$) based on hours studied ($x_1$).
Assume our trained weights are: $\theta_0 = -10$ (bias) and $\theta_1 = 2$.
Student studies for $6$ hours ($x_1 = 6$).

**Step 1: Compute the linear combination ($z$)**
$$z = \theta_0 + \theta_1 x_1$$
$$z = -10 + 2(6) = -10 + 12 = 2$$
The linear model predicts a score of $2$.

**Step 2: Apply the Sigmoid function**
$$h_\theta(x) = \frac{1}{1 + e^{-2}}$$
$$h_\theta(x) = \frac{1}{1 + 0.135}$$
$$h_\theta(x) = \frac{1}{1.135} \approx 0.88$$

**Step 3: Interpret and Threshold**
The model outputs $0.88$. This means there is an $88\%$ probability the student will pass.
If our decision threshold is $0.5$, since $0.88 \ge 0.5$, we officially classify this student as Class $1$ (Pass).

### URLs for Demos
* [Interactive Logistic Regression Demo](https://ml-playground.com/)
