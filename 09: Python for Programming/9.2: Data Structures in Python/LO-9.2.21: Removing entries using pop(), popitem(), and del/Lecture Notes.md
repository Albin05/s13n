## Lecture Notes: Removing Entries Using pop(), popitem(), and del


---

## Introduction

Multiple removal methods reflect **different use cases**: `del` for simple removal, `pop()` for removal + retrieval, `popitem()` for stack-like (LIFO) behavior. This represents **API granularity** - providing specific tools for specific patterns rather than one generic method.

---

<div align="center">

![Python Dictionary pop() Remove Entry](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.21.png)

*del removes by key, pop() removes and returns the value, popitem() removes the last inserted pair (LIFO)*

</div>

---

### Why Multiple Removal Methods?

**del** = **Statement** (not a method): Low-level, like variable deletion
**pop()** = **Retrieval + removal**: Get value before deleting (common pattern!)
**popitem()** = **LIFO stack**: Process items in reverse insertion order
**clear()** = **Bulk operation**: Empty everything at once

**Each serves a distinct purpose** - Python optimizes for common patterns!

### Real-World Analogies

**del like permanent deletion**: "Delete this file" → Gone forever, no undo
**pop() like withdrawal**: "Withdraw $50 from account" → Get money AND remove from balance
**popitem() like todo list**: "Take last item added" → LIFO (Last In, First Out) - like undoing recent changes
**clear() like factory reset**: "Erase all data" → Start fresh

---

### Three Ways to Remove Dictionary Entries

---

### 1. `del` Statement

Removes a specific key-value pair:

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

del student['grade']
print(student)  # {'name': 'Alice', 'age': 22}
```

**If the key doesn't exist:**
```python
# del student['email']  # KeyError: 'email'
```

**Delete the entire dictionary:**
```python
del student  # student no longer exists
# print(student)  # NameError: name 'student' is not defined
```

---

### 2. `pop()` Method

Removes and **returns** the value:

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

removed_grade = student.pop('grade')
print(removed_grade)  # 'A'
print(student)        # {'name': 'Alice', 'age': 22}
```

**With a default (no error if key missing):**
```python
result = student.pop('email', 'not found')
print(result)  # 'not found' — no KeyError!
```

**Without a default (error if key missing):**
```python
# student.pop('email')  # KeyError: 'email'
```

---

### 3. `popitem()` Method

Removes and returns the **last** inserted key-value pair (as a tuple):

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

last = student.popitem()
print(last)     # ('grade', 'A')
print(student)  # {'name': 'Alice', 'age': 22}
```

**On empty dict:**
```python
# {}.popitem()  # KeyError: 'popitem(): dictionary is empty'
```

---

### 4. `clear()` Method

Removes **all** entries (keeps the dict object):

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

student.clear()
print(student)  # {}
print(type(student))  # <class 'dict'> — still a dict, just empty
```

---

### Comparison Table

| Method | Returns Value? | Key Required? | Error if Missing? |
|--------|---------------|---------------|-------------------|
| `del d[key]` | No | Yes | Yes (KeyError) |
| `d.pop(key)` | Yes | Yes | Yes (unless default given) |
| `d.pop(key, default)` | Yes (or default) | Yes | No |
| `d.popitem()` | Yes (last pair) | No | Yes (if empty) |
| `d.clear()` | No | No | No |

---

### Safe Deletion Patterns

**Pattern 1: Check before delete**
```python
if 'email' in student:
    del student['email']
```

**Pattern 2: pop with default**
```python
email = student.pop('email', None)
if email:
    print(f"Removed: {email}")
```

**Pattern 3: Delete multiple keys**
```python
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
keys_to_remove = ['b', 'd', 'f']

for key in keys_to_remove:
    data.pop(key, None)  # Safe — ignores missing keys

print(data)  # {'a': 1, 'c': 3, 'e': 5}
```

---

### Practical Examples

**1. Remove Sensitive Data Before Logging:**
```python
user_data = {'name': 'Alice', 'email': 'alice@mail.com',
             'password': 'secret123', 'ssn': '123-45-6789'}

sensitive_keys = ['password', 'ssn']
safe_data = user_data.copy()
for key in sensitive_keys:
    safe_data.pop(key, None)

print(f"Logging: {safe_data}")
# Logging: {'name': 'Alice', 'email': 'alice@mail.com'}
```

**2. Process and Remove Items:**
```python
tasks = {'task_1': 'Buy groceries', 'task_2': 'Clean house', 'task_3': 'Study'}

while tasks:
    task_id, description = tasks.popitem()
    print(f"Completed: {description}")

# Completed: Study
# Completed: Clean house
# Completed: Buy groceries
```

**3. Filter Out Entries:**
```python
scores = {'Alice': 92, 'Bob': 45, 'Charlie': 78, 'Diana': 38, 'Eve': 85}

# Remove failing students (below 50)
failing = [name for name, score in scores.items() if score < 50]
for name in failing:
    del scores[name]

print(f"Passing: {scores}")
# Passing: {'Alice': 92, 'Charlie': 78, 'Eve': 85}
```

---

### Key Takeaways

1. `del d[key]` — simple removal, no return value, errors on missing key
2. `pop(key)` — removes and returns the value, can provide a default
3. `popitem()` — removes and returns the last pair (LIFO order)
4. `clear()` — empties the entire dictionary
5. Use `pop(key, None)` for safe removal without error checking
6. Never modify a dict while iterating — collect keys first, then remove
