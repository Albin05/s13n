# Lecture Notes: Return Values from Functions

## Return Statement

Functions can send values back using `return`.


### Basic Syntax

```python
def function_name():
    return value
```

## Examples

### Example 1: Return a Number

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

### Example 2: Return a String

```python
def make_greeting(name):
    return f"Hello, {name}!"

message = make_greeting("Alice")
print(message)  # Hello, Alice!
```

### Example 3: Return Boolean

```python
def is_adult(age):
    return age >= 18

if is_adult(20):
    print("Can vote")
# Output: Can vote
```

## Return vs Print

```python
# Print (displays, returns None)
def add_print(a, b):
    print(a + b)

result = add_print(5, 3)  # Displays 8
print(result)  # None

# Return (sends value back)
def add_return(a, b):
    return a + b

result = add_return(5, 3)  # Returns 8
print(result)  # 8
```

## Multiple Return Statements

```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(5))   # Positive
print(check_number(-3))  # Negative
print(check_number(0))   # Zero
```

## Key Takeaways

1. **return**: Sends value back to caller
2. **Exits function**: Stops execution immediately
3. **Store result**: Assign to variable
4. **Use in expressions**: Can use directly in calculations
5. **return vs print**: return gives value, print displays
