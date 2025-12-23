### Applying Default Parameters in Function Definitions

### Hook (3 minutes)

"Ever use a copy machine? The settings are pre-configured: single-sided, one copy, black and white. But you CAN change them! This is how default parameters work - sensible defaults with customization when needed."

Think about ordering coffee - default is medium with no sugar, but you can say "large with 2 sugars" to override!

### Section 1: The Problem - Too Many Required Arguments (4 minutes)

**Inflexible:**
```python
def greet(name, greeting, punctuation):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice", "Hello", "!")
greet("Bob", "Hello", "!")    # Repeating "Hello" and "!"
greet("Charlie", "Hello", "!")
```

**Solution - default parameters:**
```python
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")              # Hello, Alice!
greet("Bob")                # Hello, Bob!
greet("Charlie", "Hi")      # Hi, Charlie!
greet("David", "Hey", "?")  # Hey, David?
```

### Section 2: What Are Default Parameters? (5 minutes)

A default parameter has a pre-assigned value in the function definition. If no argument is provided, the default is used.

**Syntax:**
```python
def function_name(param1, param2=default_value):
    pass
```

**Example:**
```python
def power(base, exponent=2):  # exponent defaults to 2
    return base ** exponent

print(power(5))      # 5^2 = 25
print(power(5, 3))   # 5^3 = 125
print(power(2, 4))   # 2^4 = 16
```

**Key points:**
- Default parameters make arguments optional
- If not provided, default value is used
- Can override by passing a value
- Defaults must come after regular parameters

### Section 3: Syntax Rules (4 minutes)

**Rule 1: Defaults after required parameters**
```python
# WRONG
def greet(greeting="Hello", name):  # SyntaxError!
    pass

# CORRECT
def greet(name, greeting="Hello"):
    pass
```

**Rule 2: Multiple defaults**
```python
def make_coffee(size="medium", sugar=0, milk=False):
    print(f"{size} coffee, {sugar} sugar, milk: {milk}")

make_coffee()               # All defaults
make_coffee("large")        # Override size
make_coffee("small", 2)     # Override size and sugar
```

**Rule 3: Mixing required and default**
```python
def order_pizza(size, topping="cheese", extra=False):
    print(f"{size} pizza with {topping}")

order_pizza("large")              # Must provide size
order_pizza("medium", "pepperoni")
```

### Section 4: Using Default Parameters (5 minutes)

**Configuration:**
```python
def connect_to_server(host, port=8080, timeout=30):
    print(f"Connecting to {host}:{port}, timeout: {timeout}s")

connect_to_server("localhost")
connect_to_server("example.com", 443)
```

**Formatting:**
```python
def format_price(amount, currency="USD", decimals=2):
    return f"{currency} {amount:.{decimals}f}"

print(format_price(19.99))        # USD 19.99
print(format_price(19.99, "EUR")) # EUR 19.99
```

### Section 5: Keyword Arguments with Defaults (4 minutes)

```python
def create_user(username, role="user", active=True, notifications=True):
    print(f"User: {username}, Role: {role}")
    print(f"Active: {active}, Notifications: {notifications}")

create_user("alice", notifications=False)  # Skip some defaults
create_user("bob", active=False)
```

### Section 6: Common Use Cases (3 minutes)

```python
def print_header(text, width=50, char="="):
    print(char * width)
    print(text.center(width))
    print(char * width)

print_header("Welcome")        # Defaults
print_header("Hello", 30, "*") # Custom

def calculate_shipping(weight, distance, express=False):
    cost = weight * 0.5 + distance * 0.1
    return cost * 2 if express else cost
```

### Section 7: Common Mistakes (3 minutes)

**Mistake 1: Mutable defaults**
```python
# DANGEROUS
def add_item(item, items=[]):  # BAD!
    items.append(item)
    return items

# CORRECT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

**Mistake 2: Wrong order**
```python
# WRONG
def greet(greeting="Hello", name):  # SyntaxError!
    pass

# CORRECT
def greet(name, greeting="Hello"):
    pass
```

### Section 8: Practice (2 minutes)

Write `send_email` with recipient (required), subject (default "No Subject"), urgent (default False):
```python
def send_email(recipient, subject="No Subject", urgent=False):
    priority = "HIGH" if urgent else "NORMAL"
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")

send_email("alice@example.com")
send_email("bob@example.com", "Meeting", True)
```

### Wrap-Up (2 minutes)

**Key takeaways:**
1. Default parameters provide fallback values
2. Make arguments optional and functions flexible
3. Required parameters before defaults
4. Override by position or keyword
5. Avoid mutable defaults (use None)

**Template:**
```python
def function_name(required, optional=default):
    pass

function_name(value1)         # Uses default
function_name(value1, value2) # Overrides
```

Congratulations! You now know Python function fundamentals!
