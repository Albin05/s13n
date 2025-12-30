## Editorials: Tuple Packing and Unpacking

---

### Q1 Solution: Basic Tuple Unpacking

```python
# 1. Create student tuple
student = ('Alice', 20, 'Computer Science', 3.8)

# 2. Unpack into variables
name, age, major, gpa = student

# 3. Print formatted information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"GPA: {gpa}")

# 4. Swap age and gpa using tuple unpacking
age, gpa = gpa, age

# 5. Print swapped values
print(f"\nAfter swap:")
print(f"Age: {age}")
print(f"GPA: {gpa}")
```

**Explanation:**

**Step 1: Basic Unpacking**
```python
name, age, major, gpa = student
```
- The tuple has 4 elements
- We provide 4 variables on the left
- Each element is assigned in order

**Step 2: Variable Swapping**
```python
age, gpa = gpa, age
```
- Right side evaluated first: `(gpa, age)` → `(3.8, 20)`
- This tuple is then unpacked: `age = 3.8, gpa = 20`
- No temporary variable needed!

**Key Concepts:**
- Number of variables must match number of elements
- Swapping is elegant with tuple unpacking
- Right side always evaluated before assignment

---

### Q2 Solution: Extended Unpacking with * Operator

```python
# 1. Create scores tuple
scores = (95, 88, 92, 78, 85, 90, 87)

# 2. Extended unpacking
first, *middle, last = scores

# 3. Print results
print(f"First score: {first}")
print(f"Last score: {last}")
print(f"Middle scores: {middle}")
print(f"Number of middle scores: {len(middle)}")

# Calculate average of middle scores
middle_average = sum(middle) / len(middle)
print(f"Average of middle scores: {middle_average:.1f}")
```

**Explanation:**

**Extended Unpacking Pattern:**
```python
first, *middle, last = scores
```
- `first` gets the first element: `95`
- `last` gets the last element: `87`
- `*middle` collects everything in between: `[88, 92, 78, 85, 90]`

**Important Notes:**
1. The `*` creates a **list**, not a tuple
2. If there's nothing in the middle, `middle` would be `[]`
3. Only one `*` allowed per unpacking

**Alternative Patterns:**
```python
# Get first and rest
first, *rest = scores

# Get all but last
*beginning, last = scores

# Get first, second, and rest
first, second, *rest = scores
```

---

### Q3 Solution: Data Transformation System

```python
# 1. Create points list
points = [(0, 0), (3, 4), (6, 8), (1, 2)]

# 2. Translation function
def translate_point(point, dx, dy):
    x, y = point  # Unpack coordinates
    return x + dx, y + dy  # Pack and return

# 3. Scale function
def scale_point(point, factor):
    x, y = point  # Unpack
    return x * factor, y * factor  # Pack and return

# 4. Reflect function
def reflect_point(point):
    x, y = point  # Unpack
    return -x, y  # Pack and return (negate x)

# 5. Process each point
for original in points:
    # Chain transformations
    translated = translate_point(original, 5, 5)
    scaled = scale_point(translated, 2)
    final = reflect_point(scaled)
    
    # Unpack for printing
    ox, oy = original
    tx, ty = translated
    sx, sy = scaled
    fx, fy = final
    
    print(f"Original: ({ox}, {oy}) → Translated: ({tx}, {ty}) → Scaled: ({sx}, {sy}) → Reflected: ({fx}, {fy})")
```

**Explanation:**

**Function Pattern:**
```python
def translate_point(point, dx, dy):
    x, y = point      # Unpack input
    return x + dx, y + dy  # Pack output
```

**Key Points:**
1. **Unpack at start:** Extract coordinates from tuple
2. **Process:** Perform calculations
3. **Pack at return:** Return new tuple automatically

**Transformation Chain:**
```python
(0, 0) → translate(5,5) → (5, 5)
(5, 5) → scale(2) → (10, 10)
(10, 10) → reflect → (-10, 10)
```

**Loop Unpacking:**
```python
for original in points:  # Each 'original' is a tuple
    # Can also unpack directly:
    # for x, y in points:
```

---

### Q4 Solution: Student Grade Analyzer

```python
# 1. Student records
students = [
    ('Alice', 85, 90, 88, 92),
    ('Bob', 78, 82, 75, 80),
    ('Charlie', 92, 95, 93, 90),
    ('Diana', 88, 85, 90, 87)
]

# 2. Analyze function
def analyze_student(student):
    # Unpack name and all scores using extended unpacking
    name, *test_scores = student
    
    # Calculate statistics
    average = sum(test_scores) / len(test_scores)
    highest = max(test_scores)
    lowest = min(test_scores)
    passed = average >= 85
    
    # Pack and return results
    return name, average, highest, lowest, passed

# 3. Process all students
passed_students = []
all_averages = []

for student in students:
    # Unpack analysis results
    name, avg, high, low, passed = analyze_student(student)
    
    # Store data
    all_averages.append(avg)
    if passed:
        passed_students.append(name)
    
    # Print analysis
    status = "PASS" if passed else "FAIL"
    print(f"{name}: Avg={avg:.2f}, High={high}, Low={low}, Status={status}")

# Print summary
print(f"\nStudents who passed: {', '.join(passed_students)}")

class_average = sum(all_averages) / len(all_averages)
print(f"Class average: {class_average:.2f}")
```

**Explanation:**

**Extended Unpacking for Variable-Length Data:**
```python
name, *test_scores = student
```
- `name` gets first element: `'Alice'`
- `*test_scores` collects rest: `[85, 90, 88, 92]`
- Works regardless of how many test scores there are!

**Packing Return Values:**
```python
return name, average, highest, lowest, passed
```
- Returns a tuple of 5 elements
- Automatically packed by comma separation

**Unpacking Return Values:**
```python
name, avg, high, low, passed = analyze_student(student)
```
- Function returns a tuple
- Immediately unpack into separate variables

**Processing Flow:**
1. Loop through students
2. Each student is a tuple
3. Pass to function
4. Function unpacks, processes, packs results
5. Caller unpacks results
6. Process and aggregate data

---

### Q5 Solution: CSV Data Processor

```python
# 1. CSV data
csv_data = [
    "101,Alice,Engineering,95000,5",
    "102,Bob,Marketing,75000,3",
    "103,Charlie,Engineering,105000,7",
    "104,Diana,HR,65000,2",
    "105,Eve,Engineering,98000,4"
]

# 2. Parse employee function
def parse_employee(csv_string):
    # Split and unpack
    emp_id, name, department, salary, years = csv_string.split(',')
    
    # Convert types and pack
    return int(emp_id), name, department, int(salary), int(years)

# 3. Calculate bonus function
def calculate_bonus(employee):
    # Unpack employee data
    emp_id, name, department, salary, years = employee
    
    # Calculate bonus
    base_rate = 0.05  # 5%
    years_rate = 0.01 * years  # 1% per year
    
    # Engineers get extra 2%
    engineering_bonus = 0.02 if department == 'Engineering' else 0
    
    total_rate = base_rate + years_rate + engineering_bonus
    bonus = salary * total_rate
    
    # Pack and return
    return name, bonus

# 4. Process all employees
employees = []
department_bonuses = {}

for csv_string in csv_data:
    # Parse employee
    employee = parse_employee(csv_string)
    employees.append(employee)
    
    # Unpack for processing
    emp_id, name, department, salary, years = employee
    
    # Calculate bonus
    bonus_name, bonus = calculate_bonus(employee)
    
    # Print employee bonus
    print(f"{name} ({department}, {years} years): Bonus = ${bonus:.2f}")
    
    # Track by department
    if department not in department_bonuses:
        department_bonuses[department] = 0
    department_bonuses[department] += bonus

# Calculate total bonus
total_bonus = sum(department_bonuses.values())
print(f"\nTotal bonus budget: ${total_bonus:.2f}")

# Find department with highest bonuses
max_dept = max(department_bonuses.items(), key=lambda item: item[1])
dept_name, dept_bonus = max_dept  # Unpack the result
print(f"Department with highest bonuses: {dept_name} (${dept_bonus:.2f})")
```

**Explanation:**

**Parsing with Unpacking:**
```python
emp_id, name, department, salary, years = csv_string.split(',')
```
- `split(',')` returns a list of 5 strings
- Unpack directly into variables
- Then convert types as needed

**Type Conversion Pattern:**
```python
return int(emp_id), name, department, int(salary), int(years)
```
- Convert and pack in one step
- Returns properly typed tuple

**Multiple Unpacking Stages:**
```python
# Stage 1: Parse CSV
employee = parse_employee(csv_string)

# Stage 2: Unpack for processing
emp_id, name, department, salary, years = employee

# Stage 3: Calculate bonus
bonus_name, bonus = calculate_bonus(employee)
```

**Dictionary Items Unpacking:**
```python
max_dept = max(department_bonuses.items(), key=lambda item: item[1])
dept_name, dept_bonus = max_dept
```
- `items()` returns (key, value) tuples
- `max()` returns one tuple
- Unpack to get department name and bonus

**Bonus Challenge Solution:**
```python
def parse_employee_flexible(csv_string):
    """Handle variable number of fields"""
    parts = csv_string.split(',')
    
    # Use extended unpacking
    emp_id, name, *optional_fields = parts
    
    # Provide defaults
    department = optional_fields[0] if len(optional_fields) > 0 else 'Unknown'
    salary = int(optional_fields[1]) if len(optional_fields) > 1 else 0
    years = int(optional_fields[2]) if len(optional_fields) > 2 else 0
    
    return int(emp_id), name, department, salary, years

# Test with variable-length data
test_data = [
    "101,Alice,Engineering,95000,5",
    "102,Bob,Marketing,75000",
    "103,Charlie"
]

for csv in test_data:
    emp = parse_employee_flexible(csv)
    print(emp)
```

**Key Patterns:**
1. **String parsing** → unpack immediately
2. **Type conversion** during packing
3. **Function chaining** with pack/unpack
4. **Aggregation** using unpacked data
5. **Dictionary iteration** with key-value unpacking

---

### Key Takeaways

**Unpacking Patterns:**

1. **Basic:** `a, b, c = tuple`
2. **Extended:** `first, *rest = tuple`
3. **Selective:** `first, *_, last = tuple`
4. **Nested:** `a, (b, c) = (1, (2, 3))`

**Common Use Cases:**

1. **Function Returns:**
```python
def get_stats():
    return min_val, max_val, avg
    
minimum, maximum, average = get_stats()
```

2. **Loop Iteration:**
```python
for name, score in student_scores:
    print(f"{name}: {score}")
```

3. **Swapping:**
```python
a, b = b, a
```

4. **Parsing:**
```python
name, age, city = csv_row.split(',')
```

**Best Practices:**

1. Use extended unpacking for flexible data
2. Use `_` for ignored values
3. Unpack at function boundaries for clarity
4. Pack multiple return values instead of dictionaries (when appropriate)
5. Leverage unpacking in loops for cleaner code
