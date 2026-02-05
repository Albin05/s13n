## Post-class Quiz: Write Data to JSON Files

---

### Question 1
What does `json.dump()` vs `json.dumps()` do?

A) No difference
B) `dump` writes to file; `dumps` returns a string
C) `dumps` is faster
D) `dump` only works with dicts

**Correct Answer: B**

---

### Question 2
What does `indent=2` do in `json.dump()`?

A) Limits output to 2 lines
B) Adds 2 spaces of indentation for readability
C) Adds 2 tabs
D) Nothing

**Correct Answer: B**

---

### Question 3
What Python types can be serialized to JSON?

A) Only dicts and lists
B) dicts, lists, strings, numbers, bools, None
C) Any Python object
D) Only strings

**Correct Answer: B**

*Explanation: JSON supports dicts, lists, strings, ints, floats, bools, and None. Custom objects need a custom encoder.*

---

### Question 4
What does `sort_keys=True` do?

A) Sorts list values
B) Sorts dictionary keys alphabetically in the output
C) Sorts by value
D) Raises error if keys aren't sortable

**Correct Answer: B**

---

### Question 5
How do you update an existing JSON file?

A) Use append mode "a"
B) Read the file, modify the data, write it back
C) Use json.update()
D) JSON files can't be updated

**Correct Answer: B**

*Explanation: JSON files must be read entirely, modified in Python, then written back. There's no append or partial update for JSON.*

---
