## Post-class Quiz: Raise Exceptions to Signal Errors

---

### Question 1
What does `raise ValueError("bad input")` do?

A) Prints "bad input" and continues
B) Stops execution and triggers a ValueError exception
C) Returns the string "bad input"
D) Creates a ValueError but doesn't trigger it

**Correct Answer: B**

*Explanation: `raise` immediately stops the current execution flow and triggers the specified exception. It can be caught by a try-except block or will crash the program if uncaught.*

---

### Question 2
When should you raise a `TypeError` vs a `ValueError`?

A) TypeError for wrong values, ValueError for wrong types
B) TypeError for wrong types, ValueError for wrong values
C) They are interchangeable
D) TypeError for user input, ValueError for code errors

**Correct Answer: B**

*Explanation: TypeError is for when the wrong type is provided (string instead of int). ValueError is for when the type is correct but the value is invalid (negative age, out-of-range score).*

---

### Question 3
What does bare `raise` (without arguments) do?

A) Raises a generic Exception
B) Does nothing
C) Re-raises the current exception
D) Syntax error

**Correct Answer: C**

*Explanation: Inside an except block, `raise` without arguments re-raises the exception that was just caught. This is useful when you want to log or modify state before letting the error propagate.*

---

### Question 4
What is wrong with this code?

```python
def get_item(lst, index):
    if index >= len(lst):
        return None
    return lst[index]
```

A) Nothing is wrong
B) It should raise IndexError instead of returning None
C) It should use try-except
D) It should return -1

**Correct Answer: B**

*Explanation: Returning None for an invalid index is a silent failure. The caller may use None thinking it's a valid value. Raising IndexError makes the error explicit and easier to debug.*

---

### Question 5
Which is the BEST error message?

A) `raise ValueError("Error")`
B) `raise ValueError("Invalid input")`
C) `raise ValueError(f"Age must be 0-150, got {age}")`
D) `raise ValueError("Something went wrong")`

**Correct Answer: C**

*Explanation: Good error messages include what was expected and what was received. Option C tells the developer exactly what the valid range is and what invalid value was provided, making debugging easy.*

---
