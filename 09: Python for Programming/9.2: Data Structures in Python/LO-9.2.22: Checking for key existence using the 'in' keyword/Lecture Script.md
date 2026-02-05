## Lecture Script: Checking for Key Existence

**Duration:** 12 minutes

---

### Hook (2 minutes)

Your app receives JSON data from an API. Sometimes fields are missing:

```python
response = {'status': 'ok', 'data': {'name': 'Alice'}}

# This works:
print(response['status'])  # 'ok'

# This crashes:
# print(response['error'])  # KeyError!
```

In real applications, data is messy. Keys might be missing. You need to check before accessing.

---

### Section 1: Basic Key Checking (2 minutes)

```python
user = {'name': 'Alice', 'age': 25}

# Check keys
print('name' in user)   # True
print('email' in user)  # False

# NOT in
if 'email' not in user:
    print("No email on file")
```

**Remember:** `in` checks **keys only**, not values.

---

### Section 2: Keys vs Values (2 minutes)

```python
scores = {'Alice': 90, 'Bob': 85}

# Key check
print('Alice' in scores)          # True

# Value check
print(90 in scores.values())      # True
print(90 in scores)               # False — 90 is not a key!
```

---

### Section 3: Patterns with `in` (3 minutes)

**Conditional access:**
```python
if 'email' in user:
    send_notification(user['email'])
```

**Counting:**
```python
counts = {}
for item in data:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
```

**Validation:**
```python
required = {'name', 'email', 'password'}
missing = [f for f in required if f not in form]
```

---

### Section 4: in vs get() (2 minutes)

```python
# Use 'in' when you need different logic paths
if 'role' in user:
    grant_access(user['role'])
else:
    deny_access()

# Use .get() when you just need a value with fallback
role = user.get('role', 'guest')
```

---

### Summary (1 minute)

1. `key in dict` — checks if key exists (O(1))
2. `val in dict.values()` — checks if value exists
3. Use `in` for conditional logic, `.get()` for fallback values
4. Always check before `del` or `[]` to prevent `KeyError`
