# In-class Quiz: Linear Regression's Failure

## Question 1
Why does an outlier cause severe problems when using Linear Regression for binary classification?
A. It causes the model to output strings instead of numbers.
B. It pulls the regression line, shifting the decision threshold and causing misclassifications of normal points.
C. It forces the output to be strictly between 0 and 1.
D. It automatically changes the target variables to continuous values.

## Question 2
If we use a Linear Regression model $h_\theta(x)$ to predict probabilities for a classification task, which mathematical rule is violated?
A. Probabilities must be independent.
B. Probabilities must be strictly bounded between 0 and 1.
C. Probabilities must follow a normal distribution.
D. Probabilities cannot be calculated from continuous features.

## Question 3
If you train a Linear Regression model on binary data ($y \in \{0, 1\}$) and input an extremely large feature value, what is the model most likely to output?
A. Exactly 1.0
B. A value greater than 1.0
C. Exactly 0.5
D. NaN (Not a Number)
