# Multi-class Classification Strategies

## Conceptual Explanation
Standard Logistic Regression is a **binary** classifier. It answers a Yes/No question: "Is this email Spam or Not Spam?" 

But what if we need to categorize an image as a Cat, Dog, or Bird? This is a **multi-class** problem. We cannot use a single standard binary Logistic Regression model to separate three or more distinct groups. 

To solve this, Machine Learning practitioners use two primary strategies:
1.  **One-vs-Rest (OvR):** Also known as One-vs-All. We break the multi-class problem into multiple binary problems. For 3 classes (Cat, Dog, Bird), we train 3 separate models:
    * Model 1: Is it a Cat, or is it something else?
    * Model 2: Is it a Dog, or is it something else?
    * Model 3: Is it a Bird, or is it something else?
    To make a prediction, we run the image through all three models and pick the one with the highest confidence.
2.  **Multinomial (Softmax):** Instead of building separate models, we upgrade the math of Logistic Regression. We replace the Sigmoid function with the **Softmax function**, which evaluates all classes simultaneously and outputs a probability distribution where all probabilities perfectly add up to $1.0$.

## Short Examples
* **OvR:** An email system wants to tag emails as "Work", "Personal", or "Promotions". It runs three separate binary filters behind the scenes to decide the best tag.
* **Softmax:** A weather app uses a single multinomial model that outputs: 70% chance of Sun, 20% chance of Clouds, 10% chance of Rain. (Sum = 100%).

## External Links
* [Scikit-learn: Multiclass Classification](https://scikit-learn.org/stable/modules/multiclass.html)

