## Editorials: Handle Exceptions Using try-except Blocks

---

### Q1 Solution: Safe Calculator

```python
def safe_calc(a, b, operation):
    try:
        if operation == '+':
            return f"{a} + {b} = {a + b}"
        elif operation == '-':
            return f"{a} - {b} = {a - b}"
        elif operation == '*':
            return f"{a} * {b} = {a * b}"
        elif operation == '/':
            return f"{a} / {b} = {a / b}"
        else:
            return f"Unknown operation: {operation}"
    except ZeroDivisionError:
        return f"{a} / {b} = Error: division by zero"
    except TypeError as e:
        return f"{a} {operation} {b} = Error: unsupported operand type"

print(safe_calc(10, 3, '/'))
print(safe_calc(10, 0, '/'))
print(safe_calc("a", 2, '+'))
```

**Explanation:** The try block attempts the operation. `ZeroDivisionError` catches division by zero specifically. `TypeError` catches operations on incompatible types (like string + int without concat).

---

### Q2 Solution: Input Validator

```python
def get_number_in_range(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(f"Please enter a valid integer")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}")

# score = get_number_in_range("Enter score (0-100): ", 0, 100)
```

**Explanation:** The `while True` loop keeps asking. `try-except` catches non-integer input. The range check happens after successful conversion, using `continue` to restart the loop on ValueError.

---

### Q3 Solution: File Data Processor

```python
def process_numbers(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return [], 0

    valid = []
    skipped = 0
    for line in lines:
        try:
            valid.append(float(line.strip()))
        except ValueError:
            skipped += 1

    return valid, skipped

numbers, skipped = process_numbers("numbers.txt")
print(f"Valid numbers: {numbers}")
print(f"Skipped: {skipped} lines")
```

**Explanation:** Outer try-except handles missing file. Inner try-except in the loop handles individual bad lines. `strip()` removes whitespace/newlines. Each bad line increments `skipped` without stopping processing.

---

### Q4 Solution: Nested Data Extractor

```python
users = [
    {'name': 'Alice', 'address': {'city': 'Mumbai', 'zip': '400001'}},
    {'name': 'Bob'},
    {'name': 'Charlie', 'address': {'city': 'Delhi'}},
    {'name': 'Diana', 'address': None}
]

def get_city(user):
    try:
        return user['address']['city']
    except (KeyError, TypeError):
        return 'Unknown'

for user in users:
    print(f"{user['name']}: {get_city(user)}")
```

**Explanation:** `KeyError` handles missing 'address' or 'city' keys. `TypeError` handles `None['city']` (can't subscript None). Both return 'Unknown'. This is cleaner than nested if-checks.

---

### Q5 Solution: Batch Converter

```python
def convert_values(data, target_type):
    converted = []
    failed = []
    for item in data:
        try:
            converted.append(target_type(item))
        except (ValueError, TypeError) as e:
            failed.append((item, str(e)))
    return converted, failed

data = ['42', '3.14', 'hello', '100', '', None, '99']

converted, failed = convert_values(data, int)
print(f"Converted: {converted}")
print(f"Failed: {[(item, msg[:30]) for item, msg in failed]}")
```

**Explanation:** Each item is attempted individually. `ValueError` catches strings that can't convert. `TypeError` catches `None` (can't convert None to int). `as e` captures the error message for reporting.
