## Editorials: Creating and Initializing Dictionaries

---

### Q1 Solution: Basic Dictionary Creation

```python
# 1. Curly braces
book = {'title': 'Python Crash Course', 'author': 'Eric Matthes',
        'year': 2019, 'pages': 544}
print(f"book: {book}")

# 2. dict() constructor
settings = dict(theme='dark', language='en', notifications=True)
print(f"settings: {settings}")

# 3. fromkeys()
scores = dict.fromkeys(['Math', 'Science', 'English'], 0)
print(f"scores: {scores}")
```

**Explanation:** Three different creation methods for different situations. Curly braces are most common. `dict()` is readable for simple string keys. `fromkeys()` is efficient when many keys share a default value.

---

### Q2 Solution: Dictionary from Two Lists

```python
countries = ['India', 'Japan', 'Brazil', 'Germany', 'Australia']
capitals = ['New Delhi', 'Tokyo', 'Brasilia', 'Berlin', 'Canberra']

# 1. zip + dict
country_to_capital = dict(zip(countries, capitals))
print(f"Countries to capitals: {country_to_capital}")

# 2. Reverse mapping with comprehension
capital_to_country = {v: k for k, v in country_to_capital.items()}
print(f"Capitals to countries: {capital_to_country}")
```

**Explanation:** `zip()` pairs elements from both lists, and `dict()` converts those pairs into a dictionary. The reverse mapping uses a comprehension that swaps keys and values.

---

### Q3 Solution: Student Grade Book

```python
grades = {
    'Alice': {'Math': 92, 'Science': 88, 'English': 95},
    'Bob': {'Math': 78, 'Science': 85, 'English': 80},
    'Charlie': {'Math': 95, 'Science': 92, 'English': 88}
}

# Print grades and averages
averages = {}
for student, subjects in grades.items():
    print(f"{student}: {subjects}")
    avg = sum(subjects.values()) / len(subjects)
    averages[student] = avg

print()
for student, avg in averages.items():
    print(f"{student} average: {avg:.2f}")

top = max(averages, key=averages.get)
print(f"Top student: {top}")
```

**Explanation:** We iterate over the nested dictionary. `subjects.values()` gives the grade values, which we average. `max()` with `key=averages.get` finds the student with the highest average.

---

### Q4 Solution: Word Frequency with Comprehension

```python
text = "python is great and python is fun and learning python is the best way to learn programming and programming is fun"
words = text.split()

# 1. Frequency dictionary
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(f"Frequencies: {freq}")

# 2. Repeated words (comprehension)
repeated = {w: c for w, c in freq.items() if c > 1}
print(f"Repeated words: {repeated}")

# 3. Word lengths (unique words)
lengths = {w: len(w) for w in set(words)}
print(f"Word lengths: {lengths}")

# 4. Most frequent
most = max(freq, key=freq.get)
print(f"Most frequent: \'{most}\' ({freq[most]} times)")
```

**Explanation:** `.get(word, 0)` returns 0 for new words, avoiding KeyError. Dictionary comprehension with `if c > 1` filters for repeated words. `max()` with `key=freq.get` finds the key with the highest count.

---

### Q5 Solution: Inventory System

```python
inventory = {
    'laptop': {'price': 999.99, 'quantity': 10, 'category': 'electronics'},
    'phone': {'price': 699.99, 'quantity': 2, 'category': 'electronics'},
    'rice': {'price': 2.99, 'quantity': 50, 'category': 'food'},
    'bread': {'price': 3.49, 'quantity': 3, 'category': 'food'},
    'notebook': {'price': 4.99, 'quantity': 100, 'category': 'stationery'}
}

def total_value(inv):
    total = 0
    for product, details in inv.items():
        total += details['price'] * details['quantity']
    return total

def by_category(inv):
    categories = {}
    for product, details in inv.items():
        cat = details['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(product)
    return categories

def low_stock(inv, threshold):
    return {p: d['quantity'] for p, d in inv.items() if d['quantity'] < threshold}

print(f"Total inventory value: ${total_value(inventory):,.2f}")
print(f"By category: {by_category(inventory)}")
print(f"Low stock (< 5): {low_stock(inventory, 5)}")
```

**Explanation:**
- `total_value` multiplies price × quantity for each product and sums.
- `by_category` builds a new dict grouping products by their category.
- `low_stock` uses a comprehension to filter products below the threshold.
