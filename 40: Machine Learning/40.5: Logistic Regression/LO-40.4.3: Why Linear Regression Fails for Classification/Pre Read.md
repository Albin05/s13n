# Why Linear Regression Fails for Classification

## Conceptual Explanation
If classification is just mapping features to a $0$ or $1$, it might seem logical to use the tool we already know: Linear Regression. We could just fit a line to the data points and say, "If the predicted $y$ is greater than $0.5$, it belongs to Class $1$. Otherwise, Class $0$."

However, this approach suffers from two massive mathematical flaws:
1.  **Unbounded Outputs:** Probabilities must be between $0$ and $1$. A straight line extends to infinity. A Linear Regression model will happily predict that a data point has a "$250\%$ chance" of being Class $1$, or a "$-40\%$ chance", which makes no mathematical sense.
2.  **Sensitivity to Outliers:** Linear Regression uses Mean Squared Error (MSE), which heavily penalizes points far from the line. If a massive outlier is added to Class $1$, the line will tilt drastically to accommodate it. This tilt shifts the $0.5$ decision boundary, causing normal, previously correct points to suddenly be misclassified.

## Short Examples
* **The Outlier Problem:** Imagine a tumor classification model (size vs. malignancy). It works perfectly for tumors between $1cm$ and $5cm$. Suddenly, a massive $20cm$ malignant tumor is added to the dataset. The linear regression line flattens out to minimize the error for this $20cm$ tumor. As a result, the model now misclassifies $4cm$ tumors as benign, even though it got them right before.

## External Links
* [Why Linear Regression is not suitable for Classification](https://towardsdatascience.com/why-linear-regression-is-not-suitable-for-classification-cd724ddaae40)

## Visuals
*(Refer to S3 bucket for diagrams showing the regression line shifting due to an outlier, and the line crossing the $y=0$ and $y=1$ boundaries)*
