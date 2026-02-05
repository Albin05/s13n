# Lecture Script: LO-69 Implement Composition

## [0:00-0:02] Hook (2 min)
**Say**: "A car HAS-A engine, HAS-A steering wheel, HAS-A GPS. You don't say a car IS-A engine! That's the difference between composition and inheritance. Composition is about building complex objects by combining simpler ones. Think of it like LEGO blocks — you create amazing structures by putting pieces together!"

**Demo**:
```python
class Engine:
    def start(self):
        return "Engine running"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine!

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Engine running
```

**Say**: "Car contains an Engine object. That's composition! Let's master this powerful design pattern."

## [0:02-0:06] Composition vs Inheritance (4 min)

**Say**: "When should you use composition instead of inheritance? Remember: IS-A vs HAS-A!"

**Live Code**:
```python
# IS-A relationship - Use Inheritance
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        print("Woof!")

# HAS-A relationship - Use Composition
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge = capacity

    def use_power(self, amount):
        self.charge -= amount

class Laptop:
    def __init__(self):
        self.battery = Battery(100)  # Laptop HAS-A Battery

    def work(self):
        if self.battery.charge > 0:
            self.battery.use_power(10)
            print(f"Working... Battery: {self.battery.charge}%")
        else:
            print("Battery dead!")

# Test
laptop = Laptop()
laptop.work()  # Working... Battery: 90%
laptop.work()  # Working... Battery: 80%
```

**Point out**: "Dog IS-A Animal (inheritance). Laptop HAS-A Battery (composition)."

**Emphasize**: "Composition is more flexible! You can swap components, mix and match, and change behavior at runtime!"

## [0:06-0:10] Building Complex Objects (4 min)

**Say**: "Let's build a computer from components. This shows the power of composition."

**Live Code**:
```python
class CPU:
    def __init__(self, cores, speed):
        self.cores = cores
        self.speed = speed

    def process(self, task):
        return f"Processing {task} on {self.cores} cores @ {self.speed}GHz"

class RAM:
    def __init__(self, size_gb):
        self.size_gb = size_gb
        self.used = 0

    def allocate(self, amount):
        if self.used + amount <= self.size_gb:
            self.used += amount
            return True
        return False

class Storage:
    def __init__(self, capacity_gb):
        self.capacity_gb = capacity_gb
        self.files = []

    def save_file(self, filename, size):
        self.files.append({"name": filename, "size": size})
        return f"Saved {filename}"

class Computer:
    def __init__(self):
        self.cpu = CPU(8, 3.5)        # Composition!
        self.ram = RAM(16)             # Composition!
        self.storage = Storage(512)    # Composition!

    def run_program(self, program, ram_needed):
        if self.ram.allocate(ram_needed):
            result = self.cpu.process(program)
            print(result)
            print(f"RAM: {self.ram.used}/{self.ram.size_gb}GB")
            return True
        print("Not enough RAM!")
        return False

    def save(self, filename, size):
        print(self.storage.save_file(filename, size))

# Test
pc = Computer()
pc.run_program("Python IDE", 4)
# Processing Python IDE on 8 cores @ 3.5GHz
# RAM: 4/16GB

pc.run_program("Web Browser", 8)
# Processing Web Browser on 8 cores @ 3.5GHz
# RAM: 12/16GB

pc.save("project.py", 0.5)
# Saved project.py
```

**Say**: "Computer is built from CPU, RAM, and Storage. Each component is independent and reusable!"

## [0:10-0:14] Real-World Example: Car System (4 min)

**Say**: "Let's build a realistic car with multiple components."

**Live Code**:
```python
class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"{self.horsepower}HP {self.fuel_type} engine started"

    def stop(self):
        self.is_running = False
        return "Engine stopped"

class GPS:
    def __init__(self):
        self.destination = None

    def set_destination(self, location):
        self.destination = location
        return f"Route set to {location}"

    def navigate(self):
        if self.destination:
            return f"Navigating to {self.destination}"
        return "No destination set"

class MusicSystem:
    def __init__(self):
        self.current_song = None
        self.volume = 50

    def play(self, song):
        self.current_song = song
        return f"Playing: {song} (Volume: {self.volume})"

    def set_volume(self, level):
        self.volume = max(0, min(100, level))
        return f"Volume: {self.volume}"

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = Engine(250, "Gasoline")  # Composition
        self.gps = GPS()                       # Composition
        self.music = MusicSystem()             # Composition

    def start(self):
        print(f"Starting {self.brand} {self.model}")
        print(self.engine.start())

    def drive_to(self, location):
        if self.engine.is_running:
            print(self.gps.set_destination(location))
            print(self.gps.navigate())
            print(self.music.play("Highway to Hell"))
        else:
            print("Start the engine first!")

# Test
car = Car("Toyota", "Camry")
car.start()
# Starting Toyota Camry
# 250HP Gasoline engine started

car.drive_to("San Francisco")
# Route set to San Francisco
# Navigating to San Francisco
# Playing: Highway to Hell (Volume: 50)
```

**Say**: "Each component (Engine, GPS, Music) can be developed, tested, and replaced independently. That's modularity!"

## [0:14-0:18] Composition with Lists of Objects (4 min)

**Say**: "Objects can contain LISTS of other objects. Super powerful!"

**Live Code**:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return f"{self.code}: {self.name}"

class Classroom:
    def __init__(self, room_number, course):
        self.room_number = room_number
        self.course = course          # Composition
        self.students = []            # List of Student objects!

    def enroll_student(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.course.name}")

    def take_attendance(self):
        print(f"\nAttendance for {self.course}")
        print(f"Room: {self.room_number}")
        print(f"Students present: {len(self.students)}")
        for student in self.students:
            print(f"  - {student}")

    def get_average_age(self):
        if not self.students:
            return 0
        return sum(s.age for s in self.students) / len(self.students)

# Test
python_course = Course("CS101", "Introduction to Python")
classroom = Classroom("A-202", python_course)

# Enroll students
classroom.enroll_student(Student("Alice", 20))
# Alice enrolled in Introduction to Python

classroom.enroll_student(Student("Bob", 22))
# Bob enrolled in Introduction to Python

classroom.enroll_student(Student("Charlie", 21))
# Charlie enrolled in Introduction to Python

classroom.take_attendance()
# Attendance for CS101: Introduction to Python
# Room: A-202
# Students present: 3
#   - Alice (20)
#   - Bob (22)
#   - Charlie (21)

print(f"\nAverage age: {classroom.get_average_age():.1f}")
# Average age: 21.0
```

**Point out**: "Classroom contains a Course object AND a list of Student objects. Composition with collections!"

## [0:18-0:21] Real-World Example: Order System (3 min)

**Say**: "Let's build a restaurant order system with nested composition."

**Live Code**:
```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

class Order:
    def __init__(self, order_id, table_number):
        self.order_id = order_id
        self.table_number = table_number
        self.items = []  # List of MenuItem objects

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def get_total(self):
        return sum(item.price for item in self.items)

    def print_receipt(self):
        print(f"\n{'='*30}")
        print(f"Order #{self.order_id} - Table {self.table_number}")
        print('='*30)
        for item in self.items:
            print(f"  {item}")
        print('-'*30)
        print(f"Total: ${self.get_total():.2f}")
        print('='*30)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.orders = []  # List of Order objects

    def create_order(self, table_number):
        order_id = f"ORD-{len(self.orders) + 1:03d}"
        order = Order(order_id, table_number)
        self.orders.append(order)
        print(f"Created order {order_id} for table {table_number}")
        return order

    def get_total_sales(self):
        return sum(order.get_total() for order in self.orders)

# Test
restaurant = Restaurant("The Python Cafe")

order1 = restaurant.create_order(5)
# Created order ORD-001 for table 5

order1.add_item(MenuItem("Burger", 12.99))
# Added: Burger ($12.99)

order1.add_item(MenuItem("Fries", 4.99))
# Added: Fries ($4.99)

order1.add_item(MenuItem("Soda", 2.99))
# Added: Soda ($2.99)

order1.print_receipt()
# ==============================
# Order #ORD-001 - Table 5
# ==============================
#   Burger ($12.99)
#   Fries ($4.99)
#   Soda ($2.99)
# ------------------------------
# Total: $20.97
# ==============================

print(f"\nTotal sales: ${restaurant.get_total_sales():.2f}")
# Total sales: $20.97
```

**Say**: "Restaurant contains Orders, Orders contain MenuItems. Multi-level composition!"

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Create a Library system with Books and Members. Library has lists of both."

**Skeleton**:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []    # TODO: List of Book objects
        self.members = []  # TODO: List of Member objects

    def add_book(self, book):
        # TODO: Add book to library
        pass

    def register_member(self, member):
        # TODO: Add member
        pass

    def lend_book(self, book_title, member_id):
        # TODO: Find book and member, lend if available
        pass

# Test
library = Library("City Library")
library.add_book(Book("Python 101", "John Doe"))
library.register_member(Member("Alice", "M001"))
library.lend_book("Python 101", "M001")
```

**Solution** (show after 1-2 minutes):
```python
def add_book(self, book):
    self.books.append(book)
    print(f"Added: {book.title}")

def register_member(self, member):
    self.members.append(member)
    print(f"Registered: {member.name}")

def lend_book(self, book_title, member_id):
    book = next((b for b in self.books if b.title == book_title), None)
    member = next((m for m in self.members if m.member_id == member_id), None)

    if book and member and book.is_available:
        book.is_available = False
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed {book.title}")
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **HAS-A relationship**: Objects contain other objects as attributes
2. **Flexibility**: Swap components without changing the container
3. **Modularity**: Components can be developed and tested independently
4. **Reusability**: Same component can be used in multiple containers
5. **Favor composition**: Often better than inheritance for flexibility

**Common Mistakes**:
- Confusing IS-A (inheritance) with HAS-A (composition)
- Not initializing component objects in __init__
- Exposing too much internal detail of components
- Creating tight coupling between container and components

**Composition vs Inheritance**:
- **Inheritance**: Dog IS-A Animal
- **Composition**: Car HAS-A Engine
- When in doubt, choose composition for more flexibility!

**When to Use Composition**:
- Building complex objects from simpler parts
- When components can exist independently
- When you need runtime flexibility
- When you want to avoid deep inheritance hierarchies

**Closing**: "Composition is like building with LEGO blocks — combine simple, reusable components to create complex systems. It's one of the most powerful design patterns in OOP. Master it, and you'll write flexible, maintainable code!"
