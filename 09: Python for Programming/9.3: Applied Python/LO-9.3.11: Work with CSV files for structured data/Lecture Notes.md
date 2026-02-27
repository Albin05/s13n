# Lecture Notes: Work with CSV Files

## CSV Files

CSV (Comma-Separated Values) stores tabular data in plain text.


---

<div align="center">

![Python CSV File Reading with csv Module](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.11.png)

*CSV files organize data in structured rows and columns, similar to arrays in a flowchart*

</div>

---

## Introduction

CSV implements **structured text storage** - tabular data in human-readable format! Invented in 1970s for data exchange between incompatible systems. CSV is the **universal data interchange format** - simple, portable, readable by everything from Excel to databases!

### Why CSV Matters

**Before CSV** (binary formats): Data locked in proprietary formats:
```
// Binary spreadsheet - only one program can read!
01101000 01100101 01101100 01101100 01101111
```

**With CSV** (text format): Universal, human-readable:
```csv
name,age,city
Alice,25,New York
Bob,30,Chicago
```

**This is data portability** - any program can read it!

### Historical Context

**CSV originated in FORTRAN** (1970s) for data exchange. No formal standard until **RFC 4180 (2005)** - decades of ad-hoc implementations!

**Why "comma-separated"?** Inherited from punch cards where fields separated by characters. Comma chosen over space/tab because values might contain those!

**Python's csv module** (Python 2.3, 2003): Handles CSV dialects - different delimiters, quoting, escaping. Solves **format fragmentation** problem!

### Real-World Analogies

**CSV like spreadsheet exported as text**:
- **Rows**: Lines in file
- **Columns**: Comma-separated values
- **Header**: First row with column names
**Excel/Google Sheets export to CSV for portability!**

---
### CSV Format

```
name,age,city
Alice,25,New York
Bob,30,San Francisco
Charlie,35,Chicago
```

## Reading CSV Files

### Using csv.reader

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)

# Output:
# ['name', 'age', 'city']
# ['Alice', '25', 'New York']
# ['Bob', '30', 'San Francisco']
```

### Skip Header

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    
    for row in reader:
        name, age, city = row
        print(f"{name} is {age} years old")
```

### Using DictReader

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row["name"], row["age"], row["city"])
```

## Writing CSV Files

### Using csv.writer

```python
import csv

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Name", "Age", "City"])
    
    # Write data
    writer.writerow(["Alice", "25", "New York"])
    writer.writerow(["Bob", "30", "San Francisco"])
```

### Write Multiple Rows

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "San Francisco"],
    ["Charlie", "35", "Chicago"]
]

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### Using DictWriter

```python
import csv

data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"}
]

with open("output.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)
```

## Real-World Examples

### Process Student Scores

```python
import csv

# Read scores
total = 0
count = 0

with open("scores.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        score = int(row["score"])
        total += score
        count += 1

average = total / count if count > 0 else 0
print(f"Average score: {average}")
```

### Export Data

```python
import csv

users = [
    {"username": "alice", "email": "alice@example.com", "active": True},
    {"username": "bob", "email": "bob@example.com", "active": False}
]

with open("users.csv", "w", newline='') as file:
    fieldnames = ["username", "email", "active"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(users)
```

## Key Takeaways

1. **csv.reader**: Read rows as lists
2. **csv.writer**: Write rows from lists
3. **DictReader**: Read rows as dictionaries
4. **DictWriter**: Write rows from dictionaries
5. **newline=''**: Important for Windows compatibility
