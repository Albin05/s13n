## Lecture Script: Import And Use Custom Modules


---

### CS Theory Bite

> **Origin**: Custom modules implement **modular programming** (FORTRAN 1957, Modula-3 1980s). Python finds modules via **sys.path** — a search path checked in order: current directory → standard library → installed packages.
>
> **Analogy**: A custom module is like a **personal toolbox** — organize your favorite tools (functions) so you can carry them between projects.
>
> **Why it matters**: Modules prevent code duplication — write utility functions once, import everywhere.



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
