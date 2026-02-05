# ML Assignment 3

### Questions:

1. A website has trained a linear regression model to predict the amount of minutes that a user will
spend on the site. The formula they have obtained is
t = 0.8d + 0.5m + 0.5y + 0.2a + 1.5
where t is the predicted time in minutes, and d, m, y, and a are indicator variables (namely, they
take only the values 0 or 1) defined as follows:
    
    
    d is a variable that indicates if the user is on a desktop.
    m is a variable that indicates if the user is on a mobile device.
    y is a variable that indicates if the user is young (under 21 years old).
    a is a variable that indicates if the user is an adult (21 years old or older)
    
    If a user is 30 years old and on a desktop, then d = 1, m = 0, y = 0, and a = 1.
    If a 45-year-old user looks at the website from their phone, what is the expected time they will
    spend on the site?
    
2. Imagine that we trained a linear regression model in a medical dataset. The model predicts the expected lifespan of a patient. To each of the features in our dataset, the model would assign a
weight.
For the following quantities, state if you believe the weight attached to this quantity is a positive number, a negative number, or zero. 
    
    **Note:** if you believe that the weight is a very small number, whether positive or negative, you can say zero.
    
    1. Number of hours of exercise the patient gets per week 
    2. Number of cigarettes the patient smokes per week
    3. Number of family members with heart problems
    4. Number of siblings of the patient
    5. Whether or not the patient has been hospitalized
3. The following is a dataset of houses with sizes (in square feet) and prices (in dollars).

    
    ![Untitled](ML%20Assignment%203/Untitled.png)
    
    Suppose we have trained the model where the prediction for the price of the house based on size
    is the following:
    p = 2s + 50
    a. Calculate the predictions that this model makes on the dataset.
    b. Calculate the mean absolute error of this model.
    c. Calculate the root mean square error of this model.
    
4. What is linear regression and for which kind of data do we use this model?
5. What is the equation of the linear regression line?
6. Explain the slope and intercept in the linear regression equation.
7. If we increase the slope of a line in which direction the line moves (clockwise or anti-clockwise).
8. Explain the different evaluation metrics and their formula.
9. What is the difference between simple and multiple linear regression models?