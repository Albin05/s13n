## Pre-Read: Creating and Initializing Dictionaries

**Duration:** 5 minutes

---

### What You'll Learn

Dictionaries are Python's most versatile data structure. They store data as **key-value pairs** — like a real dictionary where you look up a word (key) to find its definition (value).

---

### Quick Example

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
print(student['name'])   # Alice
print(student['grade'])  # A
```

Each key maps to a value. Keys are like labels for your data.

---

### Why Not Just Use Lists?

```python
# With a list — what does index 2 mean?
student = ['Alice', 22, 'A']
print(student[2])  # 'A' — but you have to remember that 2 = grade

# With a dict — self-documenting!
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
print(student['grade'])  # 'A' — clear!
```

---

### Creating Dictionaries

```python
# Method 1: Curly braces
person = {'name': 'Alice', 'age': 25}

# Method 2: dict() constructor
person = dict(name='Alice', age=25)

# Method 3: Empty dictionary
empty = {}
```

---

### Try This

```python
# Create a dictionary for your favorite book
book = {
    'title': 'Your Book Title',
    'author': 'Author Name',
    'year': 2024,
    'rating': 4.5
}
print(book)
print(book['title'])
```

---

### What to Expect

In class, you'll learn:
- All the ways to create dictionaries
- Dictionary comprehensions
- Nested dictionaries
- Rules for keys and values
- Practical applications
