## Editorials: Iterating Through Dictionaries

---

### Q1 Solution: Basic Iteration

```python
capitals = {'India': 'New Delhi', 'Japan': 'Tokyo', 'France': 'Paris', 'Brazil': 'Brasilia'}

print("Countries:", ', '.join(capitals.keys()))
print("Capitals:", ', '.join(capitals.values()))

for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")
```

---

### Q2 Solution: Grade Statistics

```python
grades = {'Alice': 92, 'Bob': 78, 'Charlie': 85, 'Diana': 95, 'Eve': 70}

avg = sum(grades.values()) / len(grades)
print(f"Average: {avg}")

top = max(grades, key=grades.get)
bottom = min(grades, key=grades.get)
print(f"Highest: {top} ({grades[top]})")
print(f"Lowest: {bottom} ({grades[bottom]})")

above_avg = [name for name, score in grades.items() if score > avg]
print(f"Above average: {above_avg}")
```

---

### Q3 Solution: Word Frequency Report

```python
text = "python is great python is powerful python is easy to learn and python is fun"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Alphabetical:")
for word in sorted(freq):
    print(f"  {word}: {freq[word]}")

print("\nBy frequency:")
for word in sorted(freq, key=freq.get, reverse=True):
    print(f"  {word}: {freq[word]}")

print("\nBar chart:")
max_len = max(len(w) for w in freq)
for word in sorted(freq, key=freq.get, reverse=True):
    print(f"  {word.ljust(max_len)} : {'*' * freq[word]}")
```

---

### Q4 Solution: Nested Dict Report

```python
company = {
    'Engineering': {
        'Alice': {'salary': 120000, 'level': 'Senior'},
        'Bob': {'salary': 85000, 'level': 'Junior'}
    },
    'Marketing': {
        'Charlie': {'salary': 95000, 'level': 'Mid'},
        'Diana': {'salary': 110000, 'level': 'Senior'}
    },
    'Sales': {
        'Eve': {'salary': 75000, 'level': 'Junior'},
        'Frank': {'salary': 130000, 'level': 'Senior'}
    }
}

dept_totals = {}
seniors = []

for dept, employees in company.items():
    print(f"\n{dept}:")
    total = 0
    for name, info in employees.items():
        print(f"  {name}: ${info['salary']:,} ({info['level']})")
        total += info['salary']
        if info['level'] == 'Senior':
            seniors.append(name)
    dept_totals[dept] = total
    print(f"  Total: ${total:,}")

top_dept = max(dept_totals, key=dept_totals.get)
print(f"\nHighest spending dept: {top_dept} (${dept_totals[top_dept]:,})")
print(f"Senior employees: {seniors}")
```

---

### Q5 Solution: Dict Transformation Pipeline

```python
raw_data = {
    'product_001': {'name': 'Laptop', 'price': 999, 'stock': 5},
    'product_002': {'name': 'Mouse', 'price': 29, 'stock': 0},
    'product_003': {'name': 'Keyboard', 'price': 79, 'stock': 12},
    'product_004': {'name': 'Monitor', 'price': 399, 'stock': 0},
    'product_005': {'name': 'Headset', 'price': 149, 'stock': 8}
}

# 1. In stock only
in_stock = {pid: info for pid, info in raw_data.items() if info['stock'] > 0}
print(f"In stock: {[v['name'] for v in in_stock.values()]}")

# 2. Price map
price_map = {info['name']: info['price'] for info in in_stock.values()}
print(f"Prices: {price_map}")

# 3. Affordable and in stock
affordable = {info['name']: info['price'] for info in in_stock.values() if info['price'] < 200}
print(f"Affordable: {affordable}")

# 4. Total value
total = sum(info['price'] * info['stock'] for info in in_stock.values())
print(f"Total inventory value: ${total:,}")
```
