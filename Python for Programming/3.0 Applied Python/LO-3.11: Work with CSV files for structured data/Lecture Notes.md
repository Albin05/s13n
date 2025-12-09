# Lecture Notes: Work with CSV Files

## CSV Files

CSV (Comma-Separated Values) stores tabular data in plain text.


---

<div align="center">

![File folders and documents](https://images.unsplash.com/photo-1544396821-4dd40b938ad3?w=800&q=80)

*Python can read from and write to files on your system*

</div>

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
