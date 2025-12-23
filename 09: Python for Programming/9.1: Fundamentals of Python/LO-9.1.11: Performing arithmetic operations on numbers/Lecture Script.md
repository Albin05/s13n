# Lecture Script: LO-11 Perform Arithmetic Operations

## Duration: 15-20 minutes

## [0:00-0:02] Hook
**Say**: "Python is a powerful calculator! But it has special operators you might not know about. Let's explore them all!"

## [0:02-0:08] Basic Operators (6 min)

**Demonstrate each**:
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333... (ALWAYS float!)
```

**Emphasize**: `/` always returns float, even `10 / 2` gives `5.0`

## [0:08-0:14] Special Operators (6 min)

**Integer Division**:
```python
print(10 // 3)  # 3 (drops decimal)
```
**Say**: "When you can't split a cookie!"

**Modulo**:
```python
print(10 % 3)   # 1 (remainder)
```
**Say**: "Leftover after division"

**Exponentiation**:
```python
print(2 ** 3)   # 8 (2 cubed)
```

## [0:14-0:18] Augmented Assignment (4 min)

**Show the shortcut**:
```python
score = 100
score += 50   # Instead of: score = score + 50
print(score)  # 150
```

**Demonstrate**:
- `+=`, `-=`, `*=`, `//=`

## [0:18-0:20] Practice & Wrap (2 min)

**Exercise**: Calculate total cost
```python
price = 19.99
quantity = 3
tax_rate = 0.08
# Calculate total with tax
```

**Answer**:
```python
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
```

**Preview**: "Next: We'll learn which operators execute first - that's operator precedence!"
