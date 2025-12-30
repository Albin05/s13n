## Editorials: Iterating Through Lists Using Loops

### Q1 Solution: Basic List Iteration

```python
numbers = [5, 10, 15, 20, 25, 30, 35, 40]

# 1. Print all numbers
print("All numbers:", end=' ')
for num in numbers:
    print(num, end=' ')
print()

# 2. Print numbers > 20
print("Numbers > 20:", end=' ')
for num in numbers:
    if num > 20:
        print(num, end=' ')
print()

# 3. Calculate sum
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# 4. Count divisible by 10
count = 0
for num in numbers:
    if num % 10 == 0:
        count += 1
print(f"Count divisible by 10: {count}")

# 5. Find maximum
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(f"Maximum: {maximum}")
```

**Explanation:**
- Basic for loop iterates directly over elements
- Conditional `if` filters elements
- Accumulator pattern for sum and count
- Comparison pattern for finding maximum

**Key Concepts:**
- `for item in list:` - most common iteration pattern
- Accumulator variables updated in loop
- Early initialization for finding min/max

---

### Q2 Solution: Using enumerate()

```python
fruits = ['apple', 'banana', 'orange', 'mango', 'grape']

# 1. With index (0-based)
print("With index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
print()

# 2. With position (1-based)
print("With position:")
for pos, fruit in enumerate(fruits, start=1):
    print(f"{pos}. {fruit}")
print()

# 3. Long fruits (>5 letters)
print("Long fruits (>5 letters):")
for index, fruit in enumerate(fruits):
    if len(fruit) > 5:
        print(f"Index {index}: {fruit} ({len(fruit)} letters)")
print()

# 4. Even indices only
print("Fruits at even indices:")
for index, fruit in enumerate(fruits):
    if index % 2 == 0:
        print(f"{index}: {fruit}")
print()

# 5. Create dictionary
fruit_dict = {}
for index, fruit in enumerate(fruits):
    fruit_dict[index] = fruit
print(f"Dictionary: {fruit_dict}")
```

**Explanation:**
- `enumerate(list)` returns (index, value) pairs
- `enumerate(list, start=1)` starts counting from 1
- Can filter by index or value
- Perfect for creating index-based dictionaries

**enumerate() Benefits:**
- Cleaner than manual index tracking
- More Pythonic than `range(len(list))`
- Gets both index and value simultaneously

---

### Q3 Solution: Parallel List Processing with zip()

```python
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable']
prices = [999.99, 29.99, 79.99, 299.99, 9.99]
quantities = [5, 50, 30, 10, 100]

# 1. Print inventory
print("Inventory:")
for product, price, qty in zip(products, prices, quantities):
    total = price * qty
    print(f"{product}: ${price:.2f} × {qty} = ${total:.2f}")
print()

# 2-3. Calculate totals and find highest
product_values = []
for product, price, qty in zip(products, prices, quantities):
    total_value = price * qty
    product_values.append((product, total_value))

highest = max(product_values, key=lambda x: x[1])
print(f"Highest value product: {highest[0]} (${highest[1]:.2f})")

# 4. Total inventory value
inventory_value = 0
for price, qty in zip(prices, quantities):
    inventory_value += price * qty
print(f"Total inventory value: ${inventory_value:.2f}")
print()

# 5. Create list of tuples
product_details = []
for product, price, qty in zip(products, prices, quantities):
    total_value = price * qty
    product_details.append((product, price, qty, total_value))

print("Product details:")
for detail in product_details:
    print(detail)
```

**Explanation:**
- `zip()` combines multiple lists element by element
- Returns tuples that can be unpacked in loop
- Stops at shortest list
- Perfect for parallel data processing

**zip() Pattern:**
- Use when you have related data in separate lists
- Cleaner than indexing multiple lists
- Can zip 2, 3, or more lists together

---

### Q4 Solution: Temperature Analysis

```python
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temps = [72, 68, 75, 80, 78, 82, 79]

# 1. Print daily temperatures
print("Weekly Temperatures:")
for day, temp in zip(days, temps):
    print(f"{day}: {temp}°F")
print()

# 2. Find hottest and coldest
hottest_temp = max(temps)
coldest_temp = min(temps)
hottest_day = days[temps.index(hottest_temp)]
coldest_day = days[temps.index(coldest_temp)]

print("Analysis:")
print(f"Hottest: {hottest_day} ({hottest_temp}°F)")
print(f"Coldest: {coldest_day} ({coldest_temp}°F)")

# 3. Calculate average
average = sum(temps) / len(temps)
print(f"Average: {average:.1f}°F")

# 4. Count above average
above_avg = 0
for temp in temps:
    if temp > average:
        above_avg += 1
print(f"Days above average: {above_avg}")
print()

# 5. Comfort ratings
print("Comfort Ratings:")
for day, temp in zip(days, temps):
    if temp < 70:
        rating = "Cold"
    elif temp <= 78:
        rating = "Comfortable"
    else:
        rating = "Hot"
    print(f"{day}: {temp}°F - {rating}")
```

**Explanation:**
- zip() combines days and temperatures
- Built-in max(), min(), sum() for analysis
- index() method finds position in list
- Conditional logic for categorization

**Data Analysis Pattern:**
- Aggregate functions (max, min, sum, average)
- Counting with conditionals
- Categorization with if-elif-else
- Combining lists for meaningful output

---

### Q5 Solution: Grade Book Manager

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
math_scores = [85, 92, 78, 88, 95]
science_scores = [90, 88, 82, 91, 89]
english_scores = [88, 85, 90, 87, 92]

# Helper function for letter grade
def get_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

# 1-2. Calculate averages and grades
print("Student Averages:")
student_averages = []

for student, math, sci, eng in zip(students, math_scores, science_scores, english_scores):
    avg = (math + sci + eng) / 3
    grade = get_letter_grade(avg)
    student_averages.append((student, avg))
    print(f"{student}: {avg:.1f} ({grade})")
print()

# 3. Find top student
top_student = max(student_averages, key=lambda x: x[1])
print(f"Top student: {top_student[0]} ({top_student[1]:.1f})")
print()

# 4. Subject averages
math_avg = sum(math_scores) / len(math_scores)
sci_avg = sum(science_scores) / len(science_scores)
eng_avg = sum(english_scores) / len(english_scores)

print("Subject Averages:")
print(f"Math: {math_avg:.1f}")
print(f"Science: {sci_avg:.1f}")
print(f"English: {eng_avg:.1f}")

subject_avgs = [('Math', math_avg), ('Science', sci_avg), ('English', eng_avg)]
highest_subject = max(subject_avgs, key=lambda x: x[1])
print(f"Highest class average: {highest_subject[0]} ({highest_subject[1]:.1f})")
print()

# 5. Report cards
print("Report Cards:")
for student, math, sci, eng in zip(students, math_scores, science_scores, english_scores):
    avg = (math + sci + eng) / 3
    grade = get_letter_grade(avg)
    print(f"===== {student} =====")
    print(f"Math: {math}")
    print(f"Science: {sci}")
    print(f"English: {eng}")
    print(f"Average: {avg:.1f}")
    print(f"Grade: {grade}")
    print()
```

**Explanation:**
- zip() combines all parallel lists
- Helper function for letter grade calculation
- List of tuples stores student data
- max() with key parameter finds highest
- Multiple passes over data for different analyses

**Advanced Patterns:**
- Helper functions for repeated logic
- Storing intermediate results in lists
- Using lambda with max() for custom comparison
- Multi-pass processing for different insights

**Key Concepts:**
- zip() is powerful for related parallel data
- enumerate() when you need both index and value
- Break complex problems into smaller iterations
- Combine iteration with data structures (tuples, lists)
- Use built-in functions (max, min, sum) when possible
