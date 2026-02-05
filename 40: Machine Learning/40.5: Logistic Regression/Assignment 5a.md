# ML Assignment 5

### Part A:

**Questions:**

1. For a simple linear regression model, the equation is given by y = b0 + b1*x. If the value of b0 is 4 and the value of b1 is 3, what is the predicted value of y for x=2?
2. Consider a multiple linear regression model with three independent variables x1, x2, and x3. The coefficients for these variables are given by b1=2, b2=3, and b3=4, respectively. What is the equation of the regression model?

### Part B:

**Dataset: [Link](https://drive.google.com/file/d/19nDmAwb1knmCeOX8jlyx6TGJ8qDN-3iu/view?usp=share_link)**

**Questions:**

1. Perform EDA on the dataset and remove the noise and the null values.
2. Create a new column named “Company-Name” which you will get from column “NAME” (Only get company name not model number / name)
3. Drop the columns which are redundant and irrelevant.
4. Create a correlation heatmap to check the correlation of different variables with each
other.
5. Create a scatter plot of the target variable (price) against the variable "engine size”
6. Do outlier analysis and remove the outliers from different columns.
7. Do the scaling of the data accordingly.
8. Split the data in train and test and train a linear regression model to predict the price based on the given variables.
9. Calculate the mean squared error (MSE), root mean squared error (RMSE),
R-squared score, and adjusted R-squared score of the model. Find the training as well as testing accuracy.
10. Interpret the results of the evaluation metrics and comment on the performance of
the linear regression model.