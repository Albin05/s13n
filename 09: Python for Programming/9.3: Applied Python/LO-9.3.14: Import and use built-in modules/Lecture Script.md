## Lecture Script: Import And Use Built-In Modules

**Duration:** 12 minutes

---

### Hook (2 minutes)

Imagine rewriting math functions every project. Instead: `import math` — thousands of pre-built tools at your fingertips.

---

### Section 1: Basics (3 minutes)

```python
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.14159...

from random import randint
print(randint(1, 100))

import datetime
print(datetime.date.today())
```

---

### Section 2: Key Concepts (3 minutes)

**Import styles:**
```python
import math            # Full module
from math import sqrt  # Specific function
import math as m       # Alias
from math import *     # Everything (avoid!)
```

**Popular built-in modules:** math, random, datetime, os, sys, json, csv, pathlib, collections, itertools

---

### Section 3: Practical Usage (3 minutes)

```python
# Generate random password
import random, string
chars = string.ascii_letters + string.digits + string.punctuation
password = \'\'.join(random.choices(chars, k=12))
print(password)
```

---

### Summary (1 minute)

1. `import module` for full module access
2. `from module import function` for specific items
3. Key modules: math, random, datetime, os, json, pathlib
4. Explore with `dir(module)` and `help(module.function)`
