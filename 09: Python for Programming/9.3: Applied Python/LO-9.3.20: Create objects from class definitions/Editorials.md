## Editorials: Create Objects from Class Definitions

---

### Q1 Solution

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

books = [
    Book("1984", "Orwell", 328),
    Book("Dune", "Herbert", 412),
    Book("Hobbit", "Tolkien", 310),
]

for book in books:
    print(book.title)
```

---

### Q2 Solution

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(3, 4)

print(p1 is p2)   # False — different objects in memory
print(p1 == p2)    # True — __eq__ compares values
```

---

### Q3 Solution

```python
class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def from_string(cls, s):
        name, email, role = s.split(",")
        return cls(name.strip(), email.strip(), role.strip())

u = User.from_string("Alice, alice@mail.com, admin")
print(f"{u.name} ({u.role})")  # Alice (admin)
```

---

### Q4 Solution

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.done = True
                return

    def pending(self):
        return [t for t in self.tasks if not t.done]

    def summary(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.done)
        return f"{done}/{total} complete"

tl = TaskList()
tl.add_task("Write code")
tl.add_task("Test code")
tl.complete_task("Write code")
print(tl.summary())           # 1/2 complete
print(len(tl.pending()))      # 1
```

---

### Q5 Solution

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

def create_objects(class_type, data_list):
    return [class_type(**data) for data in data_list]

products = create_objects(Product, [
    {"name": "Laptop", "price": 999, "stock": 10},
    {"name": "Mouse", "price": 29, "stock": 50},
    {"name": "Keyboard", "price": 79, "stock": 30},
])

for p in products:
    print(f"{p.name}: ${p.price} ({p.stock} in stock)")
```

