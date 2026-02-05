## Pre-Read: Iterating Through Dictionaries

**Duration:** 5 minutes

---

### Three Iteration Methods

```python
d = {'name': 'Alice', 'age': 25}

# Keys
for key in d:
    print(key)       # name, age

# Values
for val in d.values():
    print(val)       # Alice, 25

# Both
for key, val in d.items():
    print(key, val)  # name Alice, age 25
```

---

### Most Useful: .items()

```python
scores = {'Alice': 90, 'Bob': 80}
for name, score in scores.items():
    print(f"{name} scored {score}")
```

---

### Try Before Class

```python
prices = {'apple': 1.5, 'banana': 0.75, 'cherry': 3.0}

# What does this print?
for item, price in prices.items():
    if price > 1:
        print(item)
```

**Answer:** `apple` and `cherry`
