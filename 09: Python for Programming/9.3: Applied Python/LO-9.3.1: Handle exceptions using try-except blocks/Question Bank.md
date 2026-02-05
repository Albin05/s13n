## Question Bank: Handle Exceptions Using try-except Blocks

---

### Q1: Safe Calculator (3 minutes, Low Difficulty)

Write a function `safe_calc(a, b, operation)` that:
- Performs the operation (+, -, *, /) on a and b
- Handles `ZeroDivisionError` for division by zero
- Handles `TypeError` for invalid operand types
- Returns the result or an error message string

Test with: `safe_calc(10, 3, '/')`, `safe_calc(10, 0, '/')`, `safe_calc("a", 2, '+')`

**Expected Output:**
```
10 / 3 = 3.3333333333333335
10 / 0 = Error: division by zero
a + 2 = Error: unsupported operand type
```

**Key Concepts:** try-except with multiple exception types

---

### Q2: Input Validator (3 minutes, Low Difficulty)

Write a function `get_number_in_range(prompt, low, high)` that:
- Keeps asking until user enters a valid integer within the range
- Handles `ValueError` for non-integer input
- Prints an error message for out-of-range values

```python
# Example usage:
score = get_number_in_range("Enter score (0-100): ", 0, 100)
```

**Key Concepts:** try-except in loops, input validation

---

### Q3: File Data Processor (5 minutes, Medium Difficulty)

Write a function `process_numbers(filename)` that:
- Reads a file where each line contains a number
- Converts each line to a float
- Skips lines that can't be converted (catch `ValueError`)
- Returns a tuple: (valid_numbers_list, skipped_count)
- Handles `FileNotFoundError` if file doesn't exist

Test with a file containing: `10`, `20.5`, `hello`, `30`, ``, `forty`, `50`

**Expected Output:**
```
Valid numbers: [10.0, 20.5, 30.0, 50.0]
Skipped: 3 lines
```

**Key Concepts:** try-except in loops, multiple exception handling

---

### Q4: Nested Data Extractor (5 minutes, Medium Difficulty)

Given nested data that may have missing keys:
```python
users = [
    {'name': 'Alice', 'address': {'city': 'Mumbai', 'zip': '400001'}},
    {'name': 'Bob'},
    {'name': 'Charlie', 'address': {'city': 'Delhi'}},
    {'name': 'Diana', 'address': None}
]
```

Write a function `get_city(user)` that safely extracts the city. Handle `KeyError`, `TypeError`, and any other relevant exceptions. Return `'Unknown'` for any failure.

**Expected Output:**
```
Alice: Mumbai
Bob: Unknown
Charlie: Delhi
Diana: Unknown
```

**Key Concepts:** Nested try-except, handling multiple failure modes

---

### Q5: Batch Converter (5 minutes, Medium Difficulty)

Write a function `convert_values(data, target_type)` that:
- Takes a list of values and a target type (int, float, str)
- Attempts to convert each value
- Returns two lists: successful conversions and failed items with their errors

```python
data = ['42', '3.14', 'hello', '100', '', None, '99']
```

Test with `target_type=int` and `target_type=float`.

**Expected Output (for int):**
```
Converted: [42, 100, 99]
Failed: [('3.14', 'invalid literal'), ('hello', 'invalid literal'), ('', 'invalid literal'), (None, "int() argument must be a string...")]
```

**Key Concepts:** try-except with error collection, `as e` for error messages
