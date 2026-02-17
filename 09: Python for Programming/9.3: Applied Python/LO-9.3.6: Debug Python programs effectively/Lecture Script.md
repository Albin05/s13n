## Lecture Script: Debug Python Programs Effectively


---

### CS Theory Bite

> **Origin**: The term "bug" dates to **Grace Hopper** (1947) who found an actual moth in the Harvard Mark II computer. Debuggers evolved from **LISP** (1960s) to **GDB** (1986) to Python's **pdb** (1992).
>
> **Analogy**: Debugging is like **detective work** — gather evidence (error messages), form hypotheses, test them systematically.
>
> **Why it matters**: You'll spend more time debugging than writing code — systematic debugging skills are essential.



### Hook (2 minutes)

Every programmer spends significant time debugging. The difference between a junior and senior developer isn't that seniors write bug-free code — it's that they find bugs faster.

```
Traceback (most recent call last):
  File "app.py", line 42, in process
    result = data[key] / total
ZeroDivisionError: division by zero
```

Can you fix this in 10 seconds? After today, yes.

---

### Section 1: Reading Tracebacks (3 minutes)

```
Traceback (most recent call last):
  File "main.py", line 15, in <module>
    run()
  File "main.py", line 10, in run
    process(data)
  File "utils.py", line 5, in process
    return int(value)
ValueError: invalid literal for int()
```

**Read bottom to top:**
1. `ValueError` — the error
2. `utils.py:5` — where it happened
3. `main.py:10` → `main.py:15` — how we got there

---

### Section 2: Print Debugging (3 minutes)

```python
def find_average(numbers):
    print(f"DEBUG input: {numbers}")
    total = sum(numbers)
    print(f"DEBUG total: {total}")
    count = len(numbers)
    avg = total / count
    print(f"DEBUG avg: {avg}")
    return avg
```

Quick, works everywhere, no tools needed.

---

### Section 3: Assert Statements (2 minutes)

```python
def withdraw(balance, amount):
    assert balance >= 0, f"Negative balance: {balance}"
    assert amount > 0, f"Invalid amount: {amount}"
    assert amount <= balance, "Insufficient funds"
    return balance - amount
```

Asserts document assumptions and catch violations immediately.

---

### Section 4: Common Bugs (3 minutes)

**Off-by-one:** `range(5)` gives `0,1,2,3,4` not `1,2,3,4,5`

**Mutable defaults:**
```python
def f(lst=[]):     # BUG: shared across calls
def f(lst=None):   # FIX: create new list each time
    lst = lst or []
```

**Type confusion:** `input()` returns string, not int

**Early return in loop:**
```python
for x in items:
    if condition:
        count += 1
    return count  # BUG: indented inside loop — returns on first iteration!
```

---

### Section 5: breakpoint() (1 minute)

```python
breakpoint()  # Drops into pdb
# n = next, p var = print, c = continue, q = quit
```

---

### Summary (1 minute)

1. Read tracebacks bottom-to-top
2. Print debugging for quick checks
3. Assert for assumptions
4. Know common bug patterns
5. Simplify, check assumptions, binary search
