## Lecture Script: Read JSON Files and Parse Data


---

### CS Theory Bite

> **Origin**: JSON was formalized by **Douglas Crockford** (2001) as a lightweight alternative to XML. Based on **JavaScript object syntax**, it became the standard for web APIs (**RFC 4627**, 2006).
>
> **Analogy**: JSON is like a **structured text message** — human-readable, machine-parseable, and universally understood by APIs.
>
> **Why it matters**: JSON is the language of web APIs — every REST endpoint speaks JSON.



### Hook (2 minutes)

Every web API returns JSON. Config files are JSON. Data exports are JSON. It's the language of modern data exchange.

```python
import json
with open("data.json") as f:
    data = json.load(f)
print(data["name"])
```

---

### Section 1: Reading JSON (3 minutes)

```python
import json

# From file
with open("users.json") as f:
    users = json.load(f)

# From string
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
```

Note: `load(file)` vs `loads(string)`.

---

### Section 2: JSON to Python Types (2 minutes)

| JSON | Python |
|------|--------|
| object | dict |
| array | list |
| string | str |
| number | int/float |
| true/false | True/False |
| null | None |

---

### Section 3: Working with Parsed Data (3 minutes)

```python
data = json.load(open("api.json"))

for user in data["users"]:
    print(user["name"])
    city = user.get("address", {}).get("city", "Unknown")
```

---

### Section 4: Error Handling (1 minute)

```python
try:
    data = json.load(open("data.json"))
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

---

### Summary (1 minute)

1. `json.load(file)` reads from file
2. `json.loads(string)` parses string
3. JSON becomes Python dicts, lists, strings, numbers, bools, None
4. Handle `JSONDecodeError` for malformed JSON
