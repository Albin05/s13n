# Pre-Read: Returning Values from Functions Using Return

## Why Return?

Functions without return are like **ovens that cook but never open** - food cooks inside, but you can't get it out to eat! Return lets functions **give back** their results.

### Simple Analogy

Think of return like **an ATM dispensing cash**:
- **Input**: You insert card, enter PIN, request $100
- **Processing**: ATM validates, checks balance, prepares money
- **Return**: Money comes out of slot (this is the return!)
- **You use it**: Take money, buy things elsewhere

Or like **a microwave**:
- **Input**: Put food in, set timer
- **Processing**: Heats food inside
- **Return**: Beep! Food is ready (you take it out)
- **vs. No return**: Food cooks but stays locked inside forever!

### Return vs Print: The Big Confusion

**Beginners' biggest mistake**: Thinking `print()` and `return` are the same.
- **print()**: Shows something to YOU (the human)
- **return**: Gives something to THE CODE (for further use)

```python
def bad_calculator(a, b):
    print(a + b)  # Shows answer, but code can't use it!

# This doesn't work!
total = bad_calculator(5, 3) + 10  # Error! Can't add None + 10
```

Return makes functions **useful**, not just pretty displays!

## What You'll Learn
In this lesson, you'll learn how to use the `return` statement to send values back from functions, allowing you to use function results in other parts of your code.

## Why This Matters
So far, functions just print output. But what if you want to:
- Use a function's result in a calculation
- Store a function's result in a variable
- Pass a function's result to another function
- Make decisions based on a function's result

The `return` statement lets functions send data back to the caller, making them infinitely more useful.

---

## What is Return?

The `return` statement sends a value back from a function to wherever it was called.

```python
def add(a, b):
    return a + b  # Send the sum back

result = add(5, 3)  # result gets 8
print(result)       # 8
```

**Key difference:**
- `print()` → Shows output on screen
- `return` → Sends value back to use in code

---

## Return vs Print

### With Print (Limited)

```python
def add(a, b):
    print(a + b)  # Just displays

add(5, 3)  # Shows: 8
x = add(5, 3)  # x gets None (not the sum!)
print(x)  # None
```

### With Return (Flexible)

```python
def add(a, b):
    return a + b  # Send value back

result = add(5, 3)  # result gets 8
x = add(10, 20)     # x gets 30
total = add(result, x)  # Can use in more calculations!
print(total)  # 38
```

---

## Simple Examples

### Example 1: Calculate and Return

```python
def square(n):
    return n * n

x = square(5)  # x = 25
y = square(10) # y = 100
z = x + y      # z = 125
print(z)       # 125
```

### Example 2: Return in Conditions

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

if is_even(4):
    print("4 is even")  # This prints!

if is_even(7):
    print("7 is even")  # This doesn't run
```

---

## Return Stops Function Execution

Once `return` runs, the function exits immediately:

```python
def check_age(age):
    if age < 18:
        return "Too young"  # Exit here if True
    return "Old enough"     # Only runs if age >= 18

print(check_age(15))  # "Too young"
print(check_age(25))  # "Old enough"
```

---

## Real-World Examples

### Example 1: Calculate Discount

```python
def apply_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price

shirt_price = apply_discount(50, 20)   # $40
shoe_price = apply_discount(100, 15)   # $85
total = shirt_price + shoe_price       # $125
print(f"Total: ${total}")
```

### Example 2: Validate Password

```python
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

password = input("Enter password: ")
if is_strong_password(password):
    print("Password accepted!")
else:
    print("Password too weak!")
```

---

## Returning Multiple Values

Python can return multiple values using tuples:

```python
def get_user_info():
    name = "Alice"
    age = 25
    city = "NYC"
    return name, age, city  # Returns tuple

name, age, city = get_user_info()
print(f"{name}, {age}, {city}")  # Alice, 25, NYC
```

---

## Try It Yourself (Before Class)

Run this code:

```python
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

a, p = calculate_rectangle(5, 3)
print(f"Area: {a}, Perimeter: {p}")
```

**Questions:**
1. What values do `a` and `p` get?
2. Try returning just `area` without `perimeter` - what changes?
3. What happens if you don't return anything?

---

## Key Takeaways

Before class, remember:
1. **return sends values back** - for use in other code
2. **return exits function** - code after return doesn't run
3. **return vs print** - return for data, print for display
4. **Can return anything** - numbers, strings, booleans, tuples
5. **No return = None** - functions return None by default

## What's Next?

In the live session, we'll:
- Practice writing functions with return values
- Use returned values in complex calculations
- Understand when to return vs print
- Learn about returning multiple values
- Handle functions that return None

See you in class!
