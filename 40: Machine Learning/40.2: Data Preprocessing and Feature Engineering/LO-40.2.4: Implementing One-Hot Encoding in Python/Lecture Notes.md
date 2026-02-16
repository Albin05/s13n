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
