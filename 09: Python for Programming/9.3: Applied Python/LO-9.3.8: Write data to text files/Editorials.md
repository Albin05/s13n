## Editorials: Write Data to Text Files

---

### Q1 Solution: Basic File Writing

```python
# 1. Using write()
with open("greeting.txt", "w") as f:
    f.write("Hello!\n")
    f.write("Welcome to Python.\n")
    f.write("Enjoy coding!\n")

# 2. Using print(file=)
with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        print(i, file=f)

# 3. Using writelines()
items = ["Apple\n", "Banana\n", "Cherry\n"]
with open("list.txt", "w") as f:
    f.writelines(items)

# Verify
for fname in ["greeting.txt", "numbers.txt", "list.txt"]:
    with open(fname) as f:
        print(f"--- {fname} ---")
        print(f.read())
```

---

### Q2 Solution: Student Record Writer

```python
students = [
    {"name": "Alice", "age": 22, "grade": "A"},
    {"name": "Bob", "age": 24, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A+"}
]

with open("students.txt", "w") as f:
    f.write(f"{'Name':<10s} {'Age':<4s} {'Grade':<5s}\n")
    f.write(f"{'-'*10} {'-'*4} {'-'*5}\n")
    for s in students:
        f.write(f"{s['name']:<10s} {s['age']:<4d} {s['grade']:<5s}\n")
```

---

### Q3 Solution: Log Writer

```python
from datetime import datetime

class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, "a")
        return self
    
    def __exit__(self, *args):
        if self.file:
            self.file.close()
    
    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"{timestamp} {level} {message}\n")

with Logger("app.log") as log:
    log.log("INFO", "Application started")
    log.log("ERROR", "Connection failed")
```

---

### Q4 Solution: Data Exporter

```python
def export_data(data, filename, fmt):
    keys = data[0].keys()
    with open(filename, "w") as f:
        if fmt == "csv":
            f.write(",".join(keys) + "\n")
            for row in data:
                f.write(",".join(str(row[k]) for k in keys) + "\n")
        elif fmt == "txt":
            widths = {k: max(len(k), max(len(str(r[k])) for r in data)) for k in keys}
            header = "  ".join(k.ljust(widths[k]) for k in keys)
            f.write(header + "\n")
            f.write("  ".join("-" * widths[k] for k in keys) + "\n")
            for row in data:
                f.write("  ".join(str(row[k]).ljust(widths[k]) for k in keys) + "\n")
        elif fmt == "md":
            f.write("| " + " | ".join(keys) + " |\n")
            f.write("| " + " | ".join("---" for _ in keys) + " |\n")
            for row in data:
                f.write("| " + " | ".join(str(row[k]) for k in keys) + " |\n")

data = [{"name": "Alice", "score": 92}, {"name": "Bob", "score": 85}]
export_data(data, "out.csv", "csv")
export_data(data, "out.txt", "txt")
export_data(data, "out.md", "md")
```

---

### Q5 Solution: Safe File Writer

```python
import shutil

def safe_write(filename, content):
    try:
        with open(filename, "x") as f:
            f.write(content)
        return True
    except FileExistsError:
        backup = filename + ".bak"
        shutil.copy2(filename, backup)
        print(f"Backup created: {backup}")
        with open(filename, "w") as f:
            f.write(content)
        return True
```
