# Pre-Read: Import Built-in Modules

## Python's Standard Library

Python comes with many built-in modules:

```python
import math
print(math.sqrt(16))  # 4.0

import random
print(random.randint(1, 10))  # Random number 1-10

import datetime
print(datetime.datetime.now())  # Current date/time
```

## Common Modules

- **math**: Mathematical functions
- **random**: Random numbers
- **datetime**: Dates and times
- **os**: Operating system interface
- **json**: JSON data
- **csv**: CSV files

## How to Import

```python
# Import entire module
import math
math.sqrt(16)

# Import specific function
from math import sqrt
sqrt(16)

# Import with alias
import datetime as dt
dt.datetime.now()
```
