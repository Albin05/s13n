## Editorials: Adding and Modifying Dictionary Entries

---

### Q1 Solution: Building a Contact

```python
contact = {}

contact['name'] = 'Alice'
print(f"Step 1: {contact}")

contact['phone'] = '555-0101'
print(f"Step 2: {contact}")

contact['email'] = 'alice@old.com'
print(f"Step 3: {contact}")

contact['email'] = 'alice@new.com'
print(f"Step 4: {contact}")

contact.setdefault('city', 'Mumbai')
print(f"Step 5: {contact}")

contact.setdefault('city', 'Delhi')  # No change!
print(f"Step 6: {contact}")
```

**Explanation:** `setdefault()` in step 5 adds 'city' because it doesn't exist. In step 6, 'city' already exists so `setdefault()` leaves it unchanged at 'Mumbai'.

---

### Q2 Solution: Config Merger

```python
defaults = {'theme': 'light', 'font_size': 14, 'language': 'en', 'notifications': True}
user_settings = {'theme': 'dark', 'font_size': 18}

# Find what will be overridden
overridden = []
for key, val in user_settings.items():
    if key in defaults and defaults[key] != val:
        overridden.append(f"{key} ({defaults[key]} -> {val})")

# Merge
final = {**defaults, **user_settings}
print(f"Final config: {final}")
print(f"Overridden: {', '.join(overridden)}")
```

---

### Q3 Solution: Word Frequency Counter

```python
text = "to be or not to be that is the question to be is to exist"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(f"Frequencies: {freq}")

most_common = max(freq, key=freq.get)
print(f"Most common: \'{most_common}\' ({freq[most_common]} times)")

once = [w for w, c in freq.items() if c == 1]
print(f"Appear once: {once}")

three_plus = [w for w, c in freq.items() if c >= 3]
print(f"Appear 3+ times: {three_plus}")
```

---

### Q4 Solution: Shopping Cart Manager

```python
def add_item(cart, name, price, qty):
    if name in cart:
        cart[name]['quantity'] += qty
    else:
        cart[name] = {'price': price, 'quantity': qty}

def update_quantity(cart, name, new_qty):
    if name in cart:
        cart[name]['quantity'] = new_qty

def get_total(cart):
    return sum(d['price'] * d['quantity'] for d in cart.values())

def apply_discount(cart, product, percent):
    if product in cart:
        cart[product]['price'] *= (1 - percent / 100)

cart = {}
add_item(cart, 'Apple', 1.50, 3)
add_item(cart, 'Banana', 0.75, 5)
add_item(cart, 'Apple', 1.50, 2)  # qty becomes 5
apply_discount(cart, 'Apple', 10)

for name, details in cart.items():
    print(f"{name}: ${details['price']:.2f} x {details['quantity']}")
print(f"Total: ${get_total(cart):.2f}")
```

---

### Q5 Solution: Grade Tracker

```python
grades = {}
data = [('Alice', 85), ('Bob', 90), ('Alice', 92),
        ('Charlie', 78), ('Bob', 88), ('Alice', 95)]

for name, score in data:
    grades.setdefault(name, []).append(score)

for student, scores in grades.items():
    avg = sum(scores) / len(scores)
    if avg >= 90: letter = 'A'
    elif avg >= 80: letter = 'B'
    elif avg >= 70: letter = 'C'
    else: letter = 'D'
    print(f"{student}: {scores} -> Avg: {avg:.2f} -> Grade: {letter}")
```

**Explanation:** `setdefault(name, [])` creates an empty list for new students, then `.append(score)` adds the score. This avoids checking if the key exists each time.
