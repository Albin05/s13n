### LO-4 Implement Float Data Types (15 minutes)

### Hook (2 minutes)

**Say**: "Can you buy something for exactly $19.99? Not $19 or $20 - you need decimals! That's why we have floats."

```python
price = 19.99
tax = 1.60
total = 21.59  # All floats!
```

### What are Floats (5 minutes)

**Say**: "Floats are numbers with decimal points. Used for money, measurements, scientific calculations."

```python
price = 29.99
height = 5.8
pi = 3.14159

print(type(price))  # <class 'float'>
```

**Key Points**:
- Floats have decimal points
- Can be positive or negative
- Used when precision matters
- Division always returns float

```python
result = 10 / 2  # 5.0 (not 5)
print(type(result))  # <class 'float'>
```

### Float Precision (5 minutes)

**Say**: "Computers can't perfectly represent all decimals. This leads to small errors."

```python
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3!)
```

**Solution - Round when displaying**:
```python
result = 0.1 + 0.2
print(f"{result:.2f}")  # 0.30
```

**Real-World**: Always round currency to 2 decimals for display!

### Practice (3 minutes)

Calculate total with tax:
```python
price = 29.99
tax_rate = 0.08
tax = price * tax_rate
total = price + tax
print(f"Total: ${total:.2f}")  # Total: $32.39
```
