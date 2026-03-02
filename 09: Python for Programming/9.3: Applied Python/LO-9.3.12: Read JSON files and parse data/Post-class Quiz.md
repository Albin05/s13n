## Post-class Quiz: Read JSON Files

---

### 
What does `json.load()` accept?

A) A JSON string
B) A file object
C) A dictionary
D) A URL

**Correct Answer: B**

*Explanation: `json.load()` reads from a file object. Use `json.loads()` to parse a JSON string.*

---

### 
What Python type does a JSON object become?

A) list
B) tuple
C) dict
D) set

**Correct Answer: C**

*Explanation: JSON objects (key-value pairs in curly braces) become Python dicts.*

---

### 
What is the difference between `json.load()` and `json.loads()`?

A) No difference
B) `load` reads from file; `loads` parses a string
C) `loads` is faster
D) `loads` handles nested data

**Correct Answer: B**

---

### 
What exception does invalid JSON raise?

A) ValueError
B) json.JSONDecodeError
C) SyntaxError
D) TypeError

**Correct Answer: B**

*Explanation: Malformed JSON raises `json.JSONDecodeError`, which is a subclass of `ValueError`.*

---

### 
What JSON value becomes Python `None`?

A) `null`
B) `undefined`
C) `""`
D) `0`

**Correct Answer: A**

*Explanation: JSON `null` maps to Python `None`. `undefined` doesn't exist in JSON.*

---
