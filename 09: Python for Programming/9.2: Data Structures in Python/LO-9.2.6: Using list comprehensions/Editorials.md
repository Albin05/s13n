## Editorials: Using List Comprehensions

### Q1 Solution: Basic List Comprehension Transformations

```python
# 1. Numbers 1-10
numbers = [x for x in range(1, 11)]
print(f"Numbers 1-10: {numbers}")

# 2. Squares
squares = [x ** 2 for x in range(1, 11)]
print(f"Squares: {squares}")

# 3. Even numbers 0-20
evens = [x for x in range(0, 21) if x % 2 == 0]
print(f"Evens 0-20: {evens}")

# 4. Uppercase
words = ['hello', 'world', 'python']
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# 5. Lengths
fruits = ['apple', 'banana', 'cherry']
lengths = [len(fruit) for fruit in fruits]
print(f"Lengths: {lengths}")
```

**Explanation:**
- `[x for x in range(1, 11)]` - basic iteration
- `[x ** 2 for x in range(1, 11)]` - transform each element
- `[x for x in range(0, 21) if x % 2 == 0]` - filter with condition
- `[word.upper() for word in words]` - apply method to each
- `[len(fruit) for fruit in fruits]` - calculate from each

**Pattern:**
`[expression for item in iterable if condition]`

---

### Q2 Solution: Filtering with Comprehensions

```python
numbers = [12, 7, 23, 8, 45, 16, 34, 9, 50, 3]

# 1. Greater than 20
greater_20 = [n for n in numbers if n > 20]
print(f"Greater than 20: {greater_20}")

# 2. Divisible by 4
div_by_4 = [n for n in numbers if n % 4 == 0]
print(f"Divisible by 4: {div_by_4}")

# 3. Single digit
single_digit = [n for n in numbers if n < 10]
print(f"Single digit: {single_digit}")

# 4. Between 10-30
between_10_30 = [n for n in numbers if 10 <= n <= 30]
print(f"Between 10-30: {between_10_30}")

# 5. Odd numbers
odds = [n for n in numbers if n % 2 != 0]
print(f"Odd numbers: {odds}")
```

**Explanation:**
- `if n > 20` - simple comparison filter
- `if n % 4 == 0` - modulo filter
- `if n < 10` - range filter
- `if 10 <= n <= 30` - chained comparison
- `if n % 2 != 0` - logical filter

**Key:** Filtering happens AFTER the `for`, BEFORE the comprehension closes

---

### Q3 Solution: Temperature Conversion System

```python
celsius_temps = [0, 10, 15, 20, 25, 30, 35, 40]

# 1. Convert to Fahrenheit
fahrenheit = [c * 9/5 + 32 for c in celsius_temps]
print(f"Fahrenheit: {fahrenheit}")

# 2. Above 77°F
above_77 = [c * 9/5 + 32 for c in celsius_temps if c * 9/5 + 32 > 77]
print(f"Above 77°F: {above_77}")

# 3. C-F Pairs
cf_pairs = [(c, c * 9/5 + 32) for c in celsius_temps]
print(f"C-F Pairs: {cf_pairs}")

# 4. Comfort levels
comfort = [
    'Cold' if (c * 9/5 + 32) < 60 else
    'Comfortable' if (c * 9/5 + 32) <= 80 else
    'Hot'
    for c in celsius_temps
]
print(f"Comfort levels: {comfort}")

# 5. Divisible by 10 in F
div_10 = [f"{c}°C" for c in celsius_temps if (c * 9/5 + 32) % 10 == 0]
print(f"Divisible by 10 in F: {div_10}")
```

**Explanation:**
- Formula applied in expression: `c * 9/5 + 32`
- Can use same expression in filter: `if c * 9/5 + 32 > 77`
- Tuples in comprehension: `(c, c * 9/5 + 32)`
- Conditional expression: `'Cold' if ... else 'Comfortable' if ... else 'Hot'`
- String formatting in expression: `f"{c}°C"`

**Comprehension Power:**
- Calculate once: `[c * 9/5 + 32 for c in celsius_temps]`
- Calculate and filter: `[... for c in ... if expression > value]`
- Transform to different types: tuples, strings, etc.

---

### Q4 Solution: Student Grade Processor

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
scores = [85, 72, 90, 65, 78, 95]

# 1. Passing students
passing = [student for student, score in zip(students, scores) if score >= 70]
print(f"Passing students: {passing}")

# 2. All pairs
all_pairs = [(student, score) for student, score in zip(students, scores)]
print(f"All student-score pairs: {all_pairs}")

# 3. Passing pairs only
passing_pairs = [(student, score) for student, score in zip(students, scores) if score >= 70]
print(f"Passing pairs: {passing_pairs}")

# 4. Letter grades
def get_letter(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

letters = [get_letter(score) for score in scores]
print(f"Letter grades: {letters}")

# 5. Formatted results
formatted = [
    f"{student}: {score} ({get_letter(score)})" 
    for student, score in zip(students, scores)
]
print("Formatted results:")
for result in formatted:
    print(f"  {result}")
```

**Explanation:**
- `zip(students, scores)` combines parallel lists
- Unpack in comprehension: `for student, score in zip(...)`
- Filter on unpacked values: `if score >= 70`
- Helper function in expression: `get_letter(score)`
- f-string formatting: `f"{student}: {score} ({letter})"`

**zip() in Comprehensions:**
- Perfect for parallel data
- Unpacks automatically
- Can filter on any variable
- Can use multiple variables in expression

---

### Q5 Solution: E-commerce Product Filter

```python
products = [
    {'name': 'Laptop', 'price': 999, 'category': 'Electronics', 'stock': 5},
    {'name': 'Mouse', 'price': 29, 'category': 'Electronics', 'stock': 50},
    {'name': 'Desk', 'price': 299, 'category': 'Furniture', 'stock': 10},
    {'name': 'Chair', 'price': 199, 'category': 'Furniture', 'stock': 15},
    {'name': 'Monitor', 'price': 349, 'category': 'Electronics', 'stock': 8},
    {'name': 'Keyboard', 'price': 79, 'category': 'Electronics', 'stock': 30}
]

# 1. Product names
names = [p['name'] for p in products]
print(f"Product names: {names}")

# 2. Electronics
electronics = [p['name'] for p in products if p['category'] == 'Electronics']
print(f"\nElectronics: {electronics}")

# 3. Under $100
under_100 = [p['name'] for p in products if p['price'] < 100]
print(f"\nUnder $100: {under_100}")

# 4. Discounted prices
print("\nDiscounted prices (>$200):")
discounted = [(p['name'], p['price'] * 0.9) for p in products if p['price'] > 200]
for name, price in discounted:
    print(f"  {name}: ${price:.2f}")

# 5. Low stock
print("\nLow stock alerts:")
low_stock = [f"{p['name']}: {p['stock']} units left" for p in products if p['stock'] < 10]
for alert in low_stock:
    print(f"  {alert}")
```

**Explanation:**
- Dictionary access in expression: `p['name']`
- Filter on dictionary value: `if p['category'] == 'Electronics'`
- Multiple filters: `if p['price'] < 100`
- Calculate in expression: `p['price'] * 0.9`
- String formatting: `f"{p['name']}: {p['stock']} units left"`

**Working with Dictionaries:**
- Access keys in expression: `p['key']`
- Filter on any key: `if p['category'] == value`
- Calculate from multiple keys: `p['price'] * p['qty']`
- Create new structures: tuples, formatted strings

**Key Concepts:**
- Comprehensions work with any iterable
- Can access complex structures (dicts, objects)
- Combine transformation and filtering
- Keep expression simple for readability
- Use helper functions for complex logic
