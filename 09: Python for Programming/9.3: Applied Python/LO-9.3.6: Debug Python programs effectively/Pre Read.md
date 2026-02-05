## Pre-Read: Debug Python Programs Effectively

**Duration:** 5 minutes

---

### Three Types of Errors

1. **Syntax** — code won't run at all (`SyntaxError`)
2. **Runtime** — code crashes mid-execution (`TypeError`, `ValueError`)
3. **Logic** — code runs but gives wrong answers (hardest!)

---

### Your Best Friend: The Traceback

```
Traceback (most recent call last):
  File "app.py", line 5, in calculate
    return x / y
ZeroDivisionError: division by zero
```

Read **bottom to top**: error first, then trace how you got there.

---

### Simplest Debug Tool: print()

```python
x = get_data()
print(f"DEBUG: x = {x}, type = {type(x)}")
```

---

### Try This

Find the bug:
```python
def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
        return count  # Bug! Where should this line be?
```
