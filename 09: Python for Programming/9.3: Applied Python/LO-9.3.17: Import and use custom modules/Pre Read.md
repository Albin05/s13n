## Pre-Read: Import And Use Custom Modules


---

### What Is a Module?

Any Python file is a module. You can import functions from one file into another:

```python
# helpers.py
def greet(name):
    return f"Hello, {{name}}!"

# main.py
from helpers import greet
print(greet("Alice"))
```

---

### Key Points

- Any .py file = a module
- Import with `import filename` (without .py)
- Use `from module import function` for specific items
