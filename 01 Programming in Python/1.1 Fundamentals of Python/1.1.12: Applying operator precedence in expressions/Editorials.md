# Editorials: Apply Operator Precedence

## Problem 1
```python
print(5 + 3 * 2)    # 11 (3*2=6, then 5+6)
print(10 - 4 / 2)   # 8.0 (4/2=2.0, then 10-2.0)
print(2 ** 3 + 1)   # 9 (2**3=8, then 8+1)
```

## Problem 2
```python
# Equal 16: Force addition first
(2 + 3) * 4 = 5 * 4 = 20  # Oops, that's 20

# Equal 16: Need different approach
2 + 3 * 4 + 2 = 2 + 12 + 2 = 16

# Equal 20: 
(2 + 3) * 4 = 20
```

## Problem 3
```python
result = 10 + 5 * 2 ** 2 - 3
# Step 1: 2 ** 2 = 4
# Step 2: 5 * 4 = 20
# Step 3: 10 + 20 = 30
# Step 4: 30 - 3 = 27
```

## Problem 4
```python
# Wrong
avg = total + count / 2

# Correct
avg = (total + count) / 2
```

## Problem 5
```python
result = (5 + 3) * 2 ** 2 - 10 // 3 + 1
# Step 1: (5 + 3) = 8
# Step 2: 2 ** 2 = 4
# Step 3: 8 * 4 = 32
# Step 4: 10 // 3 = 3
# Step 5: 32 - 3 = 29
# Step 6: 29 + 1 = 30
```
