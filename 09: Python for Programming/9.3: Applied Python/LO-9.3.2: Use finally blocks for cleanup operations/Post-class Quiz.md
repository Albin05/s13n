## Post-class Quiz: Use finally Blocks for Cleanup

---

### Question 1
When does the `finally` block execute?

A) Only when no exception occurs
B) Only when an exception occurs
C) Always, regardless of exceptions
D) Only when the except block runs

**Correct Answer: C**

*Explanation: The finally block always executes — whether the try block succeeds, an exception is caught, or an uncaught exception propagates. This makes it ideal for cleanup.*

---

### Question 2
What is the output?

```python
try:
    print("A")
    raise ValueError("oops")
except ValueError:
    print("B")
finally:
    print("C")
```

A) A
B) A, B
C) A, B, C
D) A, C

**Correct Answer: C**

*Explanation: "A" prints in try. ValueError is raised and caught, so "B" prints. Finally always runs, so "C" prints.*

---

### Question 3
What is the primary use case for `finally`?

A) Catching exceptions
B) Resource cleanup (closing files, connections)
C) Printing error messages
D) Retrying failed operations

**Correct Answer: B**

*Explanation: finally is designed for cleanup code that must run regardless of success or failure — closing files, releasing database connections, stopping timers, releasing locks.*

---

### Question 4
Can you use `finally` without `except`?

A) No, except is required
B) Yes, try-finally is valid without except
C) Only in Python 3
D) Only with a return statement

**Correct Answer: B**

*Explanation: `try-finally` without `except` is valid. The finally block runs for cleanup, and any exception propagates normally after finally completes.*

---

### Question 5
What is the output?

```python
def test():
    try:
        return 1
    finally:
        print("cleanup")

result = test()
print(result)
```

A) Only `cleanup`
B) Only `1`
C) `cleanup` then `1`
D) `1` then `cleanup`

**Correct Answer: C**

*Explanation: Even though `return 1` is reached, the finally block runs before the function actually returns. So "cleanup" prints first, then the return value 1 is printed by the caller.*

---
