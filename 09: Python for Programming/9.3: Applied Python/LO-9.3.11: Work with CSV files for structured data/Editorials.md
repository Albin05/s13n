# Editorials: Work with CSV Files

## Problem 1
```python
import csv

with open("products.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        product, price = row
        print(f"{product}: ${price}")
```

### Explanation
- We use `csv.reader()` to read the file
- `next(reader)` skips the header row
- We unpack each row into `product` and `price` variables
- Then print them in a formatted string

## Problem 2
```python
import csv

students = [
    ["Alice", 20, "A"],
    ["Bob", 21, "B"],
    ["Charlie", 19, "A"]
]

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["name", "age", "grade"])

    # Write student data
    writer.writerows(students)
```

### Explanation
- We create a list of student data (each student is a list)
- Use `csv.writer()` to create a writer object
- `writerow()` writes the header
- `writerows()` writes all student data at once
- **Important**: Always use `newline=''` when opening files for writing

## Problem 3
```python
import csv

total = 0
count = 0

with open("scores.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        name, score = row
        total += int(score)  # Convert string to int
        count += 1

average = total / count
print(f"Average score: {average:.2f}")
```

### Explanation
- Initialize variables to track total and count
- Read each row and convert the score to an integer
- Add to total and increment count
- Calculate average by dividing total by count
- Use `.2f` to format the output to 2 decimal places

**Alternative using DictReader**:
```python
import csv

total = 0
count = 0

with open("scores.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["score"])
        count += 1

average = total / count
print(f"Average score: {average:.2f}")
```

## Problem 4
```python
import csv

employees = [
    {"name": "Alice", "department": "Engineering", "salary": 80000},
    {"name": "Bob", "department": "Marketing", "salary": 65000},
    {"name": "Charlie", "department": "Engineering", "salary": 75000}
]

with open("employees.csv", "w", newline='') as file:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write column headers
    writer.writerows(employees)  # Write all employee data
```

### Explanation
- `csv.DictWriter` is perfect for writing dictionaries
- We specify the `fieldnames` to define the column order
- `writeheader()` writes the column names as the first row
- `writerows()` writes all dictionaries at once
- Each dictionary key must match the fieldnames

## Problem 5
```python
import csv

total_revenue = 0
max_revenue = 0
top_product = ""

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Product Revenues:")
    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        price = int(row["price"])

        revenue = quantity * price
        print(f"{product}: ${revenue}")

        total_revenue += revenue

        if revenue > max_revenue:
            max_revenue = revenue
            top_product = product

print(f"\nTop product: {top_product} (${max_revenue})")
print(f"Total revenue: ${total_revenue}")
```

### Explanation
- Use `DictReader` for easy access to columns by name
- For each product, calculate revenue = quantity × price
- Track the maximum revenue and corresponding product
- Accumulate total revenue across all products
- Convert string values to integers before calculation

**Key Concepts**:
1. **Type conversion**: CSV values are always strings, must convert to int/float
2. **Tracking maximum**: Compare each value and update if larger
3. **Accumulation**: Add to running total in each iteration
4. **DictReader**: Makes code more readable when working with many columns
