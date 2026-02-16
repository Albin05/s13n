# Lecture Script: Implementing One-Hot Encoding

## Topic Breakdown

### 1. The Easy Way: Pandas `get_dummies`
* **Instructor Note:** Start by creating a simple DataFrame with a categorical column.
* **Why:** Quick data exploration.
* **Code:**
    ```python
    import pandas as pd
    
    df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green']})
    
    # Simple OHE
    encoded_df = pd.get_dummies(df, columns=['Color'])
    print(encoded_df)
    # Columns: Color_Blue, Color_Green, Color_Red
    ```
* **Limitation:** What if we get a new color 'Yellow' in production? `get_dummies` won't know what to do if it wasn't in the original dataframe, or worse, it will create `Color_Yellow` which the model doesn't expect.

### 2. The Robust Way: Sklearn `OneHotEncoder`
* **Why:** For building reproducible pipelines. We split operations into `fit` (learn categories) and `transform` (apply encoding).
* **Code:**
    ```python
    from sklearn.preprocessing import OneHotEncoder
    
    # 1. Instantiate (handle_unknown='ignore' prevents crashes on new categories)
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    
    train_data = [['Red'], ['Blue']]
    test_data = [['Red'], ['Yellow']] # Yellow is unseen!
    
    # 2. Fit on Training Data
    encoder.fit(train_data)
    
    # 3. Transform Training Data
    print(encoder.transform(train_data))
    # [[0, 1], [1, 0]] (Assuming alphabetical: Blue, Red)
    
    # 4. Transform Test Data
    print(encoder.transform(test_data))
    # [[0, 1], [0, 0]] -> Yellow became [0, 0] (All zeros)
    ```

### 3. Handling the Dummy Variable Trap
* **Method:**
    * **Pandas:** `pd.get_dummies(..., drop_first=True)`
    * **Sklearn:** `OneHotEncoder(..., drop='first')`
* **Visual Aid:**
    ![Image of code snippet output showing dropped first column in one-hot encoding]

* **Demo URL:**
    [Sklearn OHE Interactive Guide](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)
