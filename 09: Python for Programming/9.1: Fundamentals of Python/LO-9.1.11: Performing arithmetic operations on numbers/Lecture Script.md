### LO-11 Perform Arithmetic Operations (21 minutes)

### Hook (3 minutes)

**Say**: "Python is a powerful calculator! But it has special operators you might not know about. Let's explore them all!"

```python
print(10 + 3)   # Addition
print(10 // 3)  # Floor division (what's this?)
print(10 % 3)   # Modulo (huh?)
```

### Basic Operators (6 minutes)

**Say**: "These are the operators you know from math class."

```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division - ALWAYS returns float!)
```

**Key Points**:
- Addition (+), subtraction (-), multiplication (*) work as expected
- Division (/) ALWAYS returns a float, even if dividing evenly
- Python handles very large numbers automatically

```python
print(10 / 2)  # 5.0 (not 5!)
print(type(10 / 2))  # <class 'float'>
```

### Special Operators (6 minutes)

**Say**: "Python has two special operators for division scenarios."

**Floor Division (//)**: Drops the decimal part
```python
print(10 // 3)  # 3 (not 3.333...)
print(7 // 2)   # 3 (not 3.5)
```

**Modulo (%)**: Returns the remainder
```python
print(10 % 3)   # 1 (10 ÷ 3 = 3 remainder 1)
print(7 % 2)    # 1 (odd number!)
print(8 % 2)    # 0 (even number!)
```

**Power (**)**: Exponentiation
```python
print(2 ** 3)   # 8 (2³)
print(5 ** 2)   # 25 (5²)
```

**Real-World**: Check if a number is even/odd using modulo!
```python
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Augmented Assignment (4 minutes)

**Say**: "Shortcuts for updating variables - you'll use these ALL the time!"

```python
score = 100
score += 50   # Same as: score = score + 50
print(score)  # 150

score -= 20   # Same as: score = score - 20
print(score)  # 130

score *= 2    # Same as: score = score * 2
print(score)  # 260
```

**All augmented operators**: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

### Practice (2 minutes)

Calculate total with tax:
```python
price = 19.99
quantity = 3
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print(f"Total: ${total:.2f}")
```
