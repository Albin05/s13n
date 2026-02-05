## Post-class Quiz: Handle Multiple Exception Types

---

### Question 1
What is the correct order for except blocks?

A) General exceptions first, specific last
B) Specific exceptions first, general last
C) Order doesn't matter
D) Only one except block is allowed

**Correct Answer: B**

*Explanation: Python checks except blocks top to bottom. If a general exception (like Exception) comes first, it catches everything, and specific handlers below it never run.*

---

### Question 2
What does `except (ValueError, TypeError) as e:` do?

A) Catches ValueError OR TypeError with the same handler
B) Catches only when both occur simultaneously
C) Syntax error
D) Catches ValueError, ignores TypeError

**Correct Answer: A**

*Explanation: Parentheses group multiple exception types. Either ValueError OR TypeError will be caught by this single handler. The matched exception is bound to `e`.*

---

### Question 3
When does the `else` block run in try-except-else?

A) Always
B) When an exception occurs
C) When NO exception occurs in the try block
D) Before the try block

**Correct Answer: C**

*Explanation: The else block runs only when the try block completes without raising any exception. If any exception occurs (even if caught), else is skipped.*

---

### Question 4
What is the output?

```python
try:
    x = int("abc")
except ValueError:
    print("A")
except Exception:
    print("B")
finally:
    print("C")
```

A) A, C
B) B, C
C) A, B, C
D) Only C

**Correct Answer: A**

*Explanation: `int("abc")` raises ValueError. The first matching except (ValueError) runs, printing "A". Since ValueError is already caught, the Exception handler is skipped. Finally always runs, printing "C".*

---

### Question 5
Why is catching bare `Exception` as the LAST except block acceptable?

A) It's never acceptable
B) After specific handlers, it acts as a safety net for unexpected errors
C) It's faster than specific exceptions
D) Python requires it

**Correct Answer: B**

*Explanation: Placing `except Exception` last (after specific handlers) catches any unexpected errors that weren't anticipated. This prevents crashes while still handling known errors specifically.*

---
