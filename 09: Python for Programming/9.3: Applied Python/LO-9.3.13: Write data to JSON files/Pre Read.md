## Pre-Read: Write Data to JSON Files


---

### Writing JSON

```python
import json
data = {"name": "Alice", "age": 25}

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

### Key Functions

- `json.dump(data, file)` — write to file
- `json.dumps(data)` — convert to string

---

### Pretty Printing

```python
json.dump(data, f, indent=2)  # Human-readable
json.dump(data, f)             # Compact (one line)
```

---

### Try This

```python
import json
scores = [{"name": "Alice", "score": 92}, {"name": "Bob", "score": 85}]
print(json.dumps(scores, indent=2))
```
