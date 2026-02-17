# Lecture Notes: Import Custom Modules

## Import Custom Modules

Creating and importing your own Python modules


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Introduction

Custom modules implement **code organization** - splitting programs into reusable files! Any `.py` file is a module - Python's **modular programming** system. This enables **separation of concerns** - each module handles one responsibility, making code maintainable!

### Why Custom Modules Matter

**Before modules** (monolithic file): Everything in one file - unmaintainable:
```python
# 5000-line file - nightmare!
def user_login(): ...
def database_query(): ...
def send_email(): ...
# 4997 more lines...
# Impossible to navigate!
```

**With modules** (organized): Code split logically:
```python
# auth.py - authentication
def user_login(): ...

# database.py - data access
def query(): ...

# email.py - email handling
def send(): ...
# Clean, organized!
```

**This is modular design** - divide and conquer!

### Historical Context

**Modular programming** from **FORTRAN** (1957) which had separate subroutine files. **Python's import** (1991) based on **Modula-3** (1980s) - literally named for modules!

**The module system**: Python's `import` uses **sys.path** to locate modules. Searches: current directory → standard library → site-packages. **Dynamic loading** - code loaded at runtime, not compile-time!

**Package structure**: Directories with `__init__.py` become packages. Hierarchical organization like file systems. Django, Flask - all structured as packages!

### Real-World Analogies

**Modules like tool organization**:
- **Monolithic**: All tools in one giant box (chaos!)
- **Modular**: Separate toolboxes - plumbing, electrical, carpentry
- **Import**: Grab specific toolbox when needed
**Organization enables finding what you need!**

**Or like library sections**:
```python
import math       # Math section
import datetime   # Time section
import json       # Data section
# Each section has related books!
```

**Or like restaurant kitchen**:
- **main.py**: Head chef coordinating
- **prep.py**: Prep station (helper functions)
- **cooking.py**: Cooking station (main logic)
- **plating.py**: Plating station (output formatting)
**Each station does one job well!**

---
### Key Concepts

Custom modules allow you to:
- Organize code into reusable files
- Split large programs into manageable pieces
- Create your own library of functions
- Share code across multiple scripts
- Build modular applications

### Core Principles

**Module basics**: Any `.py` file is a module, use `import filename` (without .py extension)

### Syntax and Usage

```python
# File: mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# File: main.py
import mymodule

print(mymodule.greet("Alice"))  # Hello, Alice!
print(mymodule.PI)              # 3.14159

# Alternative import styles
from mymodule import greet
from mymodule import greet, PI
from mymodule import *  # Not recommended
```

### Practical Examples

#### Example 1: Basic Custom Module

```python
# File: calculator.py
"""Simple calculator module"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# File: main.py
import calculator

result1 = calculator.add(10, 5)
result2 = calculator.subtract(10, 5)
result3 = calculator.multiply(10, 5)
result4 = calculator.divide(10, 5)

print(f"Add: {result1}")       # Add: 15
print(f"Subtract: {result2}")  # Subtract: 5
print(f"Multiply: {result3}")  # Multiply: 50
print(f"Divide: {result4}")    # Divide: 2.0
```

#### Example 2: Module with Classes

```python
# File: user.py
"""User management module"""

class User:
    """User class for managing user data"""

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True

    def deactivate(self):
        """Deactivate user account"""
        self.is_active = False

    def activate(self):
        """Activate user account"""
        self.is_active = True

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"User: {self.username} ({status})"

class UserManager:
    """Manage multiple users"""

    def __init__(self):
        self.users = []

    def add_user(self, user):
        """Add a user"""
        self.users.append(user)

    def get_active_users(self):
        """Get list of active users"""
        return [u for u in self.users if u.is_active]

    def get_user_count(self):
        """Get total number of users"""
        return len(self.users)

# File: main.py
from user import User, UserManager

# Create users
user1 = User("alice", "alice@example.com")
user2 = User("bob", "bob@example.com")
user3 = User("charlie", "charlie@example.com")

# Manage users
manager = UserManager()
manager.add_user(user1)
manager.add_user(user2)
manager.add_user(user3)

# Deactivate one user
user2.deactivate()

# Get active users
active = manager.get_active_users()
print(f"Active users: {len(active)}")  # Active users: 2

for user in active:
    print(f"  - {user}")
# Output:
#   - User: alice (Active)
#   - User: charlie (Active)
```

#### Example 3: Package Structure

```
my_package/
├── __init__.py           # Makes it a package
├── math_utils.py
├── string_utils.py
└── validators.py
```

```python
# File: my_package/__init__.py
"""My custom package"""
__version__ = "1.0.0"

from .math_utils import add, multiply
from .string_utils import capitalize_words
from .validators import is_valid_email

__all__ = ['add', 'multiply', 'capitalize_words', 'is_valid_email']

# File: my_package/math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# File: my_package/string_utils.py
def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    return text[::-1]

# File: my_package/validators.py
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))

# File: main.py
import my_package
from my_package import math_utils, validators

print(f"Package version: {my_package.__version__}")

# Use functions
result = my_package.add(5, 3)
print(f"5 + 3 = {result}")

text = my_package.capitalize_words("hello world")
print(f"Capitalized: {text}")

email = "test@example.com"
if validators.is_valid_email(email):
    print(f"{email} is valid")
```

#### Example 4: Module with Configuration

```python
# File: config.py
"""Application configuration"""

# Database settings
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'name': 'myapp_db',
    'user': 'admin'
}

# Application settings
APP = {
    'name': 'My Application',
    'version': '1.0.0',
    'debug': True,
    'max_connections': 100
}

# API settings
API = {
    'base_url': 'https://api.example.com',
    'timeout': 30,
    'retry_attempts': 3
}

def get_database_url():
    """Generate database URL"""
    return f"postgresql://{DATABASE['user']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['name']}"

def is_debug_mode():
    """Check if debug mode is enabled"""
    return APP.get('debug', False)

# File: app.py
import config

print(f"App: {config.APP['name']} v{config.APP['version']}")
print(f"Database URL: {config.get_database_url()}")
print(f"Debug mode: {config.is_debug_mode()}")
print(f"API timeout: {config.API['timeout']}s")

# Output:
# App: My Application v1.0.0
# Database URL: postgresql://admin@localhost:5432/myapp_db
# Debug mode: True
# API timeout: 30s
```

#### Example 5: Utility Module with __name__ == "__main__"

```python
# File: utils.py
"""Utility functions"""

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

def format_percentage(value):
    """Format decimal as percentage"""
    return f"{value * 100:.1f}%"

def format_phone(phone):
    """Format phone number"""
    digits = ''.join(c for c in phone if c.isdigit())
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone

# Test code - runs only when executing this file directly
if __name__ == "__main__":
    print("Testing utils module...")

    print(format_currency(1234.56))     # $1,234.56
    print(format_percentage(0.157))     # 15.7%
    print(format_phone("1234567890"))   # (123) 456-7890

    print("\nAll tests passed!")

# File: main.py
from utils import format_currency, format_percentage

price = 99.99
tax_rate = 0.08

total = price * (1 + tax_rate)
print(f"Price: {format_currency(price)}")
print(f"Tax: {format_percentage(tax_rate)}")
print(f"Total: {format_currency(total)}")

# Output:
# Price: $99.99
# Tax: 8.0%
# Total: $107.99
```

### Module Search Path

```python
import sys

# Python looks for modules in these locations (in order):
print("Module search path:")
for path in sys.path:
    print(f"  - {path}")

# 1. Current directory
# 2. PYTHONPATH environment variable
# 3. Installation-dependent default paths
```

### Best Practices

1. **Use clear names**: Module names should describe their purpose
2. **One module, one purpose**: Keep modules focused
3. **Add docstrings**: Document what the module does
4. **Use `__init__.py`**: For packages
5. **Avoid circular imports**: Module A imports B, B imports A
6. **Use `if __name__ == "__main__"`**: For test code

### Common Mistakes

1. **Circular imports**: Two modules importing each other
2. **Name conflicts**: Module name same as standard library
3. **Missing `__init__.py`**: Needed for packages (Python < 3.3)
4. **Wrong import path**: Check module location
5. **Modifying sys.path**: Usually unnecessary

### Organizing Larger Projects

```
project/
├── main.py
├── config.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── validators.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
└── services/
    ├── __init__.py
    ├── auth.py
    └── database.py
```

### Key Takeaways

1. Any `.py` file is a module
2. Use `import module_name` to import
3. Use `from module import item` for specific items
4. Organize related modules into packages
5. Use `__init__.py` to create packages
6. Add `if __name__ == "__main__"` for test code
7. Keep modules focused and well-documented
