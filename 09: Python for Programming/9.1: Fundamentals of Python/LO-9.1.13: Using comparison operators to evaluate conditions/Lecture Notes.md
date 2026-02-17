# Lecture Notes: Use Comparison Operators

## Introduction

Comparison operators are the foundation of **decision-making** in programs. They allow code to ask questions and respond differently based on the answers.

### Why Comparison Operators Exist

Every useful program makes decisions:
- **ATM**: Is PIN correct? Is balance sufficient?
- **Game**: Is health > 0? Did score >= high score?
- **Login**: Does password match? Is account active?

Without comparisons, programs would just execute the same instructions every time - no intelligence, no adaptation.

### The Foundation of Logic

Comparison operators implement **Boolean logic**, invented by George Boole in the 1800s. This mathematical system deals with truth values (True/False) and forms the basis of:
- All computer logic gates
- Database queries (SQL WHERE clauses)
- Conditional statements in every programming language
- Search engine filters

### Real-World Analogy

Comparison operators are like **quality control inspectors**:
- Inspector checks: "Is this item > 5 inches?" → True or False
- Inspector checks: "Does weight == specification?" → True or False
- Based on answer, item passes or fails

Or think of them like **bouncers at a club**:
- "Is age >= 21?" → True: enter, False: denied
- "Is name on list?" → True: VIP entrance, False: regular line

## Comparison Operators

Comparison operators compare two values and return a **boolean** result: `True` or `False`.


### The Six Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

## Examples

### Equal To (`==`)

```python
age = 18
print(age == 18)  # True
print(age == 20)  # False

name = "Alice"
print(name == "Alice")  # True
print(name == "Bob")    # False
```

**Common Mistake**: Using `=` instead of `==`
```python
# Wrong - This assigns 18 to age
if age = 18:  # SyntaxError!

# Correct - This checks if age equals 18
if age == 18:  # Correct!
```

### Not Equal To (`!=`)

```python
status = "pending"
print(status != "completed")  # True
print(status != "pending")    # False
```

### Greater Than (`>`)

```python
score = 85
print(score > 75)   # True
print(score > 90)   # False
print(score > 85)   # False (not greater, equal!)
```

### Less Than (`<`)

```python
temperature = 25
print(temperature < 30)  # True
print(temperature < 20)  # False
print(temperature < 25)  # False (not less, equal!)
```

### Greater Than or Equal To (`>=`)

```python
age = 18
print(age >= 18)  # True (equal counts!)
print(age >= 16)  # True
print(age >= 21)  # False
```

### Less Than or Equal To (`<=`)

```python
attempts = 3
print(attempts <= 3)  # True (equal counts!)
print(attempts <= 5)  # True
print(attempts <= 2)  # False
```

## Comparing Different Data Types

### Numbers

```python
# Comparing integers and floats works
print(5 == 5.0)      # True
print(10 > 9.5)      # True
print(3.14 <= 3.14)  # True
```

### Strings

```python
# Strings are compared alphabetically
print("apple" < "banana")   # True
print("zebra" > "aardvark") # True
print("ABC" == "abc")       # False (case-sensitive!)
```

### Type Incompatibility

```python
# Can't meaningfully compare different types
print(5 == "5")      # False (different types!)
print(10 < "20")     # TypeError in Python 3
```

## Storing Comparison Results

```python
# Comparisons return boolean values
age = 20
is_adult = age >= 18
print(is_adult)        # True
print(type(is_adult))  # <class 'bool'>

# Can use in conditions
temperature = 35
is_hot = temperature > 30
print(f"Is it hot? {is_hot}")  # Is it hot? True
```

## Real-World Applications

### Age Verification

```python
age = int(input("Enter your age: "))
can_vote = age >= 18
can_drive = age >= 16

print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
```

### Grade Checker

```python
score = 85
is_passing = score >= 60
is_excellent = score >= 90

print(f"Passing: {is_passing}")    # True
print(f"Excellent: {is_excellent}")  # False
```

### Password Validation

```python
password = input("Enter password: ")
min_length = len(password) >= 8
print(f"Password long enough: {min_length}")
```

### Temperature Alert

```python
temperature = 38
is_fever = temperature >= 37.5
print(f"Has fever: {is_fever}")  # True
```

## Common Mistakes

### 1. Using `=` Instead of `==`

```python
# Wrong
x = 5
if x = 5:  # SyntaxError
    print("Five")

# Correct
if x == 5:
    print("Five")
```

### 2. Forgetting Type Matters

```python
user_input = input("Enter age: ")  # Returns string!
# user_input = "18" (string)

# Wrong comparison
if user_input >= 18:  # TypeError!

# Correct - convert first
age = int(user_input)
if age >= 18:
    print("Adult")
```

### 3. Confusing `>` and `>=`

```python
score = 60
# Be clear about boundaries
print(score > 60)   # False
print(score >= 60)  # True
```

## Practice Exercise

Try to predict the output:

```python
a = 10
b = 20
c = 10

print(a == c)    # ?
print(a != b)    # ?
print(b > a)     # ?
print(a >= c)    # ?
print(b <= 15)   # ?
```

<details>
<summary>Answer</summary>

```python
print(a == c)    # True
print(a != b)    # True
print(b > a)     # True
print(a >= c)    # True
print(b <= 15)   # False
```
</details>

## Key Takeaways

1. **Six operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
2. **Return boolean**: All comparisons return `True` or `False`
3. **Type-aware**: Compare compatible types
4. **Not assignment**: `==` checks equality, `=` assigns
5. **Store results**: Can save comparison results in variables
