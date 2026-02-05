## Question Bank: Iterating Through Dictionaries

---

### Q1: Basic Iteration (3 minutes, Low Difficulty)

Given:
```python
capitals = {'India': 'New Delhi', 'Japan': 'Tokyo', 'France': 'Paris', 'Brazil': 'Brasilia'}
```

Using iteration, print:
1. All country names (keys only)
2. All capital cities (values only)
3. Each country with its capital in format "The capital of X is Y"

**Expected Output:**
```
Countries: India, Japan, France, Brazil
Capitals: New Delhi, Tokyo, Paris, Brasilia
The capital of India is New Delhi
The capital of Japan is Tokyo
The capital of France is Paris
The capital of Brazil is Brasilia
```

**Key Concepts:** `.keys()`, `.values()`, `.items()`

---

### Q2: Grade Statistics (3 minutes, Low Difficulty)

```python
grades = {'Alice': 92, 'Bob': 78, 'Charlie': 85, 'Diana': 95, 'Eve': 70}
```

Using dictionary iteration, calculate and print:
1. Average grade
2. Highest scorer (name and grade)
3. Lowest scorer (name and grade)
4. Students above average (names)

**Expected Output:**
```
Average: 84.0
Highest: Diana (95)
Lowest: Eve (70)
Above average: ['Alice', 'Diana', 'Charlie']
```

**Key Concepts:** `.values()`, `.items()`, `max()`, `min()`

---

### Q3: Word Frequency Report (5 minutes, Medium Difficulty)

```python
text = "python is great python is powerful python is easy to learn and python is fun"
```

1. Build a frequency dictionary
2. Print words sorted alphabetically with their counts
3. Print words sorted by frequency (highest first)
4. Print a bar chart using `*` characters

**Expected Output:**
```
Alphabetical:
  and: 1
  easy: 1
  fun: 1
  ...
  python: 4

By frequency:
  python: 4
  is: 4
  ...

Bar chart:
  python : ****
  is     : ****
  to     : *
  ...
```

**Key Concepts:** Sorted iteration, formatting

---

### Q4: Nested Dict Report (5 minutes, Medium Difficulty)

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
```

By iterating through the nested structure, print:
1. Each department with its employees
2. Total salary per department
3. Department with highest total salary
4. All Senior-level employees across departments

**Key Concepts:** Nested iteration, accumulating values

---

### Q5: Dict Transformation Pipeline (5 minutes, Medium Difficulty)

```python
raw_data = {
    'product_001': {'name': 'Laptop', 'price': 999, 'stock': 5},
    'product_002': {'name': 'Mouse', 'price': 29, 'stock': 0},
    'product_003': {'name': 'Keyboard', 'price': 79, 'stock': 12},
    'product_004': {'name': 'Monitor', 'price': 399, 'stock': 0},
    'product_005': {'name': 'Headset', 'price': 149, 'stock': 8}
}
```

Using dict iteration and comprehensions:
1. Create `in_stock` — only products with stock > 0
2. Create `price_map` — {product_name: price} for in-stock items
3. Create `affordable` — products under $200 that are in stock
4. Calculate total inventory value (price × stock for in-stock items)

**Key Concepts:** Filtering with comprehensions, chained transformations
