### LO-3 Implement Integer Data Types (16 minutes)

### Hook (3 minutes)

**Say**: "What's 10 divided by 3? In math, it's 3.333... But what if you're splitting 10 cookies among 3 people? You can't split a cookie! That's where integer division comes in."

```python
cookies = 10
people = 3
each_gets = 10 // 3  # 3 cookies each
```

### What are Integers (5 minutes)

**Say**: "Integers are whole numbers - no decimals. They can be positive, negative, or zero."

```python
age = 25
year = 2024
count = 0
temperature = -5

print(type(age))  # <class 'int'>
```

**Key Points**:
- Integers have no decimal point
- Can be any size (Python handles big numbers!)
- Used for counting, indexing, IDs

### Integer Operations (5 minutes)

**Say**: "Python has two types of division - regular (/) gives decimals, floor (//) gives integers."

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333... (float!)
print(a // b)  # 3 (integer division)
print(a % b)   # 1 (remainder - modulo)
```

**Real-World**: Modulo (%) checks if number is even/odd!
```python
if num % 2 == 0:
    print("Even")
```

### Practice (3 minutes)

```python
candies = 25
friends = 4

each_gets = candies // friends  # 6
leftover = candies % friends    # 1

print(f"Each friend gets {each_gets} candies")
print(f"{leftover} candy left over")
```

