# Regression vs Classification

## Comparative Table

| Feature | Regression | Classification |
| :--- | :--- | :--- |
| **Goal** | Predict a continuous value (Quantity). | Predict a discrete label (Category). |
| **Output** | Numerical (Integer/Float). | Categorical (String/Int ID). |
| **Ordering** | Output has natural order ($2.5 < 5.0$). | Output categories may not have order (Cat vs Dog). |
| **Visualization** | Line of Best Fit. | Decision Boundary. |
| **Key Algorithms** | Linear Regression, Decision Tree Regressor. | Logistic Regression, KNN Classifier, SVM. |
| **Evaluation** | Mean Squared Error (MSE), $R^2$. | Accuracy, Confusion Matrix, AUC-ROC. |

## Important Note on Logistic Regression
Despite the name, **Logistic Regression** is a **Classification** algorithm. It is named "Regression" because it estimates the *probability* (a continuous number between 0 and 1) of a class, but it is used to classify inputs.

## Hybrid Problems
Some problems can be framed as both:
* **Age Prediction:**
    * *Regression:* Predict exact age (24.5 years).
    * *Classification:* Predict age group (Child, Adult, Senior).

## Visual Summary
[Image of diagram illustrating input data going into two different boxes labeled Regression and Classification with different outputs]
