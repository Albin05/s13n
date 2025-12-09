# Pre-Read: Apply Operator Precedence

## Order of Operations (PEMDAS)

Just like in math, Python follows an order:

**P**arentheses
**E**xponents
**M**ultiplication/**D**ivision (left to right)
**A**ddition/**S**ubtraction (left to right)

```python
result = 2 + 3 * 4
print(result)  # 14, not 20!
# Because: 3 * 4 happens first (12), then + 2
```

## Use Parentheses

```python
result = (2 + 3) * 4
print(result)  # 20
# Parentheses force addition first
```

## Examples

```python
# Without parentheses
print(10 + 5 * 2)    # 20 (5*2=10, then +10)

# With parentheses  
print((10 + 5) * 2)  # 30 (10+5=15, then *2)
```

## Key Point
When in doubt, use parentheses!
