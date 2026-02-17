# Lecture Notes: Implement Composition

## Implement Composition

Building complex objects from simpler ones


---

<div align="center">

![Tree structure showing inheritance](https://images.unsplash.com/photo-1502101872923-d48509bff386?w=800&q=80)

*Inheritance allows classes to inherit properties from parent classes*

</div>

---

## Introduction

Composition implements **object aggregation** - building complex objects from simpler parts! This is **"has-a" relationships** vs inheritance's "is-a". Composition is **flexible assembly** - mix and match components like LEGO blocks. **Gang of Four**: "Favor composition over inheritance"!

### Why Composition Transforms Design

**Problem with deep inheritance**: Rigid, fragile hierarchies:
```python
# BRITTLE - inheritance explosion!
class Vehicle: pass
class Car(Vehicle): pass
class ElectricCar(Car): pass
class ElectricSportsCar(ElectricCar): pass
# Deep hierarchy - changes at top break everything!
```

**Solution with composition**: Flexible component assembly:
```python
# FLEXIBLE - mix components!
class Engine: pass
class Battery: pass
class GPS: pass

class Car:
    def __init__(self):
        self.engine = Engine()    # Has-a engine
        self.battery = Battery()  # Has-a battery
        self.gps = GPS()          # Has-a GPS
# Swap components easily - no deep hierarchy!
```

**This is modularity** - build complex from simple!

### Historical Context

**Composition** favored by **Gang of Four** (1994 Design Patterns book) - "prefer object composition over class inheritance". **Why?** Inheritance creates **tight coupling** (parent changes break children), composition creates **loose coupling** (components independent)!

**Unix philosophy** (1970s): "Do one thing well, compose programs". **Object composition** applies same principle - small classes with single responsibility, composed into complex systems!

**Aggregation vs composition**: **Composition** = strong ownership (Engine dies with Car). **Aggregation** = weak ownership (Driver exists independently of Car). Most OOP uses composition - simpler lifecycle!

### Real-World Analogies

**Composition like computer assembly**:
- **Computer**: Has-a CPU, RAM, Storage, Monitor (components)
- **Not inheritance**: Computer doesn't inherit from CPU!
- **Mix and match**: Swap CPU without changing whole design
**Build custom systems from standard parts!**

**Or like human body**:
```python
class Heart:
    def beat(self): return "Beating"

class Brain:
    def think(self): return "Thinking"

class Human:
    def __init__(self):
        self.heart = Heart()  # Has-a heart
        self.brain = Brain()  # Has-a brain
    def live(self):
        print(self.heart.beat())
        print(self.brain.think())
# Organs are components, not inheritance!
```

**Or like restaurant kitchen**:
- **Restaurant**: Has-a Kitchen, Dining Room, Staff
- **Kitchen**: Has-a Oven, Refrigerator, Sink
- **Each component**: Independent, replaceable
**Complex business from simple parts!**

### Composition vs Inheritance: The Design Choice

**Use inheritance when**:
- True "is-a" relationship (Dog IS-A Animal)
- Shared behavior across subtypes
- Polymorphism needed

**Use composition when**:
- "Has-a" relationship (Car HAS-A Engine)
- Need flexibility to change components
- Want loose coupling
- Components used by multiple classes

**General rule**: **Prefer composition** - easier to test, modify, extend!

---
### Understanding the Concept

Composition is a design principle where a class contains instances of other classes as attributes, creating a "has-a" relationship. Instead of inheriting from a class (is-a), you include it as a component (has-a).

**Key concepts**: has-a relationship, object composition, aggregation, building complex objects

### Syntax and Usage

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self):
        return self.engine.start()
```

### Basic Composition

```python
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge = capacity

    def use_power(self, amount):
        self.charge = max(0, self.charge - amount)
        return self.charge > 0

class Processor:
    def __init__(self, speed):
        self.speed = speed

    def process(self):
        return f"Processing at {self.speed}GHz"

class Laptop:
    def __init__(self, brand):
        self.brand = brand
        self.battery = Battery(100)  # Composition
        self.processor = Processor(2.5)  # Composition

    def use(self):
        if self.battery.use_power(10):
            return self.processor.process()
        return "Battery dead"

# Usage
laptop = Laptop("Dell")
print(laptop.use())  # Processing at 2.5GHz
print(laptop.use())  # Processing at 2.5GHz
print(f"Battery: {laptop.battery.charge}%")  # Battery: 80%
```

### Practical Examples

#### Example 1: Car System

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

class Wheel:
    def __init__(self, size):
        self.size = size
        self.pressure = 32

    def inflate(self, psi):
        self.pressure = psi
        print(f"Wheel inflated to {psi} PSI")

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

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = Engine(250, "Gasoline")  # Composition
        self.wheels = [Wheel(18) for _ in range(4)]  # Composition
        self.gps = GPS()  # Composition

    def start(self):
        print(f"Starting {self.brand} {self.model}")
        print(self.engine.start())

    def check_wheels(self):
        print("Checking all wheels:")
        for i, wheel in enumerate(self.wheels, 1):
            print(f"  Wheel {i}: {wheel.size}\" - {wheel.pressure} PSI")

    def drive_to(self, location):
        if self.engine.is_running:
            print(self.gps.set_destination(location))
            print(self.gps.navigate())
        else:
            print("Start the engine first!")

# Usage
car = Car("Toyota", "Camry")
car.start()
# Starting Toyota Camry
# 250HP Gasoline engine started

car.check_wheels()
# Checking all wheels:
#   Wheel 1: 18" - 32 PSI
#   Wheel 2: 18" - 32 PSI
#   Wheel 3: 18" - 32 PSI
#   Wheel 4: 18" - 32 PSI

car.drive_to("San Francisco")
# Route set to San Francisco
# Navigating to San Francisco
```

#### Example 2: Computer System

```python
class CPU:
    def __init__(self, cores, speed):
        self.cores = cores
        self.speed = speed
        self.temperature = 40

    def process(self, task):
        self.temperature += 5
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

    def free(self, amount):
        self.used = max(0, self.used - amount)

class Storage:
    def __init__(self, capacity_gb, storage_type):
        self.capacity_gb = capacity_gb
        self.storage_type = storage_type
        self.used = 0
        self.files = []

    def save_file(self, filename, size_gb):
        if self.used + size_gb <= self.capacity_gb:
            self.files.append({"name": filename, "size": size_gb})
            self.used += size_gb
            return f"Saved {filename} ({size_gb}GB)"
        return "Not enough storage"

    def get_free_space(self):
        return self.capacity_gb - self.used

class Monitor:
    def __init__(self, size, resolution):
        self.size = size
        self.resolution = resolution

    def display(self, content):
        return f"[{self.size}\" {self.resolution}] {content}"

class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.cpu = CPU(8, 3.5)
        self.ram = RAM(16)
        self.storage = Storage(512, "SSD")
        self.monitor = Monitor(27, "2560x1440")
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} computer starting...")
        print(self.cpu.process("boot sequence"))
        self.ram.allocate(2)
        print(f"RAM: {self.ram.used}GB / {self.ram.size_gb}GB allocated")
        print(self.monitor.display("Welcome!"))

    def run_program(self, program_name, ram_needed):
        if not self.is_on:
            return "Computer is off"

        if self.ram.allocate(ram_needed):
            result = self.cpu.process(program_name)
            print(self.monitor.display(result))
            print(f"CPU Temperature: {self.cpu.temperature}°C")
            return f"{program_name} running"
        return "Not enough RAM"

    def save_work(self, filename, size):
        result = self.storage.save_file(filename, size)
        print(result)
        print(f"Storage: {self.storage.used}GB / {self.storage.capacity_gb}GB used")
        print(f"Free space: {self.storage.get_free_space()}GB")

    def system_info(self):
        print(f"\n{self.brand} System Information:")
        print(f"CPU: {self.cpu.cores} cores @ {self.cpu.speed}GHz")
        print(f"RAM: {self.ram.size_gb}GB (Using: {self.ram.used}GB)")
        print(f"Storage: {self.storage.capacity_gb}GB {self.storage.type} (Free: {self.storage.get_free_space()}GB)")
        print(f"Monitor: {self.monitor.size}\" {self.monitor.resolution}")

# Usage
pc = Computer("Dell")
pc.power_on()
# Dell computer starting...
# Processing boot sequence on 8 cores @ 3.5GHz
# RAM: 2GB / 16GB allocated
# [27" 2560x1440] Welcome!

print()
pc.run_program("Python IDE", 4)
# [27" 2560x1440] Processing Python IDE on 8 cores @ 3.5GHz
# CPU Temperature: 45°C
# Python IDE running

print()
pc.save_work("project.py", 0.1)
# Saved project.py (0.1GB)
# Storage: 0.1GB / 512GB used
# Free space: 511.9GB

pc.system_info()
# Dell System Information:
# CPU: 8 cores @ 3.5GHz
# RAM: 16GB (Using: 6GB)
# Storage: 512GB SSD (Free: 511.9GB)
# Monitor: 27" 2560x1440
```

#### Example 3: University System

```python
class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.state} {self.zipcode}"

class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.code}: {self.name} ({self.credits} credits)"

class Grade:
    def __init__(self, course, score):
        self.course = course
        self.score = score

    def get_letter_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        return "F"

class Student:
    def __init__(self, student_id, name, address):
        self.student_id = student_id
        self.name = name
        self.address = address  # Composition
        self.enrolled_courses = []  # Composition
        self.grades = []  # Composition

    def enroll(self, course):
        self.enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course.name}")

    def add_grade(self, course, score):
        grade = Grade(course, score)
        self.grades.append(grade)
        print(f"Grade added: {course.name} - {score}% ({grade.get_letter_grade()})")

    def get_gpa(self):
        if not self.grades:
            return 0.0

        grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        total_points = sum(grade_points[g.get_letter_grade()] * g.course.credits
                          for g in self.grades)
        total_credits = sum(g.course.credits for g in self.grades)
        return total_points / total_credits if total_credits > 0 else 0.0

    def display_transcript(self):
        print(f"\nTranscript for {self.name} (ID: {self.student_id})")
        print(f"Address: {self.address.get_full_address()}")
        print("\nGrades:")
        for grade in self.grades:
            print(f"  {grade.course} - {grade.score}% ({grade.get_letter_grade()})")
        print(f"\nGPA: {self.get_gpa():.2f}")

# Usage
address = Address("123 College St", "Boston", "MA", "02101")
student = Student("S12345", "Alice Johnson", address)

# Create courses
python = Course("CS101", "Introduction to Python", 3)
math = Course("MATH201", "Calculus I", 4)
physics = Course("PHYS101", "Physics I", 4)

# Enroll in courses
student.enroll(python)
# Alice Johnson enrolled in Introduction to Python

student.enroll(math)
# Alice Johnson enrolled in Calculus I

student.enroll(physics)
# Alice Johnson enrolled in Physics I

# Add grades
student.add_grade(python, 95)
# Grade added: Introduction to Python - 95% (A)

student.add_grade(math, 88)
# Grade added: Calculus I - 88% (B)

student.add_grade(physics, 92)
# Grade added: Physics I - 92% (A)

# Display transcript
student.display_transcript()
# Transcript for Alice Johnson (ID: S12345)
# Address: 123 College St, Boston, MA 02101
#
# Grades:
#   CS101: Introduction to Python (3 credits) - 95% (A)
#   MATH201: Calculus I (4 credits) - 88% (B)
#   PHYS101: Physics I (4 credits) - 92% (A)
#
# GPA: 3.73
```

#### Example 4: Restaurant Order System

```python
class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_subtotal(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name} = ${self.get_subtotal():.2f}"

class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True
        print(f"Table {self.table_number} is now occupied")

    def free(self):
        self.is_occupied = False
        print(f"Table {self.table_number} is now free")

class Order:
    def __init__(self, order_id, table):
        self.order_id = order_id
        self.table = table  # Composition
        self.items = []  # Composition
        self.status = "pending"

    def add_item(self, menu_item, quantity):
        order_item = OrderItem(menu_item, quantity)
        self.items.append(order_item)
        print(f"Added to order: {order_item}")

    def remove_item(self, menu_item_name):
        self.items = [item for item in self.items
                     if item.menu_item.name != menu_item_name]
        print(f"Removed {menu_item_name} from order")

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items)

    def apply_tax(self, tax_rate=0.08):
        return self.get_total() * tax_rate

    def apply_tip(self, tip_percent=0.15):
        return self.get_total() * tip_percent

    def get_final_total(self):
        subtotal = self.get_total()
        tax = self.apply_tax()
        tip = self.apply_tip()
        return subtotal + tax + tip

    def print_receipt(self):
        print(f"\n{'='*40}")
        print(f"Order #{self.order_id} - Table {self.table.table_number}")
        print(f"{'='*40}")

        for item in self.items:
            print(f"  {item}")

        print(f"{'-'*40}")
        print(f"Subtotal:        ${self.get_total():>10.2f}")
        print(f"Tax (8%):        ${self.apply_tax():>10.2f}")
        print(f"Tip (15%):       ${self.apply_tip():>10.2f}")
        print(f"{'='*40}")
        print(f"TOTAL:           ${self.get_final_total():>10.2f}")
        print(f"{'='*40}\n")

# Usage
# Create menu items
burger = MenuItem("Classic Burger", 12.99, "Main")
fries = MenuItem("French Fries", 4.99, "Side")
soda = MenuItem("Soft Drink", 2.99, "Beverage")
salad = MenuItem("Caesar Salad", 8.99, "Appetizer")

# Create table
table5 = Table(5, 4)
table5.occupy()
# Table 5 is now occupied

# Create order
order = Order("ORD-001", table5)

# Add items
order.add_item(burger, 2)
# Added to order: 2x Classic Burger = $25.98

order.add_item(fries, 2)
# Added to order: 2x French Fries = $9.98

order.add_item(soda, 3)
# Added to order: 3x Soft Drink = $8.97

order.add_item(salad, 1)
# Added to order: 1x Caesar Salad = $8.99

# Print receipt
order.print_receipt()
# ========================================
# Order #ORD-001 - Table 5
# ========================================
#   2x Classic Burger = $25.98
#   2x French Fries = $9.98
#   3x Soft Drink = $8.97
#   1x Caesar Salad = $8.99
# ----------------------------------------
# Subtotal:        $     53.92
# Tax (8%):        $      4.31
# Tip (15%):       $      8.09
# ========================================
# TOTAL:           $     66.32
# ========================================
```

#### Example 5: Library Management System

```python
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f"{self.name} (b. {self.birth_year})"

class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author  # Composition
        self.year = year
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author.name} ({self.year})"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

class Loan:
    def __init__(self, book, member, due_days=14):
        self.book = book
        self.member = member
        self.due_days = due_days
        self.is_returned = False

    def return_book(self):
        self.is_returned = True
        self.book.is_available = True

    def __str__(self):
        status = "Returned" if self.is_returned else f"Due in {self.due_days} days"
        return f"{self.book.title} - {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Composition
        self.members = []  # Composition
        self.loans = []  # Composition

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member}")

    def lend_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if not book:
            print("Book not found")
            return False

        if not member:
            print("Member not found")
            return False

        if not book.is_available:
            print(f"{book.title} is not available")
            return False

        loan = Loan(book, member)
        self.loans.append(loan)
        book.is_available = False
        member.borrowed_books.append(book)
        print(f"Loaned {book.title} to {member.name}")
        return True

    def return_book(self, isbn, member_id):
        loan = next((l for l in self.loans
                    if l.book.isbn == isbn and
                    l.member.member_id == member_id and
                    not l.is_returned), None)

        if loan:
            loan.return_book()
            loan.member.borrowed_books.remove(loan.book)
            print(f"{loan.member.name} returned {loan.book.title}")
            return True

        print("Loan not found")
        return False

    def show_available_books(self):
        print(f"\nAvailable Books at {self.name}:")
        available = [b for b in self.books if b.is_available]
        if available:
            for book in available:
                print(f"  [{book.isbn}] {book}")
        else:
            print("  No books available")

    def show_member_loans(self, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Member not found")
            return

        print(f"\n{member.name}'s Borrowed Books:")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"  {book}")
        else:
            print("  No borrowed books")

# Usage
library = Library("City Public Library")

# Create authors
rowling = Author("J.K. Rowling", 1965)
tolkien = Author("J.R.R. Tolkien", 1892)
orwell = Author("George Orwell", 1903)

# Create and add books
book1 = Book("ISBN001", "Harry Potter", rowling, 1997)
book2 = Book("ISBN002", "The Hobbit", tolkien, 1937)
book3 = Book("ISBN003", "1984", orwell, 1949)

library.add_book(book1)
# Added book: 'Harry Potter' by J.K. Rowling (1997)

library.add_book(book2)
# Added book: 'The Hobbit' by J.R.R. Tolkien (1937)

library.add_book(book3)
# Added book: '1984' by George Orwell (1949)

# Register members
alice = Member("M001", "Alice")
bob = Member("M002", "Bob")

library.register_member(alice)
# Registered member: Alice (ID: M001)

library.register_member(bob)
# Registered member: Bob (ID: M002)

# Show available books
library.show_available_books()
# Available Books at City Public Library:
#   [ISBN001] 'Harry Potter' by J.K. Rowling (1997)
#   [ISBN002] 'The Hobbit' by J.R.R. Tolkien (1937)
#   [ISBN003] '1984' by George Orwell (1949)

# Lend books
library.lend_book("ISBN001", "M001")
# Loaned Harry Potter to Alice

library.lend_book("ISBN003", "M002")
# Loaned 1984 to Bob

# Show member's loans
library.show_member_loans("M001")
# Alice's Borrowed Books:
#   'Harry Potter' by J.K. Rowling (1997)

# Return a book
library.return_book("ISBN001", "M001")
# Alice returned Harry Potter

# Show available books again
library.show_available_books()
# Available Books at City Public Library:
#   [ISBN001] 'Harry Potter' by J.K. Rowling (1997)
#   [ISBN002] 'The Hobbit' by J.R.R. Tolkien (1937)
```

### Composition vs Inheritance

**Use Composition when:**
- You have a "has-a" relationship
- You want more flexibility
- You need to combine multiple components
- Components can exist independently

**Use Inheritance when:**
- You have an "is-a" relationship
- You want to share behavior
- Subclasses are specialized versions of the parent

### Best Practices

1. **Favor composition over inheritance**: More flexible and maintainable
2. **Keep components independent**: Each component should work on its own
3. **Use clear naming**: Make relationships obvious
4. **Encapsulate components**: Don't expose internal details
5. **Initialize in __init__**: Create component objects in the constructor

### Common Mistakes

1. **Exposing too much**: Don't let external code directly modify components
2. **Tight coupling**: Components shouldn't know about their container
3. **Not initializing**: Always create component objects in __init__
4. **Mixing relationships**: Be clear about composition vs aggregation

### When to Use

Use composition when:
- Building complex systems from simple parts
- You need flexibility to change components
- Components have different lifecycles
- You want to avoid deep inheritance hierarchies

### Key Takeaways

1. Composition creates "has-a" relationships
2. Objects contain other objects as attributes
3. More flexible than inheritance
4. Promotes code reuse and modularity
5. Components can be independently tested and maintained
6. Essential for building complex, maintainable systems
