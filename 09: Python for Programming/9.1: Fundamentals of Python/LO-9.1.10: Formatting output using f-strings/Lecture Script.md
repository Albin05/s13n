# Lecture Script: LO-10 Format Output with F-strings

## [0:00-0:02] Hook
**Say**: "Tired of writing `'text' + str(variable) + 'more text'`? F-strings are magic!"

## [0:02-0:07] F-string Basics (5 min)
```python
name = "Alice"
age = 25
print(f"Hi {name}, age {age}")
```

Show how much cleaner than concatenation!

## [0:07-0:12] Expressions & Formatting (5 min)
```python
price = 19.99
print(f"Price: ${price:.2f}")
print(f"Double: ${price * 2:.2f}")
```

## [0:12-0:15] Practice (3 min)
Create a receipt with f-strings:
- Item name
- Price
- Quantity
- Total (calculated)
