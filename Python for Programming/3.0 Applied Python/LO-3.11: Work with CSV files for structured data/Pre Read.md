# Pre-Read: Work with CSV Files

## What are CSV Files?

CSV (Comma-Separated Values) files store tabular data:

```
name,age,city
Alice,25,New York
Bob,30,San Francisco
Charlie,35,Chicago
```

## Reading CSV Files

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Alice', '25', 'New York']
```

## Writing CSV Files

```python
import csv

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', '25'])
    writer.writerow(['Bob', '30'])
```

## Why Use CSV?

1. **Simple format**: Human-readable
2. **Universal**: Supported everywhere
3. **Efficient**: Good for tabular data
