# Lecture Notes: Import Built-in Modules

## Import Built-in Modules

Using Python's standard library modules in your programs


---

<div align="center">

![Python import Built-in Modules math sys os](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.14.png)

*Built-in modules provide pre-written functions that you can import and call in your program flow*

</div>

---

## Introduction

The import system implements **modular programming** - organizing code into reusable components! Python's **standard library** (200+ modules) is the **"batteries included"** philosophy - everything you need ships with Python. Modules solve the **code organization problem**!

### Why Modules Matter

**Before modules** (single file): Code becomes unmaintainable:
```python
# All 10,000 lines in one file!
def math_sqrt(x): ...
def file_read(path): ...
def json_parse(data): ...
# Impossible to navigate!
```

**With modules** (organized): Code split logically:
```python
import math  # Math functions
import os    # File operations
import json  # JSON parsing
# Clean, organized!
```

**This is separation of concerns** - each module handles one domain!

### Historical Context

**Modules from FORTRAN** (1957) which had SUBROUTINE libraries. **Python's import** (1991) based on **Modula-3** (1980s) module system.

**"Batteries included"** philosophy: **Guido van Rossum** (Python creator) wanted stdlib to handle common tasks without external dependencies. Contrast with **JavaScript** (minimal stdlib) or **Go** (comprehensive stdlib like Python).

**The import statement** uses **sys.path** to find modules - pioneered by **Unix dynamic linker** (1970s). Python's import is essentially dynamic code loading!

### Real-World Analogies

**Modules like tool chest**:
- **Toolbox**: Module (collection of related tools)
- **Tools**: Functions/classes (specific functionality)
- **Import**: Open toolbox, grab tools needed
**Don't carry all tools - import what you need!**

---
### Key Concepts

Python comes with a rich standard library of built-in modules for:
- File and directory operations
- Date and time handling
- Math operations
- Random number generation
- System interactions

### Core Principles

**Common built-in modules**: `os`, `sys`, `math`, `random`, `datetime`, `json`, `re`, `pathlib`

### Syntax and Usage

```python
# Different ways to import
import math                      # Import entire module
from math import sqrt, pi        # Import specific items
from datetime import datetime    # Import specific class
import random as rnd             # Import with alias
```

### Practical Examples

#### Example 1: Math Module

```python
import math

# Basic math operations
print(f"Pi: {math.pi}")                    # 3.141592653589793
print(f"E: {math.e}")                      # 2.718281828459045

# Square root and power
number = 16
print(f"Square root of {number}: {math.sqrt(number)}")  # 4.0
print(f"2^8 = {math.pow(2, 8)}")                        # 256.0

# Trigonometric functions
angle = 45
radians = math.radians(angle)
print(f"sin(45°) = {math.sin(radians):.4f}")  # 0.7071
print(f"cos(45°) = {math.cos(radians):.4f}")  # 0.7071

# Rounding functions
value = 4.7
print(f"floor({value}) = {math.floor(value)}")  # 4
print(f"ceil({value}) = {math.ceil(value)}")    # 5

# Logarithms
print(f"log(100, base 10) = {math.log10(100)}")  # 2.0
print(f"natural log(e) = {math.log(math.e)}")    # 1.0
```

#### Example 2: Random Module

```python
import random

# Random integers
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Random float between 0 and 1
probability = random.random()
print(f"Random probability: {probability:.4f}")

# Random choice from list
colors = ["red", "green", "blue", "yellow"]
chosen_color = random.choice(colors)
print(f"Random color: {chosen_color}")

# Shuffle a list
deck = list(range(1, 11))
random.shuffle(deck)
print(f"Shuffled deck: {deck}")

# Random sample (without replacement)
lottery_numbers = random.sample(range(1, 50), 6)
print(f"Lottery numbers: {sorted(lottery_numbers)}")

# Seed for reproducible results
random.seed(42)
print(f"First random: {random.random()}")
random.seed(42)
print(f"Same random: {random.random()}")  # Same as above
```

#### Example 3: Datetime Module

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Create specific date
birthday = date(1990, 5, 15)
print(f"Birthday: {birthday}")

# Calculate age
today = date.today()
age = today.year - birthday.year
print(f"Age: {age} years")

# Time arithmetic
one_week = timedelta(days=7)
next_week = today + one_week
print(f"Next week: {next_week}")

# Time difference
event_date = date(2024, 12, 25)
days_until = (event_date - today).days
print(f"Days until event: {days_until}")

# Parse date string
date_string = "2024-03-15"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date.date()}")

# Different formats
print(f"Full: {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
print(f"Short: {now.strftime('%m/%d/%y')}")
```

#### Example 4: OS Module

```python
import os

# Current working directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# List files in directory
files = os.listdir('.')
print(f"Files in current directory: {len(files)}")

# Check if path exists
if os.path.exists('data.txt'):
    print("File exists!")
else:
    print("File does not exist")

# Get file info
filename = 'example.txt'
if os.path.exists(filename):
    size = os.path.getsize(filename)
    print(f"File size: {size} bytes")

# Join paths (works on all OS)
data_path = os.path.join('data', 'files', 'example.txt')
print(f"Path: {data_path}")

# Get file extension
name, ext = os.path.splitext('document.pdf')
print(f"Name: {name}, Extension: {ext}")

# Environment variables
home = os.getenv('HOME', 'default_home')
print(f"Home directory: {home}")

# Create directory
new_dir = 'temp_folder'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    print(f"Created directory: {new_dir}")
```

#### Example 5: Multiple Modules Together

```python
import os
import sys
from datetime import datetime
import random

class FileLogger:
    """Simple file logger using built-in modules"""

    def __init__(self, log_file='app.log'):
        self.log_file = log_file

        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def log(self, message, level='INFO'):
        """Log a message with timestamp"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(self.log_file, 'a') as f:
            f.write(log_entry)

        print(log_entry.strip())

    def get_stats(self):
        """Get log file statistics"""
        if not os.path.exists(self.log_file):
            return "Log file doesn't exist"

        size = os.path.getsize(self.log_file)
        with open(self.log_file, 'r') as f:
            lines = len(f.readlines())

        return f"Log file: {size} bytes, {lines} entries"

# Usage
logger = FileLogger('logs/application.log')

logger.log("Application started", "INFO")
logger.log("Processing data", "INFO")
logger.log("Warning: Low memory", "WARNING")
logger.log("Error occurred", "ERROR")

print(logger.get_stats())

# Use sys module
print(f"\nPython version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Arguments: {sys.argv}")
```

### Commonly Used Built-in Modules

**File & System**:
- `os` - Operating system interface
- `sys` - System-specific parameters
- `pathlib` - Object-oriented filesystem paths
- `shutil` - High-level file operations

**Data Processing**:
- `json` - JSON encoding/decoding
- `csv` - CSV file reading/writing
- `re` - Regular expressions
- `collections` - Specialized container datatypes

**Date & Time**:
- `datetime` - Date and time handling
- `time` - Time access and conversions

**Math & Random**:
- `math` - Mathematical functions
- `random` - Random number generation
- `statistics` - Statistical functions

**Internet & Networking**:
- `urllib` - URL handling
- `http` - HTTP protocols

### Best Practices

1. **Import only what you need**: `from math import sqrt` vs `import math`
2. **Use meaningful aliases**: `import numpy as np` (common convention)
3. **Import at top of file**: Keep all imports together
4. **Avoid wildcard imports**: Don't use `from module import *`
5. **Check module documentation**: Use `help(module)` for info

### Common Mistakes

1. **Name conflicts**: Don't name your file `random.py` if importing `random`
2. **Circular imports**: Module A imports B, B imports A
3. **Importing inside functions**: Usually import at module level
4. **Not checking if module exists**: Use try/except for optional modules

### Key Takeaways

1. Python has rich standard library of built-in modules
2. Use `import module` or `from module import item`
3. Common modules: `os`, `sys`, `math`, `random`, `datetime`, `json`
4. No installation needed - they come with Python
5. Import at top of file for clarity
6. Use `help()` and official docs to learn modules
