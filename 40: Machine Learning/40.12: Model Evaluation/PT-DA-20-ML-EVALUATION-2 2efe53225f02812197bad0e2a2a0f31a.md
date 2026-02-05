# PT-DA-20-ML-EVALUATION-2

[Training_Data-:](https://drive.google.com/file/d/1MUgKLbcC-YXF-xZEB6pag6T1WMAOUD8u/view?usp=sharing)

[Testing_Data-:](https://drive.google.com/file/d/1OEtPkR-Ne65bXxtrohALyjCwKsWQ9yVr/view?usp=sharing)

1.  In column “**action_taken_name”** you have to convert it into 1 and 0 form so value “`Loan originated`"  should be converted into 1 and rest all to 0 and do change column name to “Loan Status”
2. Handle **Noise only** present in dataset:
    
    Note-: Some noise may look like **“ **%^9045*^&50 “** and here you have to get only first set of  digits like in this case you have to get only **9045.**
    
3. Remove columns which have more then **50% of Nulls** and after that **handle Null** for remaining and make sure not to drop rows. 
4. Get a visual presentation of distribution of different category in column “**state_name”**
5. Check multi collinearity and drop columns which has more then 70% 
6. Get the column name  which has 4th lowest correlation with “Loan status” 
7. Get the column name which has 8th highest correlation with “Loan status”
8. Perform Outlier Analysis (also get the percent of rows got removed if it’s more than 60% then don’t perform outlier analysis)  
9. Encode and Scale relevant columns
10. Create Logistic regression model with threshold of 0.5, 0.7 and 0.8
11. Get all metrics of logistic regression for each threshold.
12. You want to build a logistic regression model to predict whether a customer will purchase a product based on their age. Given the following data points:
Age: [25, 30, 35, 40, 45, 50, 55]
Purchased: [0, 1, 1, 0, 1, 1, 0]
Calculate the coefficients and intercept of the logistic regression model using maximum likelihood estimation. Then, use the model to predict the probability of a 47-year-old customer making a purchase