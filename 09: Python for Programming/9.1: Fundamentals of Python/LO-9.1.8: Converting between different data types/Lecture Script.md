### LO-8 Convert Between Data Types (16 minutes)

### Hook (3 minutes)

**Say**: "What if I ask your age and you type '25'? Python sees text, not a number! We need type conversion."

```python
age_text = "25"
# age_text + 1  # Error! Can't add string and number
age = int(age_text)  # Convert to integer
print(age + 1)  # 26
```

### Conversion Functions (6 minutes)

**Say**: "Python has built-in functions to convert between types: int(), float(), str(), bool()"

```python
# String to number
age_str = "25"
age_int = int(age_str)    # 25 (integer)
price_str = "19.99"
price_float = float(price_str)  # 19.99 (float)

# Number to string
score = 100
score_str = str(score)    # "100" (string)

# To boolean
active = bool(1)          # True
inactive = bool(0)        # False
```

**Key Points**:
- `int()`: Converts to integer (drops decimals!)
- `float()`: Converts to decimal number
- `str()`: Converts to text
- `bool()`: Converts to True/False

**Common Errors**:
```python
int("3.14")  # Error! Can't convert float string directly
int(float("3.14"))  # Works! 3
```

### User Input with Conversion (5 minutes)

**Say**: "Input() always returns strings. Convert them for math!"

```python
age_str = input("Enter age: ")
age = int(age_str)
print(f"Next year you'll be {age + 1}")

# Combined in one line
age = int(input("Enter age: "))
```

**Real-World**: Every form on websites converts your input - age to numbers, prices to floats, etc.

### Practice (2 minutes)

Convert and use values:
```python
# Convert "3.14" → float → int → string
value = "3.14"
as_float = float(value)  # 3.14
as_int = int(as_float)   # 3
as_str = str(as_int)     # "3"
print(f"Final: {as_str}, Type: {type(as_str)}")
```
