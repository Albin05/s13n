## Post-class Quiz: Debug Python Programs Effectively

---

### Question 1
How should you read a Python traceback?

A) Top to bottom
B) Bottom to top — error first, then trace the calls
C) Only the last line matters
D) Only the first line matters

**Correct Answer: B**

*Explanation: The last line shows the error type and message. Lines above show the call chain from most recent to oldest, helping you trace how the program reached the error.*

---

### Question 2
What does `assert x > 0, "must be positive"` do?

A) Always prints "must be positive"
B) Raises AssertionError if x <= 0
C) Sets x to a positive value
D) Does nothing

**Correct Answer: B**

*Explanation: `assert` checks the condition. If False, it raises AssertionError with the given message. If True, it does nothing. It's a quick way to validate assumptions.*

---

### Question 3
What is the bug in this code?

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

A) `append` is wrong
B) Mutable default argument — the list persists between calls
C) Missing return statement
D) No bug

**Correct Answer: B**

*Explanation: Default mutable arguments (like `[]`) are created once and shared across all calls. Each call modifies the same list. Fix: use `items=None` and create a new list inside.*

---

### Question 4
Which is the best debugging strategy for a long function?

A) Rewrite the entire function
B) Add print statements everywhere
C) Binary search — add a print in the middle, narrow down which half has the bug
D) Delete the function and start over

**Correct Answer: C**

*Explanation: Binary search debugging is efficient. Check the midpoint: if values are correct there, the bug is in the second half. This logarithmically narrows down the bug location.*

---

### Question 5
What does `breakpoint()` do?

A) Stops the program permanently
B) Drops into an interactive debugger (pdb)
C) Prints all variables
D) Creates a backup of the code

**Correct Answer: B**

*Explanation: `breakpoint()` pauses execution and opens the Python debugger (pdb), where you can inspect variables, step through code line by line, and evaluate expressions interactively.*

---
