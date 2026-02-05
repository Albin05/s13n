## Post-class Quiz: Handle Exceptions Using try-except Blocks

---

### Question 1
What happens when an exception occurs inside a `try` block?

A) The program crashes immediately
B) Python jumps to the matching `except` block
C) Python ignores the error
D) The `try` block restarts

**Correct Answer: B**

*Explanation: When an exception occurs in a `try` block, Python stops executing the `try` block and looks for a matching `except` block. If found, it executes that handler. The program then continues after the try-except structure.*

---

### Question 2
What is the output?

```python
try:
    x = int("abc")
    print("Success")
except ValueError:
    print("Error caught")
print("Done")
```

A) `Success` then `Done`
B) `Error caught` then `Done`
C) Only `Error caught`
D) Only `Done`

**Correct Answer: B**

*Explanation: `int("abc")` raises ValueError. Python skips `print("Success")` and jumps to the except block, printing "Error caught". Then "Done" prints because it's after the entire try-except structure.*

---

### Question 3
Which catches BOTH ValueError and TypeError?

A) `except ValueError, TypeError:`
B) `except (ValueError, TypeError):`
C) `except ValueError or TypeError:`
D) `except [ValueError, TypeError]:`

**Correct Answer: B**

*Explanation: Multiple exception types must be in a tuple: `except (ValueError, TypeError)`. Option A is Python 2 syntax. Options C and D are invalid syntax.*

---

### Question 4
When does the `else` block execute?

A) Always
B) Only when an exception occurs
C) Only when NO exception occurs
D) Before the `try` block

**Correct Answer: C**

*Explanation: The `else` block runs only if the `try` block completes without raising any exception. If an exception occurs and is caught, `else` is skipped.*

---

### Question 5
Why should you avoid bare `except:` (without specifying an exception type)?

A) It's a syntax error
B) It catches ALL exceptions, hiding bugs
C) It's slower
D) It doesn't catch anything

**Correct Answer: B**

*Explanation: A bare `except:` catches everything, including `KeyboardInterrupt` and `SystemExit`. This can hide real bugs and make debugging impossible. Always catch specific exception types.*

---
