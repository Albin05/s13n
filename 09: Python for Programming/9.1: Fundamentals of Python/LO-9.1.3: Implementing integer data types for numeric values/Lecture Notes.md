# Lecture Notes: Implement Integer Data Types

## Introduction
Integers (int) are one of Python's fundamental data types. They represent whole numbers and are used for counting, indexing, and any quantity that doesn't require decimal precision.

---


## What are Integers?

### Definition
**Integer**: A whole number with no decimal point
- Can be positive: `5`, `100`, `2024`
- Can be negative: `-3`, `-50`, `-999`
- Can be zero: `0`

### Why Integers Are Fundamental

Integers are the mathematical foundation of computing. At the lowest level, computers understand only two states: on (1) and off (0). These binary digits combine to represent integers, which then represent everything else - text, images, videos, and more.

**Historical Note**: Early computers could only work with integers. Decimal numbers (floats) came later and required special hardware. Even today, integer operations are faster than float operations on most processors.

### Real-World Analogy

Think of integers like **counting blocks**:
- You can have 1 block, 2 blocks, 10 blocks
- You can't have 2.5 blocks - blocks are whole units
- Similarly, you can have 5 students, but not 5.3 students

Or think about **floors in a building**:
- Ground floor (0), 1st floor, 2nd floor...
- Basement levels: -1, -2, -3...
- No "floor 2.5"!

### Creating Integer Variables
```python
age = 25
year = 2024
score = 0
temperature = -10
```

### Checking Type
```python
count = 100
print(type(count))  # <class 'int'>
```

---

## Integer Arithmetic

### Addition and Subtraction
```python
a = 10
b = 3

sum_result = a + b
print(sum_result)  # 13

difference = a - b
print(difference)  # 7
```

### Multiplication
```python
price = 5
quantity = 10
total = price * quantity
print(total)  # 50
```

### Division: Two Types

**Regular Division** (`/`) - Always returns float:
```python
result = 10 / 3
print(result)        # 3.3333333...
print(type(result))  # <class 'float'>

result = 10 / 2
print(result)        # 5.0 (still a float!)
```

**Integer Division** (`//`) - Returns integer (floor division):
```python
result = 10 // 3
print(result)        # 3 (drops decimal part)
print(type(result))  # <class 'int'>

result = 10 // 2
print(result)        # 5 (integer)
```

### Modulo Operator (%)
Returns the remainder of division:
```python
print(10 % 3)  # 1 (10 ÷ 3 = 3 remainder 1)
print(15 % 4)  # 3 (15 ÷ 4 = 3 remainder 3)
print(10 % 2)  # 0 (10 ÷ 2 = 5 remainder 0)
```

**Use case - Check if number is even:**
```python
number = 10
if number % 2 == 0:
    print("Even")  # Prints this!
else:
    print("Odd")
```

### Exponentiation
```python
base = 2
exponent = 3
result = base ** exponent
print(result)  # 8 (2³ = 2 × 2 × 2)
```

---

## Integer Properties

### No Size Limit in Python 3

**This is special!** In most programming languages (C, C++, Java), integers have fixed sizes:
- C's `int`: typically -2,147,483,648 to 2,147,483,647 (32 bits)
- Exceed this range → overflow error or wraparound bugs

**Python's advantage**: Arbitrary precision integers
```python
# Python can handle huge numbers!
big_number = 123456789012345678901234567890
even_bigger = big_number ** 100  # Still works!
print(big_number)  # No overflow!
```

**How it works**: Python automatically allocates more memory as needed. The integer 5 takes less memory than 5000000000000, but both work seamlessly.

**Trade-off**: Slightly slower than fixed-size integers, but much safer and easier to use. Python prioritizes **correctness** over raw speed.

**Real-world impact**: No need to worry about integer overflow bugs that have caused:
- The Y2K problem (years stored as 2 digits)
- The 2038 problem (Unix timestamps overflow)
- Financial calculation errors in other languages

### Operations with Mixed Types
```python
int_num = 10
float_num = 3.5

result = int_num + float_num
print(result)        # 13.5
print(type(result))  # <class 'float'> - becomes float!
```

**Rule**: int + float = float

---

## Practical Examples

### Example 1: Calculate Average (Integer Division)
```python
total_score = 475
num_tests = 5

average = total_score // num_tests
print(average)  # 95
```

### Example 2: Split Bill
```python
total_bill = 100
num_people = 3

per_person = total_bill // num_people
print(per_person)  # 33

remainder = total_bill % num_people
print(remainder)  # 1 (someone pays extra dollar)
```

### Example 3: Convert Hours to Minutes
```python
hours = 3
minutes_per_hour = 60

total_minutes = hours * minutes_per_hour
print(total_minutes)  # 180
```

---

## Common Use Cases

| Use Case | Example |
|----------|---------|
| Counting | `student_count = 30` |
| Ages | `age = 25` |
| Years | `year = 2024` |
| Scores | `score = 95` |
| Quantities | `apples = 10` |
| IDs | `user_id = 12345` |

---

## Key Takeaways
1. Integers are whole numbers (no decimals)
2. Use `/` for float division, `//` for integer division
3. Use `%` to get remainder
4. Integer + float = float
5. Python integers have no size limit
6. Use integers when you don't need decimal precision
