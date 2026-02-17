## Lecture Script: Write Data to JSON Files


---

### CS Theory Bite

> **Origin**: JSON serialization converts Python objects to portable text. **json.dumps()** handles the mapping: `dict` → `{}`, `list` → `[]`, `None` → `null`, `True` → `true`.
>
> **Analogy**: Writing JSON is like **translating a letter** — convert Python's dialect into the universal JSON format that any language can read.
>
> **Why it matters**: Saving data as JSON enables interoperability — other programs, languages, and services can read your output.



### Hook (2 minutes)

You've processed data and need to save results in a format any program can read:

```python
import json
with open("results.json", "w") as f:
    json.dump({"status": "complete", "score": 95}, f, indent=2)
```

---

### Section 1: Writing JSON (3 minutes)

```python
import json
data = {"name": "Alice", "scores": [85, 92, 78]}

# To file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# To string
json_string = json.dumps(data, indent=2)
```

---

### Section 2: Formatting Options (3 minutes)

```python
json.dump(data, f, indent=2)             # Pretty print
json.dump(data, f, sort_keys=True)       # Alphabetical keys
json.dump(data, f, ensure_ascii=False)   # Allow Unicode
```

---

### Section 3: Read-Modify-Write (3 minutes)

```python
try:
    with open("data.json") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

data.append({"name": "New Entry"})

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

### Summary (1 minute)

1. `json.dump(data, file)` writes to file
2. `json.dumps(data)` returns string
3. `indent=2` for readability
4. Read-modify-write for updates
