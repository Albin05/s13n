## Pre-Read: Read JSON Files

**Duration:** 5 minutes

---

### What Is JSON?

JSON (JavaScript Object Notation) is a text format for structured data:

```json
{"name": "Alice", "age": 25, "scores": [85, 92]}
```

---

### Reading JSON in Python

```python
import json
with open("data.json") as f:
    data = json.load(f)
print(data["name"])  # Alice
```

---

### JSON Types Map to Python

- JSON object → Python dict
- JSON array → Python list
- JSON string → Python str
- JSON number → Python int/float
- JSON true/false → Python True/False
- JSON null → Python None

---

### Try This

```python
import json
text = '{"city": "Mumbai", "population": 20000000}'
data = json.loads(text)
print(data["city"])
```
