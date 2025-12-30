## Pre-Read: Perform Element-wise Operations

### What You'll Learn

In this session, you'll discover one of NumPy's most powerful features: element-wise operations. You'll learn how to perform mathematical operations on entire arrays without writing loops, making your code faster, cleaner, and more efficient.

### Why It Matters

Element-wise operations are fundamental for:

1. **Data transformation**: Apply calculations to entire datasets at once
2. **Performance**: NumPy operations are much faster than Python loops
3. **Code clarity**: Write concise, readable code
4. **Scientific computing**: Essential for mathematical and statistical operations

Real-world examples:
- Convert temperatures from Fahrenheit to Celsius for entire datasets
- Apply discounts to all product prices
- Calculate percentage changes across time series
- Normalize data for machine learning

### Key Concepts Preview

**Element-wise Operations:**
- Operations apply to each element independently
- No loops needed
- Works with scalars and arrays
- Arrays must have compatible shapes

**Basic syntax:**
```python
arr = np.array([10, 20, 30, 40, 50])

# Scalar operations
result = arr + 5   # [15, 25, 35, 45, 55]
result = arr * 2   # [20, 40, 60, 80, 100]
result = arr ** 2  # [100, 400, 900, 1600, 2500]

# Array operations
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
result = arr1 + arr2  # [11, 22, 33]
```

**Comparison operations:**
```python
arr = np.array([10, 25, 30, 15, 40])
result = arr > 20  # [False, True, True, False, True]
```

### What to Expect

You'll learn:
1. Basic arithmetic operations (+, -, *, /, **)
2. Operations between arrays
3. Comparison operations
4. In-place operations (+=, -=, etc.)
5. Floor division and absolute value
6. Practical applications in data analysis

### Prepare

Make sure you have:
- NumPy installed
- Understanding of basic arithmetic operators
- Completed NumPy array creation lessons
- Basic Python knowledge

### Quick Example

Try to predict the output:
```python
prices = np.array([100, 200, 150, 250])
discount = 0.10  # 10% discount

# Apply discount
new_prices = prices * (1 - discount)  # ?

# Find expensive items
expensive = prices > 180  # ?

# Double all prices
doubled = prices * 2  # ?
```

Answers:
- new_prices: [90., 180., 135., 225.] (10% off)
- expensive: [False, True, False, True] (200 and 250 > 180)
- doubled: [200, 400, 300, 500]

### Traditional Python vs NumPy

**Without NumPy (using loops):**
```python
prices = [100, 200, 150, 250]
new_prices = []
for price in prices:
    new_prices.append(price * 0.9)
# Slow, verbose
```

**With NumPy (element-wise):**
```python
prices = np.array([100, 200, 150, 250])
new_prices = prices * 0.9
# Fast, concise
```

Element-wise operations eliminate the need for loops and make your code significantly faster and more readable!
