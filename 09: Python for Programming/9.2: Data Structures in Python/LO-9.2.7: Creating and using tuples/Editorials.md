## Editorials: Creating and Using Tuples

### Q1 Solution: Basic Tuple Creation and Access

```python
# 1. Create tuple
numbers = (10, 20, 30, 40, 50)
print(f"Tuple: {numbers}")

# 2. First and last
first = numbers[0]
last = numbers[-1]
print(f"First: {first}")
print(f"Last: {last}")

# 3. Slice [1:3]
slice_result = numbers[1:3]
print(f"Slice [1:3]: {slice_result}")

# 4. Single element tuple
single = (100,)  # Note the comma!
print(f"Single element: {single}")

# 5. Convert list to tuple
from_list = tuple([1, 2, 3])
print(f"From list: {from_list}")
```

**Explanation:**
- Tuples created with parentheses: `(1, 2, 3)`
- Indexing same as lists: `[0]`, `[-1]`
- Slicing same as lists: `[1:3]`
- Single element needs comma: `(100,)` not `(100)`
- `tuple()` constructor converts iterables

**Key Point:** The comma makes the tuple, not the parentheses!

---

### Q2 Solution: Tuple Methods and Operations

```python
numbers = (5, 10, 15, 10, 20, 10, 25)

# 1. Count 10s
count_10 = numbers.count(10)
print(f"Count of 10: {count_10}")

# 2. Index of 15
index_15 = numbers.index(15)
print(f"Index of 15: {index_15}")

# 3. Second occurrence of 10
# First at index 1, so start search from index 2
second_10 = numbers.index(10, 2)
print(f"Second occurrence of 10 at index: {second_10}")

# 4. Membership test
has_20 = 20 in numbers
print(f"20 in tuple: {has_20}")

# 5. Sum and length
total = sum(numbers)
length = len(numbers)
print(f"Sum: {total}")
print(f"Length: {length}")
```

**Explanation:**
- `count(value)` - returns number of occurrences
- `index(value)` - returns first occurrence index
- `index(value, start)` - search from start position
- `in` operator for membership testing
- Built-in functions: `sum()`, `len()`

**Only 2 Methods:** Tuples have only `count()` and `index()` - no append, remove, etc.

---

### Q3 Solution: Coordinate System

```python
import math

# 1. Define points
origin = (0, 0)
point_a = (3, 4)
point_b = (-2, 5)

print(f"Origin: {origin}")
print(f"Point A: {point_a}")
print(f"Point B: {point_b}")
print()

# 2. Distance from origin
def distance_from_origin(point):
    x, y = point  # Unpack tuple
    return math.sqrt(x**2 + y**2)

print("Distance from origin:")
dist_a = distance_from_origin(point_a)
dist_b = distance_from_origin(point_b)
print(f"  Point A: {dist_a:.2f}")
print(f"  Point B: {dist_b:.2f}")
print()

# 3. Translate point
def translate_point(point, dx, dy):
    x, y = point
    return (x + dx, y + dy)  # Return new tuple

translated = translate_point(point_a, 2, -1)
print(f"Translate Point A by (2, -1): {translated}")
print()

# 4. Random points
points = [(1, 2), (4, 1), (-3, 2), (2, -4), (5, 5)]
print(f"Random points: {points}")

# 5. Farthest point
farthest = max(points, key=distance_from_origin)
farthest_dist = distance_from_origin(farthest)
print(f"Farthest point: {farthest} at distance {farthest_dist:.2f}")
```

**Explanation:**
- Tuples perfect for immutable coordinates
- Unpack with `x, y = point`
- Return new tuple from function
- `max()` with key function finds farthest
- Math operations don't modify tuple

**Pattern:** Functions return new tuples rather than modifying

---

### Q4 Solution: RGB Color Manager

```python
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255)
}

# 1. Brightness function
def brightness(rgb):
    r, g, b = rgb
    return (r + g + b) / 3

# Calculate all brightness
print("Color brightness:")
for name, rgb in colors.items():
    b = brightness(rgb)
    print(f"  {name}: {b:.1f}")
print()

# 2. Invert color
def invert_color(rgb):
    r, g, b = rgb
    return (255 - r, 255 - g, 255 - b)

# 3. Brightest and darkest
brightest_name = max(colors, key=lambda name: brightness(colors[name]))
darkest_name = min(colors, key=lambda name: brightness(colors[name]))

print(f"Brightest: {brightest_name} ({brightness(colors[brightest_name]):.1f})")
print(f"Darkest: {darkest_name} ({brightness(colors[darkest_name]):.1f})")
print()

# 4. Bright colors
bright_colors = [name for name, rgb in colors.items() if brightness(rgb) > 150]
print(f"Bright colors (>150): {bright_colors}")
print()

# 5. Invert primaries
primaries = ['red', 'green', 'blue']
print("Inverted colors:")
for name in primaries:
    original = colors[name]
    inverted = invert_color(original)
    print(f"  {name} {original} → {inverted}")
```

**Explanation:**
- Tuples as dict values for RGB
- Unpack in function: `r, g, b = rgb`
- Return new tuple from function
- Tuples are hashable - can be dict keys
- List comprehension filters colors

**Why Tuples:** RGB values shouldn't change, perfect for tuples

---

### Q5 Solution: Student Records System

```python
students = [
    (101, 'Alice', 20, 'A', 3.8),
    (102, 'Bob', 21, 'B', 3.2),
    (103, 'Charlie', 19, 'A', 3.9),
    (104, 'Diana', 20, 'C', 2.8),
    (105, 'Eve', 22, 'B', 3.5)
]

# 1. Find by ID
def find_by_id(students, student_id):
    for student in students:
        if student[0] == student_id:
            return student
    return None

student_103 = find_by_id(students, 103)
print(f"Student 103: {student_103}")
print()

# 2. Honors students
def get_honors_students(students):
    return [s for s in students if s[4] >= 3.5]

honors = get_honors_students(students)
print("Honors students (GPA ≥ 3.5):")
for student in honors:
    id, name, age, grade, gpa = student  # Unpack
    print(f"  {name}: {gpa}")
print()

# 3. Average GPA
total_gpa = sum(s[4] for s in students)
avg_gpa = total_gpa / len(students)
print(f"Average GPA: {avg_gpa:.2f}")
print()

# 4. ID to name mapping
id_to_name = {s[0]: s[1] for s in students}
print("ID to Name mapping:")
print(f"  {id_to_name}")
print()

# 5. Youngest and oldest
youngest = min(students, key=lambda s: s[2])
oldest = max(students, key=lambda s: s[2])

print(f"Youngest: {youngest[1]} ({youngest[2]} years)")
print(f"Oldest: {oldest[1]} ({oldest[2]} years)")
```

**Explanation:**
- Each record is immutable tuple
- Access by index: `student[0]` for ID, `student[4]` for GPA
- Unpack for readability: `id, name, age, grade, gpa = student`
- Filter with list comprehension
- `min()`/`max()` with key parameter

**Why Tuples:**
- Student records shouldn't be modified
- Fixed structure: always 5 elements
- Can be sorted, compared
- More memory efficient than dicts

**Key Concepts:**
- Tuples for immutable records
- Index access or unpacking
- Functions work with tuples naturally
- Great for fixed-structure data
