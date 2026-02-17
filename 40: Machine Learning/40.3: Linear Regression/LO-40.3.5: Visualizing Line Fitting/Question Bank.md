# Question Bank: Visualizing Line Fitting

## Q1 (MCQ)
**Problem:** Which of the following plots allows you to best visually assess if the Linear Regression assumption is valid (i.e., the data is actually linear)?
A. A Histogram of $x$ values.
B. A Residual Plot (Residuals vs $x$).
C. A Pie Chart of $y$ values.
D. A Box Plot of $y$.

## Q2 (Coding)
**Problem:** Write a Python function `plot_residuals(x, y, model)` using `matplotlib`. The function should scatter plot the data and draw vertical lines connecting each point to the model's prediction.
*Inputs:* `x` array, `y` array, `model` (linear equation function).

## Q3 (NAT)
**Problem:** You have a point at $(4, 10)$. Your regression line is $y = 2x + 1$. What is the **squared length** of the vertical residual line for this point?

## Q4 (MSQ)
**Problem:** Which of the following visual characteristics indicate a **Bad Fit**?
A. The residuals form a U-shape pattern when plotted against $x$.
B. The residuals are randomly distributed around 0.
C. The regression line passes through the mean of X and Mean of Y ($\bar{x}, \bar{y}$).
D. Several data points are very far from the line (Outliers) influencing the slope.

## Q5 (Coding)
**Problem:** Generate a plot that visualizes RSS.
1. Define 3 points.
2. Define a line $y=x$.
3. Calculate squared errors.
4. Plot the points, the line, and `fill_between` or draw squares to represent the error magnitude.

## Q6 (Subjective)
**Problem:** Explain why measuring the **Perpendicular Distance** (shortest path to the line) is different from measuring the **Vertical Distance** ($y - \hat{y}$). Why does Linear Regression use Vertical Distance? (Hint: Think about what we are trying to predict).
