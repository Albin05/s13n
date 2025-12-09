# Lecture Notes: Use Comparison Operators

## Comparison Operators

Comparison operators compare two values and return a **boolean** result: `True` or `False`.


---

<div align="center">

![Mathematical operations visualization](https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&q=80)

*Operators allow you to perform operations on data*

</div>

---
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
