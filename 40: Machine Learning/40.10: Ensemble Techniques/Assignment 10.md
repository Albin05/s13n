# ML Assignment 10

### **Part A :**

**Questions:** 

1. Use the below data (outlook, temperature, humidity, and wind as the features and the class label plays which has two values yes or no. Based on the given 4 features a child goes out to play or not) and find out the Gini index for each of the four features and based on the Gini values select the feature that will be used to make the first split.

![Untitled](ML%20Assignment%2010/Untitled.png)

1. List down the advantages & disadvantages of the Decision Trees.
2. Consider a binary classification problem with two classes: "spam" and "not spam". You have a dataset of 500 emails, of which 200 are spam and 300 are not spam. Calculate the Gini index for this dataset.
3. You are training a decision tree model on a dataset of 1000 customer records, where each record has two features: age (in years) and income (in thousands of dollars), and the target variable is "customer churn" (yes or no). You decide to split the data on the age feature using a threshold of 30 years. After splitting the data, you have 600 records in the left subtree and 400 records in the right subtree. Of the 600 records in the left subtree, 400 are non-churners and 200 are churners. Of the 400 records in the right subtree, 150 are non-churners and 250 are churners. Calculate the Gini index for each of the two subtrees.

### Part B:

**Dataset: [Link](https://docs.google.com/spreadsheets/d/1wCGmH7X1ez-Ny-3b8qQpPWeBraE1WAnSwrZ36XkkWEE/edit?usp=sharing)**

Given a dataset of children with kyphosis(a spinal condition) who underwent an operation. The dataset has the following columns:

- Kyphosis: whether or not the kyphosis was present after the operation.
- Age: age of children in months
- Number: number of vertebrae involved in the operation
- Start: the topmost vertebrae number involved in the operation.

Use 70% of the data for training and the rest for testing. Use Decision Tree Classifier model and make predictions for the test data. Also, evaluate the model.