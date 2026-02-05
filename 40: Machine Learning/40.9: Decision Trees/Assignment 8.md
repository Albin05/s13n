# ML Assignment 8

## Part A:

**Dataset Links:**

[train.csv](https://masai-course.s3.ap-south-1.amazonaws.com/editor/uploads/2023-03-09/train_220348.csv)

[test.csv](https://masai-course.s3.ap-south-1.amazonaws.com/editor/uploads/2023-03-09/test_with_label_791460.csv)

**Questions:**

1. Find and deal with the null values in different columns.
2. Check the data types of each column and change them accordingly.
3. Create a new column “duration” that would be the sum of values of column “Fever since” and “Headche”
4. Find the 5-point summary of the numerical columns
5. Find the different unique values in each categorical column.
6. Create a correlation heatmap to check the correlation of different variables with each
other.
7. Do outlier analysis and remove the outliers from different columns.
8. Apply the scaling on numerical columns and encode the categorical ones.
9. Train the logistic regression model with the help of all given columns.
10. Create a confusion matrix.
11. Create a Classification report.

## **Part - B**

1. In the following spam-detection decision tree model, determine whether an email from your
mom with the subject line, “Please go to the store, there’s a sale,” will be classified as spam.

![Untitled](ML%20Assignment%208/Untitled.png)

1. Our goal is to build a decision tree model to determine whether credit card transactions are
fraudulent. We use the dataset of credit card transactions below, with the following features:
• Value: value of the transaction.
• Approved vendor: the credit card company has a list of approved vendors. This variable
indicates whether the vendor is in this list.

| Transaction | Value | Approved vendor | Fraudulent |
| --- | --- | --- | --- |
| Transaction 1 | 100 | Not approved | Yes |
| Transaction 2 | 100 | Approved | No |
| Transaction 3 | 10,000 | Approved | No |
| Transaction 4 | 10,000 | Not approved | Yes |
| Transaction 5 | 5,000 | Approved | Yes |
| Transaction 6 | 100 | Approved | No |

Build the first node of the decision tree by computing GI(Gini Impurity).