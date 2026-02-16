# Lecture Script: Introduction to Categorical Variables

## Topic Breakdown

### 1. Why is this a problem?
* **Instructor Note:** Ask a student to calculate "Red + Blue". They can't.
* **Why:** Computers are calculators. They need numbers. If you feed the string "Cat" into a Neural Network, it crashes. We *must* translate these text labels into numerical values.

### 2. What are the types?
* **Nominal (Names):**
    * Variables where order doesn't matter.
    * *Example:* "City". Is London > Paris? No.
    * *Processing:* We typically use **One-Hot Encoding** (creating new columns like `is_London`, `is_Paris`).
* **Ordinal (Order):**
    * Variables where rank matters.
    * *Example:* "Satisfaction". High > Medium > Low.
    * *Processing:* We typically use **Label Encoding** (Low=1, Med=2, High=3) to preserve the rank.

### 3. How do we detect them in code?
* **Method:** In Pandas, these often have the data type `object` (string) or `category`.
* **Code Example:**
    Identifying and checking types.

    ```python
    import pandas as pd

    data = {
        'City': ['Paris', 'London', 'Paris'],    # Nominal
        'Size': ['S', 'M', 'L'],                 # Ordinal
        'Price': [100, 200, 150]                 # Numerical (Not categorical)
    }
    df = pd.DataFrame(data)

    print(df.dtypes)
    # City      object (Categorical)
    # Size      object (Categorical)
    # Price     int64  (Numerical)

    print(df['City'].unique()) 
    # ['Paris' 'London']
    ```

* **Visual Aid:**
    !

* **Demo URL:**
    [Pandas Categorical Data Types](https://pandas.pydata.org/docs/user_guide/categorical.html)
