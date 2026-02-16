# Lecture Script: One-Hot Encoding Theory

## Topic Breakdown

### 1. Why do we need this specific encoding?
* **Instructor Note:** Show a dataset with "City": Paris, London, Tokyo. Ask students if they should map them to 1, 2, 3.
* **Why:** If we use 1, 2, 3 (Label Encoding), the model interprets this mathematically: $Tokyo (3) > Paris (1)$. It might try to average them ($Average = London (2)$). This is nonsense for Nominal data. We need a representation that treats all categories equally.

### 2. What is One-Hot Encoding?
* **Definition:** A process that transforms a single categorical variable with $N$ unique categories into $N$ binary features (0 or 1).
* **Mechanism:**
    * Identify all unique values.
    * Create a new column for each value.
    * Mark 1 if the row belongs to that value, 0 otherwise.
* **The Dummy Variable Trap:**
    * If we have `Is_Male` and `Is_Female`, we typically only need one column. If `Is_Male` is 0, we *know* `Is_Female` is 1. Including both introduces **Multicollinearity** (redundancy).
    * Solution: Drop the first column ($N-1$ columns).

### 3. How do we implement it?
* **Method:** We use `pandas.get_dummies()` or `sklearn.OneHotEncoder`.
* **Code Example:**
    ```python
    import pandas as pd

    data = {'Color': ['Red', 'Green', 'Red', 'Blue']}
    df = pd.DataFrame(data)

    # 1. Standard One-Hot Encoding
    ohe_df = pd.get_dummies(df, columns=['Color'])
    print(ohe_df)
    # Result:
    #    Color_Blue  Color_Green  Color_Red
    # 0           0            0          1
    # 1           0            1          0
    
    # 2. Avoiding Dummy Variable Trap (Drop First)
    ohe_trap_free = pd.get_dummies(df, columns=['Color'], drop_first=True)
    # Result has only 2 columns. If both are 0, it implicitly means the dropped category.
    ```

* **Visual Aid:**
    !

* **Demo URL:**
    [Pandas get_dummies documentation](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
