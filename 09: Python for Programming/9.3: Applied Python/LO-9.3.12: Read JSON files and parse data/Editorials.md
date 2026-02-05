## Editorials: Read JSON Files and Parse Data

---

### Q1 Solution: Basic JSON Reading

```python
import json
with open("users.json") as f:
    users = json.load(f)
for user in users:
    print(f"{user['name']}: {user['email']}")
```

---

### Q2 Solution: Nested JSON Access

```python
import json
with open("profile.json") as f:
    data = json.load(f)

name = data.get("name", "Unknown")
city = data.get("address", {}).get("city", "Unknown")
theme = data.get("preferences", {}).get("theme", "light")
print(f"{name} from {city}, theme: {theme}")
```

---

### Q3 Solution: API Response Parser

```python
import json

def parse_response(json_file):
    with open(json_file) as f:
        response = json.load(f)
    if response.get("status") != "success":
        return []
    items = response.get("data", [])
    return [item for item in items if item.get("active", False)]
```

---

### Q4 Solution: Config from JSON

```python
import json

def load_config(filename, defaults):
    try:
        with open(filename) as f:
            user_config = json.load(f)
    except FileNotFoundError:
        user_config = {}
    config = {**defaults, **user_config}
    required = ["host", "port"]
    missing = [k for k in required if k not in config]
    if missing:
        raise ValueError(f"Missing required config: {missing}")
    return config
```

---

### Q5 Solution: JSON Data Aggregator

```python
import json
from collections import defaultdict

def aggregate_sales(file_list):
    totals = defaultdict(float)
    counts = defaultdict(int)
    for fname in file_list:
        with open(fname) as f:
            data = json.load(f)
        for item in data:
            totals[item["category"]] += item["amount"]
            counts[item["category"]] += 1
    for cat in sorted(totals):
        avg = totals[cat] / counts[cat]
        print(f"{cat}: total=${totals[cat]:.2f}, avg=${avg:.2f}, count={counts[cat]}")
```
