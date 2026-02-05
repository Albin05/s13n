# Lecture Script: LO-53 Work with CSV Files

## [0:00-0:02] Hook (2 min)
**Say**: "Imagine you have a spreadsheet with thousands of rows of data — sales records, student grades, weather data. How do you process it with Python? CSV files are the answer! They're the universal language of data exchange."

**Demo**: Show a sample CSV file opened in a text editor:
```
name,age,city
Alice,25,New York
Bob,30,San Francisco
```

**Say**: "Just plain text with commas! But incredibly powerful."

## [0:02-0:08] Reading CSV Files (6 min)

**Say**: "Python's csv module makes reading CSV files simple. Let's see how."

**Live Code**:
```python
import csv

# Create a sample CSV file first
with open("students.csv", "w") as f:
    f.write("name,grade,subject\n")
    f.write("Alice,95,Math\n")
    f.write("Bob,87,Science\n")
    f.write("Charlie,92,Math\n")

# Now read it
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Output:
# ['name', 'grade', 'subject']
# ['Alice', '95', 'Math']
# ['Bob', '87', 'Science']
# ['Charlie', '92', 'Math']
```

**Point out**: "Each row is a list. The first row is usually the header."

**Say**: "Let's skip the header and process the data:"
```python
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        name, grade, subject = row
        print(f"{name} scored {grade} in {subject}")
```

**Emphasize**: "Use next(reader) to skip the header row."

## [0:08-0:12] DictReader for Easier Access (4 min)

**Say**: "There's an even better way — DictReader. It uses the header as keys!"

**Live Code**:
```python
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['name']} scored {row['grade']} in {row['subject']}")
```

**Say**: "Now we can access columns by name! Much clearer code."

**Real Example**:
```python
# Calculate average grade
total = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row['grade'])
        count += 1

average = total / count
print(f"Average grade: {average:.2f}")
```

## [0:12-0:16] Writing CSV Files (4 min)

**Say**: "Now let's write data to CSV files."

**Live Code**:
```python
import csv

# Writing with csv.writer
with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Product", "Price", "Quantity"])

    # Write data
    writer.writerow(["Laptop", "999", "5"])
    writer.writerow(["Mouse", "25", "50"])
    writer.writerow(["Keyboard", "75", "20"])
```

**Point out**: "Always use newline='' — it prevents extra blank lines on Windows."

**Say**: "You can write multiple rows at once:"
```python
data = [
    ["Product", "Price", "Quantity"],
    ["Laptop", "999", "5"],
    ["Mouse", "25", "50"]
]

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # writerows, not writerow!
```

## [0:16-0:20] DictWriter Example (4 min)

**Say**: "Just like DictReader, there's DictWriter for writing dictionaries."

**Live Code**:
```python
import csv

products = [
    {"product": "Laptop", "price": 999, "quantity": 5},
    {"product": "Mouse", "price": 25, "quantity": 50},
    {"product": "Keyboard", "price": 75, "quantity": 20}
]

with open("inventory.csv", "w", newline='') as file:
    fieldnames = ["product", "price", "quantity"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    writer.writerows(products)  # Write all rows
```

**Say**: "This is perfect when you're working with dictionaries — like from a database or API."

## [0:20-0:23] Practice Challenge (3 min)

**Challenge**: "Let's build a simple grade book system."

**Guide students**:
```python
import csv

# Write student data
students = [
    {"name": "Alice", "math": 95, "science": 88},
    {"name": "Bob", "math": 87, "science": 92},
    {"name": "Charlie", "math": 92, "science": 85}
]

with open("grades.csv", "w", newline='') as file:
    fieldnames = ["name", "math", "science"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

# Read and calculate averages
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        math = int(row["math"])
        science = int(row["science"])
        avg = (math + science) / 2
        print(f"{row['name']}'s average: {avg:.2f}")
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **csv.reader()**: Read rows as lists
2. **csv.DictReader()**: Read rows as dictionaries (easier!)
3. **csv.writer()**: Write rows from lists
4. **csv.DictWriter()**: Write rows from dictionaries
5. Always use **newline=''** when writing

**Common Pitfall**: "Remember, CSV data is always strings! Convert numbers with int() or float()."

**Closing**: "CSV files are everywhere — Excel can open them, databases can import them, APIs can export them. Master this and you can work with any tabular data!"
