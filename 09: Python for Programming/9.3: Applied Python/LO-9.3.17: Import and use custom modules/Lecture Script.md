## Lecture Script: Import And Use Custom Modules

**Duration:** 12 minutes

---

### Hook (2 minutes)

Your main.py is 2000 lines long. Finding anything is a nightmare. Solution: split into modules — separate files for separate concerns.

---

### Section 1: Basics (3 minutes)

```python
# mymodule.py
def greet(name):
    return f"Hello, {{name}}!"

PI = 3.14159

# main.py
import mymodule
print(mymodule.greet("Alice"))
print(mymodule.PI)
```

---

### Section 2: Key Concepts (3 minutes)

**Package structure:**
```
mypackage/
    __init__.py    # Makes it a package
    utils.py
    models.py
    helpers.py
```

```python
from mypackage import utils
from mypackage.models import User
```

---

### Section 3: Practical Usage (3 minutes)

**The __name__ guard:**
```python
# utils.py
def helper():
    return "helping!"

if __name__ == "__main__":
    # Only runs when executed directly
    print(helper())
    # NOT when imported
```

---

### Summary (1 minute)

1. Any .py file is a module
2. Directories with __init__.py are packages
3. Use `if __name__ == "__main__"` for test code
4. Organize code into logical modules
