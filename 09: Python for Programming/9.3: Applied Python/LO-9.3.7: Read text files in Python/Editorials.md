## Editorials: Read Text Files in Python

---

### Q1 Solution: Basic File Reading

```python
try:
    with open("sample.txt") as f:
        content = f.read()
    
    lines = content.splitlines()
    words = content.split()
    chars = len(content.replace("\n", ""))
    
    print(f"Content:\n{content}")
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {chars}")
except FileNotFoundError:
    print("File 'sample.txt' not found!")
```

**Explanation:** `read()` gets everything. `splitlines()` splits by line. `split()` splits by whitespace (counts words). We remove newlines for character count.

---

### Q2 Solution: Line-by-Line Processing

```python
def print_numbered(filename):
    try:
        with open(filename) as f:
            for i, line in enumerate(f, 1):
                print(f"{i}: {line.strip()}")
            print(f"\nTotal: {i} lines")
    except FileNotFoundError:
        print(f"File '{filename}' not found")

print_numbered("sample.txt")
```

---

### Q3 Solution: Log File Analyzer

```python
def analyze_log(filename):
    counts = {'INFO': 0, 'ERROR': 0, 'WARNING': 0}
    errors = []
    first_ts = last_ts = None
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(None, 3)  # Split into 4 parts max
            timestamp = f"{parts[0]} {parts[1]}"
            level = parts[2]
            message = parts[3] if len(parts) > 3 else ""
            
            if first_ts is None:
                first_ts = timestamp
            last_ts = timestamp
            
            if level in counts:
                counts[level] += 1
            if level == "ERROR":
                errors.append(message)
    
    return {'counts': counts, 'errors': errors, 'first': first_ts, 'last': last_ts}
```

---

### Q4 Solution: Config File Reader

```python
def read_config(filename):
    config = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' not in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            # Type conversion
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass  # Keep as string
            
            config[key] = value
    return config

config = read_config("app.conf")
print(config)
```

---

### Q5 Solution: File Comparison

```python
def compare_files(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    same = diff = only_one = 0
    max_lines = max(len(lines1), len(lines2))
    
    for i in range(max_lines):
        if i < len(lines1) and i < len(lines2):
            if lines1[i] == lines2[i]:
                same += 1
            else:
                diff += 1
                print(f"Line {i+1} differs:")
                print(f"  File1: {lines1[i].strip()}")
                print(f"  File2: {lines2[i].strip()}")
        elif i < len(lines1):
            only_one += 1
            print(f"Line {i+1}: only in {file1}")
        else:
            only_one += 1
            print(f"Line {i+1}: only in {file2}")
    
    print(f"\nSame: {same}, Different: {diff}, Only in one: {only_one}")
```
