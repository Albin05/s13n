# Title: Multi-class Classification Strategies - Editorials

## Problem Description (Q1)
What is the core principle behind the **One-vs-Rest (OvR)** (also known as One-vs-All) strategy for multi-class classification?
A. It trains a single model to predict all classes simultaneously using a specialized cost function.
B. It trains $K$ separate binary classifiers for a $K$-class problem, each distinguishing one class from all other classes.
C. It trains a binary classifier for every possible pair of classes.
D. It randomly groups classes into two macro-classes and performs binary classification.

## Objective
To understand the architectural approach of the One-vs-Rest strategy.

## Hint
If you have classes A, B, and C, how would you isolate A using a binary model?

## Short Explanation
Option B is correct. The OvR strategy splits a multi-class problem into multiple independent binary classification problems.

## Detailed Explanation
Standard Logistic Regression is inherently binary; it separates data into two groups. To handle multiple classes (e.g., Red, Green, Blue) using OvR, we train a separate binary classifier for each class:
1.  Classifier 1: Red vs. [Green, Blue]
2.  Classifier 2: Green vs. [Red, Blue]
3.  Classifier 3: Blue vs. [Red, Green]
For a dataset with $K$ classes, we train exactly $K$ binary models. During prediction, we run the new data point through all $K$ models and select the class whose model outputs the highest probability.

## Constraints / Edge Cases
OvR can suffer from class imbalance. For example, in a 10-class problem where each class has 100 samples, the "Red vs. Rest" model will be trained on 100 positive samples and 900 negative samples.

---

## Problem Description (Q2)
If a dataset contains 7 distinct classes, how many individual binary classification models are trained when using the **One-vs-One (OvO)** strategy?
A. 7
B. 14
C. 21
D. 49

## Objective
Differentiate between OvR and OvO strategies mathematically.

## Hint
OvO creates a model for every possible pair of classes. The formula for combinations is $\frac{N(N-1)}{2}$.

## Short Explanation
Option C is correct. OvO trains a model for every unique pair, resulting in 21 models for 7 classes.

## Detailed Explanation
Unlike One-vs-Rest (which trains $K$ models), One-vs-One (OvO) trains a binary classifier for every possible pair of classes. The number of models is given by the combination formula $\frac{K(K-1)}{2}$. 
For $K = 7$:
$$\frac{7(7-1)}{2} = \frac{42}{2} = 21$$
While this results in many more models, each model is trained on a much smaller subset of the data (only the data belonging to the two classes being compared), which can be faster for certain algorithms like Support Vector Machines.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q3)
Which of the following are characteristics of the **Multinomial** (Softmax) approach to multi-class Logistic Regression? (Select all that apply)
A. It trains $K$ completely independent binary models.
B. It utilizes the Softmax activation function instead of the Sigmoid function.
C. The predicted probabilities across all $K$ classes are guaranteed to sum to exactly $1.0$.
D. It relies on the Cross-Entropy loss function generalized for multiple classes.

## Objective
Identify the properties of a true multinomial logistic model.

## Hint
Multinomial Logistic Regression is an integrated model, not a meta-strategy of combining separate models.

## Short Explanation
Options B, C, and D are correct. Multinomial logistic regression uses the Softmax function to jointly optimize the probabilities so they always sum to $1$.

## Detailed Explanation
Instead of hacking binary regression to handle multiple classes (like OvR does), Multinomial Logistic Regression upgrades the math directly:
* **B & C:** It replaces the Sigmoid function with the **Softmax** function. Softmax takes the raw scores for all $K$ classes and normalizes them into a unified probability distribution, ensuring that $P(Class 1) + P(Class 2) + \dots + P(Class K) = 1.0$.
* **D:** To train this joint model, it uses Categorical Cross-Entropy loss.
* **A is incorrect** because it trains a single, unified model with a weight matrix, rather than independent binary models.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q4)
Explain why the individual probabilities predicted by the $K$ models in a One-vs-Rest (OvR) strategy might not sum to exactly $1.0$, whereas the outputs of a Softmax function always do.

## Objective
Contrast the independent nature of OvR probabilities with the joint distribution of Softmax.

## Hint
Are the binary models in OvR aware of each other during training?

## Short Explanation
OvR trains independent models that do not communicate, so their probabilities are not normalized against each other. Softmax normalizes the scores jointly in a single mathematical operation.

## Detailed Explanation
In a **One-vs-Rest** setup, if you have 3 classes (A, B, C), you train 3 separate logistic regression models. Model A calculates the probability of A vs. Not A entirely independently of Model B. Because they don't share a denominator or a normalization step, Model A might output 0.6, Model B might output 0.5, and Model C might output 0.2. The sum is 1.3. (We simply pick the highest value, 0.6, as the prediction).
In contrast, the **Softmax** function calculates the exponentials of all class scores and divides each by the sum of all exponentials. This mathematically forces the outputs to act as a joint probability distribution that strictly sums to $1.0$.

## Constraints / Edge Cases
N/A

---

## Problem Description (Q5)
Write a Python snippet using `scikit-learn` to train a Logistic Regression model on a multi-class dataset `X_train`, `y_train` strictly using the Multinomial (Softmax) strategy, overriding the default behavior.

## Objective
Implement multi-class strategy configurations in `scikit-learn`.

## Hint
Check the `multi_class` parameter in the `LogisticRegression` initialization.

## Short Explanation
You must explicitly set the `multi_class` parameter to `'multinomial'` when instantiating the model.

## Detailed Explanation
```python
from sklearn.linear_model import LogisticRegression

# To force the use of the Softmax/Multinomial approach:
# We also specify a solver that supports multinomial loss, like 'lbfgs'
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')

# Fit the model to the multi-class training data
model.fit(X_train, y_train)

# Predict probabilities (these will sum to 1 for each sample)
probabilities = model.predict_proba(X_test)
