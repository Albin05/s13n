# Editorials: Implement Composition

## Problem 1
```python
class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")
        print(f"Engine: {self.engine.horsepower}hp, {self.engine.type}")

# Test the classes
engine = Engine(200, "V6")
car = Car("Toyota", "Camry", engine)
car.display_info()
```

### Explanation
- Composition means one class contains an instance of another class
- The `Car` class HAS-AN `Engine` (not IS-AN Engine like inheritance)
- We create an `Engine` object first, then pass it to the `Car` constructor
- The car can access engine properties through `self.engine.horsepower`
- This represents a "whole-part" relationship: a car is made up of an engine
- Composition is more flexible than inheritance for HAS-A relationships
- If the engine is destroyed, it doesn't affect the Engine class definition

## Problem 2
```python
class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address.street}, {self.address.city} {self.address.zipcode}")

# Test the classes
address = Address("123 Main St", "Springfield", "12345")
person = Person("John Doe", address)
person.display_info()

# Can also create inline
person2 = Person("Jane Smith", Address("456 Oak Ave", "Riverside", "67890"))
person2.display_info()
```

### Explanation
- A `Person` object contains an `Address` object as an attribute
- This models the real-world relationship: a person has an address
- We can access address details through `self.address.street`, `self.address.city`, etc.
- The `Address` object can be created separately or inline during Person creation
- Multiple persons can share the same address object if needed
- This separates concerns: Address handles location data, Person handles personal data
- Composition makes the code modular and reusable

## Problem 3
```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                removed = self.books.pop(i)
                print(f"Removed: {removed}")
                return
        print(f"Book with ISBN {isbn} not found")

    def find_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                print(f"Found: {book}")
                return book
        print(f"Book '{title}' not found")
        return None

    def list_all_books(self):
        print(f"\n=== {self.name} Catalog ===")
        if not self.books:
            print("No books in library")
        else:
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

# Test the system
library = Library("City Library")

# Add books
book1 = Book("Python Programming", "John Smith", "978-1234567890")
book2 = Book("Data Science Basics", "Jane Doe", "978-0987654321")
book3 = Book("Web Development", "Bob Johnson", "978-1111111111")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Find a book
library.find_book("Python")

# Remove a book
library.remove_book("978-0987654321")

# List all books
library.list_all_books()
```

### Explanation
- The `Library` class contains a list of `Book` objects (composition)
- Library HAS-MANY Books (one-to-many relationship)
- The library manages the collection and provides methods to manipulate it
- Each `Book` maintains its own state independently
- The `__str__` method in Book makes printing easier
- `find_book()` uses case-insensitive partial matching for flexibility
- The books list is private to the library and accessed through methods
- This demonstrates aggregation: books can exist independently of the library

## Problem 4
```python
class CPU:
    def __init__(self, brand, speed, cores):
        self.brand = brand
        self.speed = speed
        self.cores = cores

    def __str__(self):
        return f"{self.brand} {self.speed}GHz, {self.cores} cores"

class RAM:
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def __str__(self):
        return f"{self.size}GB {self.type}"

class Storage:
    def __init__(self, capacity, type):
        self.capacity = capacity
        self.type = type

    def __str__(self):
        return f"{self.capacity}GB {self.type}"

class Computer:
    def __init__(self, brand, cpu, ram, storage):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def get_specs(self):
        specs = f"""
=== {self.brand} Computer Specifications ===
CPU: {self.cpu}
RAM: {self.ram}
Storage: {self.storage}
"""
        return specs

# Test the system
cpu = CPU("Intel Core i7", 3.5, 8)
ram = RAM(16, "DDR4")
storage = Storage(512, "SSD")

computer = Computer("Dell XPS", cpu, ram, storage)
print(computer.get_specs())

# Create another computer with different components
computer2 = Computer(
    "HP Pavilion",
    CPU("AMD Ryzen 5", 3.2, 6),
    RAM(8, "DDR4"),
    Storage(1000, "HDD")
)
print(computer2.get_specs())
```

### Explanation
- `Computer` is composed of multiple component objects (CPU, RAM, Storage)
- This models real-world composition: a computer is made up of these parts
- Each component is a separate class with its own attributes and behavior
- Components can be mixed and matched to create different configurations
- The `__str__` methods make components easy to display
- This is strong composition: components are meaningful as part of the computer
- Each component class is independent and reusable
- Multiple computers can use the same component types with different values

## Problem 5
```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Professor:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def __str__(self):
        return f"Prof. {self.name}"

class Course:
    def __init__(self, course_code, name, professor):
        self.course_code = course_code
        self.name = name
        self.professor = professor
        self.enrolled_students = []

    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            student.enrolled_courses.append(self)
            print(f"Enrolled {student.name} in {self.name}")
        else:
            print(f"{student.name} is already enrolled in {self.name}")

    def get_enrollment_count(self):
        return len(self.enrolled_students)

    def __str__(self):
        return f"{self.course_code}: {self.name} (Prof. {self.professor.name})"

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"Added {course.name} to {self.name} department")

    def get_total_enrollment(self):
        total = 0
        for course in self.courses:
            total += course.get_enrollment_count()
        return total

    def display_stats(self):
        print(f"\n=== {self.name} Department Statistics ===")
        print(f"Total Courses: {len(self.courses)}")
        print(f"Total Enrollment: {self.get_total_enrollment()}")
        print("\nCourse Details:")
        for course in self.courses:
            print(f"  {course}")
            print(f"    Instructor: {course.professor}")
            print(f"    Enrolled: {course.get_enrollment_count()} students")
            if course.enrolled_students:
                for student in course.enrolled_students:
                    print(f"      - {student}")

# Test the system
# Create professors
prof1 = Professor("Dr. Smith", "E001", "Computer Science")
prof2 = Professor("Dr. Johnson", "E002", "Computer Science")

# Create courses
course1 = Course("CS101", "Introduction to Programming", prof1)
course2 = Course("CS201", "Data Structures", prof2)

# Create department and add courses
cs_dept = Department("Computer Science")
cs_dept.add_course(course1)
cs_dept.add_course(course2)

# Create students
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")
student3 = Student("Charlie", "S003")

# Enroll students
print("\n=== Enrollments ===")
course1.enroll_student(student1)
course1.enroll_student(student2)
course1.enroll_student(student3)
course2.enroll_student(student1)
course2.enroll_student(student2)

# Display statistics
cs_dept.display_stats()

# Show student's enrolled courses
print(f"\n=== {student1.name}'s Courses ===")
for course in student1.enrolled_courses:
    print(f"  - {course}")
```

### Explanation
- Complex composition with multiple object relationships
- `Course` HAS-A `Professor` (one-to-one composition)
- `Course` HAS-MANY `Students` (one-to-many composition/aggregation)
- `Department` HAS-MANY `Courses` (one-to-many composition)
- `Student` HAS-MANY `Courses` (many-to-many relationship through enrollment)
- `enroll_student()` maintains bidirectional relationship: adds course to student AND student to course
- This prevents inconsistent state where a student is in a course but course doesn't know about student
- The `display_stats()` method demonstrates navigating the composed object graph
- Objects maintain references to each other, creating a network of relationships
- This models real-world university structure where entities are interconnected

**Key Concepts**:
1. **Composition** represents HAS-A relationships (Car HAS-AN Engine)
2. **Aggregation** is weak composition where parts can exist independently (Library HAS Books)
3. **One-to-one**: one object contains one other object
4. **One-to-many**: one object contains multiple objects (collections)
5. **Many-to-many**: objects on both sides contain collections of each other
6. **Bidirectional relationships**: objects maintain references to each other
7. **Composition vs Inheritance**: use composition for HAS-A, inheritance for IS-A
8. **Modularity**: composed objects can be reused and tested independently
