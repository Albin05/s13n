# Implementing One-Hot Encoding in Python

## Concept
Knowing the theory of One-Hot Encoding (OHE) is essential, but implementing it correctly in a Machine Learning pipeline requires specific tools. In Python, there are two primary ways to perform OHE:

1.  **Pandas (`pd.get_dummies`):**
    * *Pros:* Extremely easy to use, returns a readable DataFrame immediately.
    * *Cons:* Does not "remember" the categories. If your training data has "Red" and "Blue", but your test data only has "Red", the resulting DataFrames will have different shapes, breaking your model.
2.  **Scikit-Learn (`OneHotEncoder`):**
    * *Pros:* Creates a transformer object that "learns" the categories from training data and applies exactly the same transformation to test data (handling errors or unknown categories gracefully).
    * *Cons:* Slightly more verbose syntax; output is often a NumPy array (requiring conversion back to DataFrame for readability).

## Real-World Scenario
Imagine building a model to predict house prices based on "City".
* **Training Data:** `[Paris, London]`
* **Test Data:** `[Paris, London, Tokyo]`
* **Pandas approach:** Will create columns `City_Paris`, `City_London`. It might crash on `Tokyo` or simply ignore it depending on how you code it.
* **Sklearn approach:** The encoder knows `Paris` and `London`. When it sees `Tokyo`, you can tell it to throw an error or encode it as all-zeros (handle_unknown='ignore').

## Visualization
![Image of diagram comparing pandas get_dummies vs sklearn OneHotEncoder workflow]

## External Resources
* [Documentation: Pandas get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
* [Documentation: Sklearn OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
