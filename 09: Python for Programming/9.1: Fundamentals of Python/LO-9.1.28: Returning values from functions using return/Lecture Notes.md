# Lecture Notes: Return Values from Functions

## Introduction

The `return` statement introduces **output** from functions - the ability to send computed values back to the caller. This completes the **input-process-output** cycle that makes functions powerful building blocks.

### Why Return Exists

**The usability problem**: Functions that only print are limited - you can't use their results in calculations, store them, or pass them to other functions.
**Return solution**: Functions compute values AND send them back for further use. This enables **function composition** - using outputs of one function as inputs to another.

**Mathematical parallel**: Functions in math return values: f(x) = x² returns a value you can use. Programming functions work the same way!

### Real-World Analogy

Return is like **a calculator**:
- **Input**: You press 5 + 3
- **Processing**: Calculator computes internally
- **Return**: Shows "8" on display (returns value you can copy/use)
- **vs Display only**: If calculator just showed "8" but you couldn't copy it, useless!

Or like **a vending machine**:
- **Input**: You insert money, press button
- **Processing**: Machine finds item
- **Return**: Item drops into slot (returns physical product)
- **You get output**: Can now eat/use the item elsewhere!

### Return vs Print: The Critical Difference

This is one of the most confusing concepts for beginners:
- **print()**: Shows something to the user (side effect, no value returned)
- **return**: Sends value back to the code (for further computation)

```python
def bad_add(a, b):
    print(a + b)  # Just displays, returns None

result = bad_add(5, 3)  # Displays 8
# result is None! Can't use it!
```

**Professional code uses return** - printing is only for final user output.

### The Power of Composition

Return enables **chaining functions** - outputs become inputs:
```python
result = function3(function2(function1(data)))
```

This **functional composition** is fundamental to modern programming - building complex operations from simple, reusable pieces.

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
