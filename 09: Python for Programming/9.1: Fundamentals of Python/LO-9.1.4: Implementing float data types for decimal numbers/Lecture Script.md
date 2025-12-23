# Lecture Script: LO-4 Implement Float Data Types

## [0:00-0:02] Hook
**Say**: "Can you buy something for exactly $19.99? Not $19 or $20 - you need decimals! That's why we have floats."

## [0:02-0:07] Floats Explained (5 min)
- Define floats (numbers with decimals)
- Show examples
- Demonstrate `type()`

## [0:07-0:12] Precision Demo (5 min)
**Show the surprise**:
```python
print(0.1 + 0.2)  # 0.30000000000000004
```
Explain why (binary representation)

## [0:12-0:15] Practice (3 min)
Calculate price with tax:
```python
price = 29.99
tax_rate = 0.08
total = price * (1 + tax_rate)
```
