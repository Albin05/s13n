## Editorials: Handle Multiple Exception Types

---

### Q1 Solution: Multi-Error Handler

```python
def safe_access(data, key, index):
    try:
        return data[key][index]
    except KeyError:
        print(f"Key '{key}' not found")
    except IndexError:
        print(f"Index {index} out of range for '{key}'")
    except TypeError as e:
        print(f"Cannot index into {type(data.get(key)).__name__}: {e}")
    return None

data = {'nums': [1, 2, 3], 'text': 'hello', 'val': 42}
print(safe_access(data, 'nums', 1))     # 2
print(safe_access(data, 'missing', 0))  # KeyError
print(safe_access(data, 'nums', 10))    # IndexError
print(safe_access(data, 'val', 0))      # TypeError
```

---

### Q2 Solution: Input Converter

```python
def convert(value, target_type):
    try:
        return target_type(value)
    except ValueError:
        return f"Cannot convert {value!r} to {target_type.__name__}"
    except TypeError:
        return f"Cannot convert None to {target_type.__name__}"

print(convert("42", int))       # 42
print(convert("abc", int))      # Cannot convert 'abc' to int
print(convert(None, int))       # Cannot convert None to int
print(convert("3.14", float))   # 3.14
```

---

### Q3 Solution: File Format Detector

```python
import json, csv, io

def load_file(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        return ("error", f"File not found: {filename}")
    
    # Try JSON
    try:
        data = json.loads(content)
        return ("json", data)
    except json.JSONDecodeError:
        pass
    
    # Try CSV
    try:
        reader = csv.reader(io.StringIO(content))
        data = list(reader)
        if len(data) > 1 and len(data[0]) > 1:
            return ("csv", data)
    except csv.Error:
        pass
    
    # Fall back to plain text
    return ("text", content.splitlines())
```

---

### Q4 Solution: Robust Calculator

```python
def evaluate(expression):
    ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b,
           '*': lambda a,b: a*b, '/': lambda a,b: a/b}
    try:
        parts = expression.split()
        a, op, b = float(parts[0]), parts[1], float(parts[2])
        result = ops[op](a, b)
    except ValueError:
        return f"Error: invalid numbers in '{expression}'"
    except ZeroDivisionError:
        return "Error: division by zero"
    except KeyError:
        return f"Error: unknown operator '{parts[1]}'"
    except (IndexError, AttributeError):
        return "Error: invalid expression format"
    else:
        print("Calculation successful")
        return result
    finally:
        print(f"Attempted: {expression}")

print(evaluate("10 + 5"))
print(evaluate("8 / 0"))
print(evaluate("abc * 2"))
```

---

### Q5 Solution: API Response Handler

```python
def process_api_response(response):
    try:
        if response is None:
            raise TypeError("Response is None")
        status = response['status']
        if status != 200:
            return f"HTTP Error: {status}"
        users = response['data']['users']
        name = users[0]['name']
        return f"First user: {name}"
    except TypeError as e:
        return f"Type error: {e}"
    except KeyError as e:
        return f"Missing field: {e}"
    except IndexError:
        return "No users in response"

responses = [
    {'status': 200, 'data': {'users': [{'name': 'Alice'}]}},
    {'status': 404},
    {'status': 200, 'data': 'not a dict'},
    {'status': 200, 'data': {'users': None}},
    None
]
for r in responses:
    print(process_api_response(r))
```
