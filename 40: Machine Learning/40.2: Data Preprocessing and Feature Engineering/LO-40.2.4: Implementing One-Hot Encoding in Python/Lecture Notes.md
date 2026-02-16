# Implementing One-Hot Encoding

## Method 1: Pandas `get_dummies`
Best for: Quick analysis, data cleaning, visualization.

```python
import pandas as pd

# Load data
df = pd.DataFrame({'Fruit': ['Apple', 'Banana', 'Apple']})

# Encode
# columns=['Fruit']: Specific column to encode
# prefix='F': Naming convention (F_Apple, F_Banana)
# drop_first=True: Avoid multicollinearity
df_encoded = pd.get_dummies(df, columns=['Fruit'], prefix='F', drop_first=True)
```
## Method 2: Scikit-Learn OneHotEncoder
Best for: Production ML pipelines, consistency between Train/Test sets.

```python
from sklearn.preprocessing import OneHotEncoder

# Setup
# sparse_output=False: Return numpy array instead of sparse matrix (easier to read)
# handle_unknown='ignore': If test data has new categories, set all columns to 0
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Training Data (Fit & Transform)
X_train = [['Male', 1], ['Female', 3], ['Male', 2]]
X_train_encoded = ohe.fit_transform(X_train)

# Test Data (Transform Only - DO NOT FIT)
X_test = [['Female', 1], ['Unknown', 2]]
X_test_encoded = ohe.transform(X_test)
