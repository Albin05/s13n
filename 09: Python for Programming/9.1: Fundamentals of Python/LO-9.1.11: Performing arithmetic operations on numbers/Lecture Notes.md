# Lecture Notes: Perform Arithmetic Operations

## Introduction
Python provides comprehensive arithmetic operators for all types of calculations, from basic math to complex scientific formulas.

### Why Arithmetic Operators Are Fundamental

At its core, a computer is a **mathematical machine**. The word "computer" literally means "one who computes." Before electronic computers, "computers" were people who performed calculations!

**Historical perspective**:
- **1940s**: First electronic computers were built to calculate artillery tables and break codes
- **1950s**: FORTRAN (FORmula TRANslation) was created specifically for scientific calculations
- **Today**: Every app uses arithmetic - from social media (likes + 1) to games (damage calculations) to finance

Even tasks that don't seem mathematical involve arithmetic:
- **Text processing**: Character positions, string lengths
- **Graphics**: Pixel coordinates, color values
- **Networks**: Packet sizes, transfer speeds
- **Time**: Unix timestamps are numbers representing seconds since 1970

### Operators as Functions

In mathematics and computer science, operators are just **special syntax for functions**:

```python
# These are equivalent:
result = 5 + 3        # Operator syntax
result = add(5, 3)    # Function syntax (if 'add' existed)
```

**Why use operators instead of functions?**
- **Readability**: `a + b` is clearer than `add(a, b)`
- **Familiarity**: Matches mathematical notation
- **Conciseness**: Less typing, easier to scan

This is called **operator overloading** or **syntactic sugar** - making code sweeter (easier) to write and read.

### Real-World Analogy

Think of arithmetic operators like **tools in a toolbox**:
- **Addition (+)**: Like combining piles - put two piles together
- **Subtraction (-)**: Like removing items - take some away
- **Multiplication (*)**: Like repeated addition - "3 bags of 5 apples = 15 apples"
- **Division (/)**: Like splitting equally - "share 12 cookies among 4 people"
- **Modulo (%)**: Like the remainder when dividing - "13 cookies, 5 people, 3 left over"
- **Exponentiation (**)**: Like repeated multiplication - "2³ = 2×2×2"

Each tool has its specific purpose, and you choose the right one for the job.

---


## Basic Arithmetic Operators

### Addition (+)
```python
a = 10
b = 5
sum_result = a + b
print(sum_result)  # 15
```

**With different types**:
```python
int_num = 10
float_num = 3.5
result = int_num + float_num
print(result)  # 13.5 (becomes float)
```

### Subtraction (-)
```python
a = 10
b = 3
difference = a - b
print(difference)  # 7
```

**Can produce negatives**:
```python
result = 5 - 10
print(result)  # -5
```

### Multiplication (*)
```python
price = 19.99
quantity = 3
total = price * quantity
print(total)  # 59.97
```

**String repetition** (bonus):
```python
text = "Hello" * 3
print(text)  # "HelloHelloHello"
```

### Division (/)

**Always returns float**:
```python
result = 10 / 2
print(result)        # 5.0 (float, not 5)
print(type(result))  # <class 'float'>

result = 10 / 3
print(result)        # 3.3333333...
```

---

## Special Arithmetic Operators

### Why Python Has Two Division Operators

Most languages have just one division operator, but Python 3 has two: `/` and `//`. This was a deliberate design choice.

**The problem**: In Python 2 and many other languages, `/` behaved differently with ints vs floats:
```python
# Python 2 behavior (confusing!)
10 / 3    # → 3 (integer division)
10.0 / 3  # → 3.333... (float division)
```

This caused countless bugs when programmers forgot about integer division.

**Python 3's solution**: Make division behavior explicit:
- `/` **always** returns float (predictable)
- `//` **always** returns integer (when you need it)

This is Python's philosophy: "Explicit is better than implicit."

### Integer Division (//)

Returns integer, discarding remainder:
```python
result = 10 // 3
print(result)  # 3 (not 3.333...)

result = 15 // 4
print(result)  # 3

result = 20 // 5
print(result)  # 4
```

**With negatives**:
```python
result = -10 // 3
print(result)  # -4 (floors toward negative infinity)
```

### Modulo (%)

Returns remainder after division:
```python
print(10 % 3)   # 1 (10 = 3×3 + 1)
print(15 % 4)   # 3 (15 = 4×3 + 3)
print(20 % 5)   # 0 (20 = 5×4 + 0, no remainder)
```

**Practical use - Check even/odd**:
```python
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Get last digit**:
```python
number = 12345
last_digit = number % 10
print(last_digit)  # 5
```

### Exponentiation (**)

Raises number to a power:
```python
result = 2 ** 3
print(result)  # 8 (2³ = 2 × 2 × 2)

result = 5 ** 2
print(result)  # 25 (5²)

result = 10 ** 0
print(result)  # 1 (anything⁰ = 1)
```

**Square roots** (using fractional exponent):
```python
result = 16 ** 0.5
print(result)  # 4.0 (√16)
```

---

## Augmented Assignment Operators

Shortcuts for updating variables:

### Basic Augmented Operators

```python
x = 10

# Long way
x = x + 5
print(x)  # 15

# Short way (augmented assignment)
x += 5
print(x)  # 20
```

### All Augmented Operators

```python
score = 100

score += 50   # score = score + 50 → 150
score -= 25   # score = score - 25 → 125
score *= 2    # score = score * 2 → 250
score //= 10  # score = score // 10 → 25
score %= 7    # score = score % 7 → 4
score **= 2   # score = score ** 2 → 16
```

### When to Use Augmented Assignment

```python
# Updating game score
player_score = 0
player_score += 100  # Completed level
player_score += 50   # Bonus points
player_score -= 20   # Penalty

# Doubling a value
money = 100
money *= 2  # Now have 200

# Halving a value
portions = 8
portions //= 2  # Now have 4
```

---

## Practical Examples

### Example 1: Simple Calculator
```python
num1 = 15
num2 = 4

print(f"Sum: {num1 + num2}")           # 19
print(f"Difference: {num1 - num2}")    # 11
print(f"Product: {num1 * num2}")       # 60
print(f"Division: {num1 / num2}")      # 3.75
print(f"Integer Div: {num1 // num2}")  # 3
print(f"Remainder: {num1 % num2}")     # 3
print(f"Power: {num1 ** 2}")           # 225
```

### Example 2: Temperature Conversion
```python
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")  # 25°C = 77.0°F
```

### Example 3: Compound Interest
```python
principal = 1000
rate = 0.05  # 5%
years = 3

amount = principal * (1 + rate) ** years
interest = amount - principal

print(f"Final amount: ${amount:.2f}")
print(f"Interest earned: ${interest:.2f}")
```

### Example 4: Bill Splitter
```python
total_bill = 127.50
num_people = 4
tip_percent = 0.18

tip = total_bill * tip_percent
total_with_tip = total_bill + tip
per_person = total_with_tip / num_people

print(f"Bill: ${total_bill}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Total: ${total_with_tip:.2f}")
print(f"Per person: ${per_person:.2f}")
```

---

## Operator Summary Table

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1.666...` |
| `//` | Integer Division | `5 // 3` | `1` |
| `%` | Modulo | `5 % 3` | `2` |
| `**` | Exponentiation | `5 ** 3` | `125` |

---

## Key Takeaways

1. **Seven arithmetic operators**: +, -, *, /, //, %, **
2. **Division** (`/`) always returns float
3. **Integer division** (`//`) returns integer, drops decimal
4. **Modulo** (`%`) returns remainder
5. **Exponentiation** (`**`) calculates powers
6. **Augmented assignment** (+=, -=, etc.) updates variables efficiently
7. **Mixed types** (int + float) return float
8. **Order matters** (we'll learn precedence in LO-12)

---

## Practice Exercises

Try these calculations:
```python
# Exercise 1: Calculate circle area
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"Area: {area}")

# Exercise 2: Convert hours to seconds
hours = 2
minutes = hours * 60
seconds = minutes * 60
print(f"{hours} hours = {seconds} seconds")

# Exercise 3: Check if number is even
number = 42
is_even = (number % 2 == 0)
print(f"{number} is even: {is_even}")
```
