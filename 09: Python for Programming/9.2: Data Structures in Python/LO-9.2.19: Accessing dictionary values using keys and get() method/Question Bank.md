## Question Bank: Accessing Dictionary Values

---

### Q1: Basic Access (3 minutes, Low Difficulty)

Given:
```python
movie = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010,
    'rating': 8.8,
    'genres': ['Sci-Fi', 'Thriller']
}
```

Print:
1. The title using `[]`
2. The director using `.get()`
3. The first genre from the genres list
4. The `'budget'` key using `.get()` with a default of `'Unknown'`
5. Check if `'rating'` exists in the dict

**Expected Output:**
```
Title: Inception
Director: Christopher Nolan
First genre: Sci-Fi
Budget: Unknown
Has rating: True
```

**Key Concepts:** `[]` vs `.get()`, nested access, `in` operator

---

### Q2: Safe Config Reader (3 minutes, Low Difficulty)

Given a partial configuration:
```python
config = {'host': '192.168.1.1', 'port': 8080}
```

Write code that reads these settings with defaults:
- `host` (default: `'localhost'`)
- `port` (default: `3000`)
- `protocol` (default: `'http'`)
- `timeout` (default: `30`)
- `debug` (default: `False`)

Print the complete configuration.

**Expected Output:**
```
host: 192.168.1.1
port: 8080
protocol: http
timeout: 30
debug: False
```

**Key Concepts:** `.get()` with default values

---

### Q3: Nested Data Extraction (5 minutes, Medium Difficulty)

Given:
```python
api_response = {
    'status': 'success',
    'data': {
        'user': {
            'id': 42,
            'name': 'Alice',
            'profile': {
                'avatar': 'alice.png',
                'bio': 'Python developer'
            }
        },
        'posts': [
            {'id': 1, 'title': 'Hello World'},
            {'id': 2, 'title': 'Learning Python'}
        ]
    }
}
```

Safely extract and print:
1. The user's name
2. The user's bio
3. The user's phone (doesn't exist — default to `'N/A'`)
4. The title of the second post
5. The total number of posts

**Expected Output:**
```
Name: Alice
Bio: Python developer
Phone: N/A
Second post: Learning Python
Total posts: 2
```

**Key Concepts:** Nested access, safe chaining with `.get()`

---

### Q4: Student Lookup System (5 minutes, Medium Difficulty)

```python
students = {
    'S001': {'name': 'Alice', 'grade': 'A', 'courses': ['Math', 'Physics']},
    'S002': {'name': 'Bob', 'grade': 'B', 'courses': ['Chemistry', 'Biology']},
    'S003': {'name': 'Charlie', 'grade': 'A', 'courses': ['Math', 'English']}
}
```

Write a function `lookup(student_id)` that:
1. Returns student info if ID exists
2. Returns `"Student not found"` if ID doesn't exist
3. Prints name, grade, and number of courses

Test with: `'S001'`, `'S004'`, `'S003'`

Then write `get_students_by_grade(grade)` that returns names of all students with that grade.

**Expected Output:**
```
S001: Alice, Grade A, 2 courses
S004: Student not found
S003: Charlie, Grade A, 2 courses
Students with grade A: ['Alice', 'Charlie']
```

**Key Concepts:** `.get()` for missing keys, iterating dict values

---

### Q5: Data Transformer (5 minutes, Medium Difficulty)

Given raw data with inconsistent keys:
```python
records = [
    {'name': 'Alice', 'age': 25, 'city': 'Mumbai'},
    {'name': 'Bob', 'city': 'Delhi'},
    {'name': 'Charlie', 'age': 30},
    {'name': 'Diana', 'age': 28, 'city': 'Bangalore', 'phone': '9876543210'},
]
```

Write a function `normalize(records)` that:
1. Ensures every record has keys: `name`, `age`, `city`, `phone`
2. Uses defaults: `age=0`, `city='Unknown'`, `phone='N/A'`
3. Returns the normalized list

Print all normalized records.

**Expected Output:**
```
Alice | Age: 25 | City: Mumbai | Phone: N/A
Bob | Age: 0 | City: Delhi | Phone: N/A
Charlie | Age: 30 | City: Unknown | Phone: N/A
Diana | Age: 28 | City: Bangalore | Phone: 9876543210
```

**Key Concepts:** `.get()` for filling missing fields, data normalization
