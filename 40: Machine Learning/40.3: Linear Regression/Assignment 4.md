# ML Assignment 4

**Dataset Link :**

[train_data](https://masai-course.s3.ap-south-1.amazonaws.com/editor/uploads/2023-03-07/train_data_978637.csv)

[test_data](https://masai-course.s3.ap-south-1.amazonaws.com/editor/uploads/2023-03-07/test_df_with_label_692652.csv)

According to the World Health Organisation (WHO), stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.

This dataset predicts whether a patient will likely get a stroke based on the input parameters like gender, age, and various diseases. Each row in the data provides relevant information about the patient.

**Questions:**

1. Find the null values in different columns. Do not drop the null values, fill it up with the appropriate values.
2. Check the data types of each column and change them accordingly. You can drop the noise values.
3. Find the 5-point summary of the numerical columns
4. Find the different unique values in each categorical column.
5. Create a correlation heatmap to check the correlation of different variables with each
other.
6. Plot histogram of ChestPainType, RestingECG, and heart disease
7. Plot distribution of Age, Cholesterol, and MaxHR.
8. Plot Pair plots of numerical variables.
9. Apply the scaling on numerical columns and encode the categorical ones.
10. Train the logistic regression model with the help of all given columns.
11. Check F score
12. Calculate precision and recall