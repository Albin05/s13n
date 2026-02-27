# Lecture Notes: Read JSON Files

## Read JSON Files

Loading JSON data from files into Python data structures


---

<div align="center">

![Python JSON File Read json.load() Parse](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.12.jpg)

*JSON data forms a nested tree structure similar to the DOM, with objects containing other objects*

</div>

---

## Introduction

JSON implements **structured data serialization** - converting complex data structures to text and back! Created for **web APIs** (AJAX, 2000s), JSON became the **internet's data format** - replacing XML. JSON is **human-readable structured data**!

### Why JSON Revolutionized the Web

**Before JSON** (XML): Verbose, hard to parse:
```xml
<person>
  <name>Alice</name>
  <age>25</age>
</person>
```

**With JSON**: Concise, JavaScript-native:
```json
{"name": "Alice", "age": 25}
```

**This is data minimalism** - only essential syntax!

### Historical Context

**JSON invented by Douglas Crockford** (2001) for web applications. Derived from **JavaScript object literals**. **RFC 4627 (2006)** formalized the standard.

**Why JSON won**: JavaScript engines parse it natively (using `eval()` originally, `JSON.parse()` later). **XML required complex parsers** - JSON is just JavaScript syntax!

**Python's json module** (Python 2.6, 2008): Maps JSON to Python dicts/lists perfectly. **Perfect impedance match** - JSON objects → dicts, arrays → lists!

### Real-World Analogies

**JSON like structured message format**:
- **Letter (XML)**: Formal, verbose
- **Text message (JSON)**: Concise, gets point across
**Web APIs prefer text messages over letters!**

---
### Key Concepts

JSON (JavaScript Object Notation) is a lightweight data format commonly used for:
- Data storage and configuration files
- API responses and web services
- Data exchange between applications
- Storing structured data

### Core Principles

**Important functions**: `json.load()`, `json.loads()`, parsing JSON to Python dicts/lists

### Syntax and Usage

```python
import json

# Read from file
with open('data.json', 'r') as file:
    data = json.load(file)  # Converts JSON to Python dict/list

# Read from string
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)  # Converts JSON string to Python dict
```

### Practical Examples

#### Example 1: Reading Simple JSON File

```python
import json

# Create a sample JSON file
sample_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming", "hiking"]
}

# Write to file (for demonstration)
with open('user.json', 'w') as file:
    json.dump(sample_data, file)

# Read JSON file
with open('user.json', 'r') as file:
    user_data = json.load(file)

print("User Information:")
print(f"Name: {user_data['name']}")
print(f"Age: {user_data['age']}")
print(f"City: {user_data['city']}")
print(f"Hobbies: {', '.join(user_data['hobbies'])}")

# Output:
# User Information:
# Name: Alice
# Age: 30
# City: New York
# Hobbies: reading, gaming, hiking
```

#### Example 2: Reading Configuration File

```python
import json

# Sample config.json file:
# {
#     "database": {
#         "host": "localhost",
#         "port": 5432,
#         "username": "admin",
#         "database_name": "myapp"
#     },
#     "app_settings": {
#         "debug_mode": true,
#         "max_connections": 100,
#         "timeout": 30
#     }
# }

def load_config(filename):
    """Load configuration from JSON file"""
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Config file '{filename}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in config file: {e}")
        return None

# Load and use configuration
config = load_config('config.json')

if config:
    # Access database settings
    db_config = config['database']
    print(f"Connecting to {db_config['host']}:{db_config['port']}")
    print(f"Database: {db_config['database_name']}")

    # Access app settings
    app_config = config['app_settings']
    print(f"Debug mode: {app_config['debug_mode']}")
    print(f"Max connections: {app_config['max_connections']}")

# Output:
# Connecting to localhost:5432
# Database: myapp
# Debug mode: True
# Max connections: 100
```

#### Example 3: Reading Array of Objects

```python
import json

# Sample students.json file:
# [
#     {"id": 1, "name": "Alice", "grade": 85, "courses": ["Math", "Science"]},
#     {"id": 2, "name": "Bob", "grade": 92, "courses": ["English", "History"]},
#     {"id": 3, "name": "Charlie", "grade": 78, "courses": ["Math", "Art"]}
# ]

def load_students(filename):
    """Load student data from JSON file"""
    with open(filename, 'r') as file:
        students = json.load(file)
    return students

# Load students
students = load_students('students.json')

# Process student data
print(f"Total students: {len(students)}\n")

for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Grade: {student['grade']}")
    print(f"Courses: {', '.join(student['courses'])}")
    print()

# Calculate average grade
average_grade = sum(s['grade'] for s in students) / len(students)
print(f"Average grade: {average_grade:.2f}")

# Find top student
top_student = max(students, key=lambda s: s['grade'])
print(f"Top student: {top_student['name']} with grade {top_student['grade']}")

# Output:
# Total students: 3
#
# ID: 1
# Name: Alice
# Grade: 85
# Courses: Math, Science
#
# ID: 2
# Name: Bob
# Grade: 92
# Courses: English, History
#
# ID: 3
# Name: Charlie
# Grade: 78
# Courses: Math, Art
#
# Average grade: 85.00
# Top student: Bob with grade 92
```

#### Example 4: Reading Nested JSON Structure

```python
import json

# Sample company.json file:
# {
#     "company_name": "Tech Corp",
#     "employees": [
#         {
#             "name": "Alice",
#             "position": "Developer",
#             "salary": 75000,
#             "projects": [
#                 {"name": "Project A", "hours": 120},
#                 {"name": "Project B", "hours": 80}
#             ]
#         },
#         {
#             "name": "Bob",
#             "position": "Manager",
#             "salary": 90000,
#             "projects": [
#                 {"name": "Project C", "hours": 100}
#             ]
#         }
#     ],
#     "location": "New York"
# }

def analyze_company_data(filename):
    """Analyze company data from JSON file"""
    with open(filename, 'r') as file:
        company = json.load(file)

    print(f"Company: {company['company_name']}")
    print(f"Location: {company['location']}")
    print(f"Total employees: {len(company['employees'])}\n")

    total_salary = 0
    total_hours = 0

    for employee in company['employees']:
        print(f"Employee: {employee['name']}")
        print(f"Position: {employee['position']}")
        print(f"Salary: ${employee['salary']:,}")

        total_salary += employee['salary']

        # Calculate total project hours
        emp_hours = sum(p['hours'] for p in employee['projects'])
        total_hours += emp_hours

        print(f"Projects: {len(employee['projects'])}")
        print(f"Total hours: {emp_hours}")

        for project in employee['projects']:
            print(f"  - {project['name']}: {project['hours']} hours")
        print()

    print(f"Average salary: ${total_salary / len(company['employees']):,.2f}")
    print(f"Total project hours: {total_hours}")

analyze_company_data('company.json')

# Output:
# Company: Tech Corp
# Location: New York
# Total employees: 2
#
# Employee: Alice
# Position: Developer
# Salary: $75,000
# Projects: 2
# Total hours: 200
#   - Project A: 120 hours
#   - Project B: 80 hours
#
# Employee: Bob
# Position: Manager
# Salary: $90,000
# Projects: 1
# Total hours: 100
#   - Project C: 100 hours
#
# Average salary: $82,500.00
# Total project hours: 300
```

#### Example 5: Reading JSON with Error Handling

```python
import json
import os

class JSONReader:
    """Class to handle JSON file reading with comprehensive error handling"""

    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def read(self):
        """Read JSON file with error handling"""
        # Check if file exists
        if not os.path.exists(self.filename):
            print(f"Error: File '{self.filename}' not found")
            return False

        # Check if file is empty
        if os.path.getsize(self.filename) == 0:
            print(f"Error: File '{self.filename}' is empty")
            return False

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            print(f"Successfully loaded {self.filename}")
            return True

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in '{self.filename}'")
            print(f"Line {e.lineno}, Column {e.colno}: {e.msg}")
            return False

        except PermissionError:
            print(f"Error: No permission to read '{self.filename}'")
            return False

        except Exception as e:
            print(f"Unexpected error reading '{self.filename}': {e}")
            return False

    def get_value(self, key, default=None):
        """Get value by key with default fallback"""
        if self.data is None:
            return default
        return self.data.get(key, default)

    def get_nested_value(self, *keys, default=None):
        """Get nested value using multiple keys"""
        if self.data is None:
            return default

        value = self.data
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value

# Usage example
reader = JSONReader('settings.json')

if reader.read():
    # Access data safely
    username = reader.get_value('username', 'unknown')
    theme = reader.get_nested_value('preferences', 'theme', default='light')

    print(f"Username: {username}")
    print(f"Theme: {theme}")

    # Access full data
    print(f"\nFull data: {reader.data}")
```

### Best Practices

1. **Always use context managers**: Use `with open()` to ensure files are properly closed
2. **Handle errors gracefully**: Catch `JSONDecodeError` for invalid JSON
3. **Validate data structure**: Check if keys exist before accessing
4. **Use encoding parameter**: Specify `encoding='utf-8'` for consistency
5. **Check file existence**: Verify file exists before attempting to read

### Common Mistakes

1. **Forgetting to close files**: Always use `with` statement
   ```python
   # Bad
   file = open('data.json')
   data = json.load(file)
   # file.close() might be forgotten

   # Good
   with open('data.json') as file:
       data = json.load(file)
   ```

2. **Not handling missing keys**: Always check or use `.get()` method
   ```python
   # Bad - will raise KeyError if missing
   name = data['name']

   # Good - returns None if missing
   name = data.get('name')

   # Good - with default value
   name = data.get('name', 'Unknown')
   ```

3. **Confusing load() and loads()**:
   - `json.load()` - reads from file object
   - `json.loads()` - reads from string

4. **Not checking for empty files**: Empty files cause JSON errors

### Real-World Applications

Common use cases for reading JSON files:
- **Configuration files**: App settings, database credentials
- **Data storage**: Storing user preferences, cache data
- **API responses**: Saving and processing API data locally
- **Data analysis**: Loading datasets for processing
- **Testing**: Using JSON fixtures for test data

### Key Takeaways

1. Use `json.load(file)` to read JSON from files
2. Use `json.loads(string)` to parse JSON strings
3. JSON converts to Python: objects→dicts, arrays→lists, true/false→True/False
4. Always handle `JSONDecodeError` for invalid JSON
5. Use context managers (`with` statement) for file handling
6. Validate data structure before accessing nested values
7. Specify encoding for better compatibility
