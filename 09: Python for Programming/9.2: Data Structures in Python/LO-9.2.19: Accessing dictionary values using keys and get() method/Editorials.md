## Editorials: Accessing Dictionary Values

---

### Q1 Solution: Basic Access

```python
movie = {
    'title': 'Inception', 'director': 'Christopher Nolan',
    'year': 2010, 'rating': 8.8, 'genres': ['Sci-Fi', 'Thriller']
}

print(f"Title: {movie['title']}")
print(f"Director: {movie.get('director')}")
print(f"First genre: {movie['genres'][0]}")
print(f"Budget: {movie.get('budget', 'Unknown')}")
print(f"Has rating: {'rating' in movie}")
```

**Explanation:** `[]` and `.get()` both return the value for existing keys. For nested access, chain `[]` — `movie['genres'][0]` gets the list then its first element. `.get()` with a default handles missing keys gracefully.

---

### Q2 Solution: Safe Config Reader

```python
config = {'host': '192.168.1.1', 'port': 8080}

host = config.get('host', 'localhost')
port = config.get('port', 3000)
protocol = config.get('protocol', 'http')
timeout = config.get('timeout', 30)
debug = config.get('debug', False)

print(f"host: {host}")
print(f"port: {port}")
print(f"protocol: {protocol}")
print(f"timeout: {timeout}")
print(f"debug: {debug}")
```

**Explanation:** `.get()` with defaults lets you define sensible fallbacks. Existing values override defaults, so `host` and `port` use actual config values while `protocol`, `timeout`, and `debug` use the specified defaults.

---

### Q3 Solution: Nested Data Extraction

```python
api_response = {
    'status': 'success',
    'data': {
        'user': {
            'id': 42, 'name': 'Alice',
            'profile': {'avatar': 'alice.png', 'bio': 'Python developer'}
        },
        'posts': [
            {'id': 1, 'title': 'Hello World'},
            {'id': 2, 'title': 'Learning Python'}
        ]
    }
}

name = api_response['data']['user']['name']
bio = api_response['data']['user']['profile']['bio']
phone = api_response['data']['user'].get('phone', 'N/A')
second_post = api_response['data']['posts'][1]['title']
total_posts = len(api_response['data']['posts'])

print(f"Name: {name}")
print(f"Bio: {bio}")
print(f"Phone: {phone}")
print(f"Second post: {second_post}")
print(f"Total posts: {total_posts}")
```

---

### Q4 Solution: Student Lookup System

```python
students = {
    'S001': {'name': 'Alice', 'grade': 'A', 'courses': ['Math', 'Physics']},
    'S002': {'name': 'Bob', 'grade': 'B', 'courses': ['Chemistry', 'Biology']},
    'S003': {'name': 'Charlie', 'grade': 'A', 'courses': ['Math', 'English']}
}

def lookup(student_id):
    student = students.get(student_id)
    if student is None:
        print(f"{student_id}: Student not found")
    else:
        print(f"{student_id}: {student['name']}, Grade {student['grade']}, {len(student['courses'])} courses")

def get_students_by_grade(grade):
    return [s['name'] for s in students.values() if s['grade'] == grade]

lookup('S001')
lookup('S004')
lookup('S003')
print(f"Students with grade A: {get_students_by_grade('A')}")
```

---

### Q5 Solution: Data Transformer

```python
records = [
    {'name': 'Alice', 'age': 25, 'city': 'Mumbai'},
    {'name': 'Bob', 'city': 'Delhi'},
    {'name': 'Charlie', 'age': 30},
    {'name': 'Diana', 'age': 28, 'city': 'Bangalore', 'phone': '9876543210'},
]

def normalize(records):
    result = []
    for rec in records:
        normalized = {
            'name': rec.get('name', 'Unknown'),
            'age': rec.get('age', 0),
            'city': rec.get('city', 'Unknown'),
            'phone': rec.get('phone', 'N/A')
        }
        result.append(normalized)
    return result

for rec in normalize(records):
    print(f"{rec['name']} | Age: {rec['age']} | City: {rec['city']} | Phone: {rec['phone']}")
```

**Explanation:** `.get()` with defaults fills in missing fields consistently. This is a common pattern in data processing — normalizing inconsistent records into a uniform format.
