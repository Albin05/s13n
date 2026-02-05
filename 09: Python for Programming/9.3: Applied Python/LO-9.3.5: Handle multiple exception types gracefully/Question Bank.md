## Question Bank: Handle Multiple Exception Types Gracefully

---

### Q1: Multi-Error Handler (3 minutes, Low Difficulty)

Write a function `safe_access(data, key, index)` that:
- Gets `data[key]` then accesses `[index]` on the result
- Handles `KeyError`, `IndexError`, `TypeError` separately with clear messages
- Returns the value or None

Test with:
```python
data = {'nums': [1, 2, 3], 'text': 'hello', 'val': 42}
safe_access(data, 'nums', 1)    # 2
safe_access(data, 'missing', 0) # KeyError
safe_access(data, 'nums', 10)   # IndexError
safe_access(data, 'val', 0)     # TypeError (int not subscriptable)
```

**Key Concepts:** Multiple except blocks

---

### Q2: Input Converter (3 minutes, Low Difficulty)

Write `convert(value, target_type)` that handles:
- `ValueError` for unconvertible values
- `TypeError` for None input
- Returns converted value or descriptive error string

Test converting various values to `int`, `float`, and `bool`.

**Key Concepts:** Specific exception handling per type

---

### Q3: File Format Detector (5 minutes, Medium Difficulty)

Write `load_file(filename)` that tries multiple formats:
1. Try JSON parsing
2. If `json.JSONDecodeError`, try CSV parsing
3. If `csv.Error`, try plain text
4. Handle `FileNotFoundError` separately
5. Return `(format, data)` tuple

**Key Concepts:** Sequential fallback with different exceptions

---

### Q4: Robust Calculator (5 minutes, Medium Difficulty)

Write a calculator `evaluate(expression)` that:
- Parses expressions like "10 + 5", "8 / 0", "abc * 2"
- Handles `ValueError` (bad numbers), `ZeroDivisionError`, `KeyError` (unknown operator)
- Uses `else` to print "Calculation successful"
- Uses `finally` to log every attempt
- Returns result or error message

**Key Concepts:** Full try-except-else-finally, multiple exceptions

---

### Q5: API Response Handler (5 minutes, Medium Difficulty)

Write `process_api_response(response)` that handles:
```python
responses = [
    {'status': 200, 'data': {'users': [{'name': 'Alice'}]}},
    {'status': 404},
    {'status': 200, 'data': 'not a dict'},
    {'status': 200, 'data': {'users': None}},
    None
]
```

Handle `TypeError`, `KeyError`, `AttributeError`, `IndexError` with specific messages. Extract the first user's name from each response.

**Key Concepts:** Nested data access with multiple failure modes
