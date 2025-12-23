### Returning Values from Functions Using Return

### Hook (3 minutes)

"Our functions print results, but imagine if your calculator showed the answer but didn't let you USE it in another calculation. Frustrating, right?"

Today: Learn how to make functions send data BACK using return statements!

Think of a vending machine - it doesn't just SHOW you the snack, it GIVES it to you. The `return` statement works the same way!

### Section 1: The Problem - Functions That Only Print (4 minutes)

**Current limitation:**
```python
def add(a, b):
    result = a + b
    print(result)  # Just prints

add(5, 3)  # Prints: 8

# But we can't use the result!
total = add(5, 3)  # Prints: 8
print(total)       # Prints: None
```

**What we need:**
```python
def add(a, b):
    return a + b  # Give back the result

total = add(5, 3)   # total = 8
print(total)        # Prints: 8
doubled = total * 2 # We can use it!
```

### Section 2: What is Return? (5 minutes)

The `return` statement sends a value back to the caller and immediately exits the function.

**Syntax:**
```python
def function_name():
    return value  # Send value back
```

**Example:**
```python
def get_greeting():
    return "Hello, World!"

message = get_greeting()
print(message)  # Hello, World!
```

**Key points:**
- `return` gives a value back
- Function stops when it hits `return`
- Store returned value in a variable
- Use returned value in expressions

### Section 3: Return vs Print (4 minutes)

**Print version:**
```python
def add_print(a, b):
    print(a + b)  # Shows on screen

x = add_print(3, 4)  # Prints: 7
print(x)             # Prints: None
```

**Return version:**
```python
def add_return(a, b):
    return a + b  # Gives value back

x = add_return(3, 4)  # x = 7
print(x)              # Prints: 7
```

**Key difference:**
- `print()` displays to screen (for humans)
- `return` gives data back (for programs)

### Section 4: Using Returned Values (5 minutes)

**In calculations:**
```python
def square(n):
    return n * n

result = square(5)                # 25
total = square(3) + square(4)     # 9 + 16 = 25
```

**In conditionals:**
```python
def is_adult(age):
    return age >= 18

if is_adult(20):
    print("Can vote!")
```

### Section 5: Returning Different Data Types (4 minutes)

**Strings, numbers, booleans:**
```python
def make_greeting(name):
    return f"Hello, {name}!"

def is_even(num):
    return num % 2 == 0
```

**Multiple values:**
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9])
```

### Section 6: Return Stops Execution (3 minutes)

```python
def check_number(num):
    if num > 10:
        return "Too big!"
    if num < 0:
        return "Negative!"
    return "Perfect!"

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```

### Section 7: Common Mistakes (3 minutes)

```python
# Forgetting to return
def add(a, b):
    result = a + b  # Forgot return!

# Not capturing
square(5)  # Value lost!
result = square(5)  # Correct

# Code after return
def greet():
    return "Hello"
    print("World")  # Never executes!
```

### Section 8: Real-World Application (3 minutes)

```python
def is_valid_password(password):
    if len(password) < 8:
        return False
    return True

def calculate_total(price, quantity, tax_rate):
    return price * quantity * (1 + tax_rate)

order_total = calculate_total(10.99, 3, 0.08)
```

### Section 9: Practice (2 minutes)

Write `calculate_discount` that returns final price:
```python
def calculate_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount

final = calculate_discount(100, 20)
print(f"Final: ${final}")  # $80.00
```

### Wrap-Up (2 minutes)

**Key takeaways:**
1. `return` sends value back to caller
2. Return stops execution immediately
3. Returned values can be stored and used
4. Print shows output; return gives usable data
5. No return means function returns `None`

**Template:**
```python
def function_name(params):
    result = some_value
    return result

value = function_name(args)
```
