# Editorials: Apply Inheritance

## Problem 1
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    pass

# Test the classes
dog = Dog("Buddy", 3)
print(f"Name: {dog.name}, Age: {dog.age}")
dog.make_sound()
```

### Explanation
- Inheritance is specified using parentheses: `class Dog(Animal):`
- The child class `Dog` automatically inherits all attributes and methods from `Animal`
- We can create a `Dog` object using the inherited `__init__` method
- The `pass` keyword creates an empty class body
- `Dog` instances have access to `name`, `age`, and `make_sound()` without redefining them
- This is the IS-A relationship: a Dog IS-AN Animal

## Problem 2
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        self.brand = brand
        self.model = model
        self.num_doors = num_doors

# Test the class
car = Car("Toyota", "Camry", 4)
print(f"Brand: {car.brand}")
print(f"Model: {car.model}")
print(f"Doors: {car.num_doors}")
```

### Explanation
- The child class can add new attributes beyond what the parent has
- `Car.__init__()` takes additional parameters (`num_doors`)
- We manually set `brand` and `model` in the child's `__init__`
- This extends the parent class by adding new functionality
- The child class can accept more parameters than the parent
- Note: This approach repeats code; using `super()` is better (covered in later LO)

## Problem 3
```python
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, ID: {self.id}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, id, salary, department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, ID: {self.id}, Salary: ${self.salary}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, id, salary, programming_language):
        self.name = name
        self.id = id
        self.salary = salary
        self.programming_language = programming_language

    def get_details(self):
        return f"Developer: {self.name}, ID: {self.id}, Salary: ${self.salary}, Language: {self.programming_language}"

# Test the classes
manager = Manager("Alice", "M001", 80000, "Engineering")
developer = Developer("Bob", "D001", 70000, "Python")

print(manager.get_details())
print(developer.get_details())
```

### Explanation
- Multiple child classes can inherit from the same parent
- Each child class adds its own unique attributes
- Child classes can override parent methods (method overriding)
- `get_details()` is redefined in each child to include their specific attributes
- This demonstrates polymorphism: same method name, different implementations
- Each child extends the base `Employee` class in its own way

## Problem 4
```python
import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Test the classes
circle = Circle(5)
square = Square(4)
triangle = Triangle(6, 3)

print(f"Circle area: {circle.area():.2f}")
print(f"Square area: {square.area():.2f}")
print(f"Triangle area: {triangle.area():.2f}")

# Demonstrate polymorphism
shapes = [circle, square, triangle]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
```

### Explanation
- All child classes inherit from `Shape` but provide their own `area()` implementation
- The base class provides a default implementation (returns 0)
- Each child overrides `area()` with the appropriate formula
- This is polymorphism: we can treat all shapes the same way (call `area()`)
- The loop demonstrates treating different objects uniformly through inheritance
- `**` operator is used for exponentiation (power)
- `math.pi` provides the value of π

## Problem 5
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_gpa(self):
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)

class Teacher(Person):
    def __init__(self, name, age, employee_id, subject, years_experience):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.subject = subject
        self.years_experience = years_experience

    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.subject} teacher with {self.years_experience} years of experience."

class TeachingAssistant(Student):
    def __init__(self, name, age, student_id, subject_taught, hours_per_week):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
        self.subject_taught = subject_taught
        self.hours_per_week = hours_per_week

    def introduce(self):
        return f"Hi, I'm {self.name}, a TA for {self.subject_taught}, working {self.hours_per_week} hours/week."

# Test the class hierarchy
student = Student("Alice", 20, "S001")
student.add_grade(3.5)
student.add_grade(3.8)
student.add_grade(4.0)

teacher = Teacher("Dr. Smith", 45, "T001", "Computer Science", 15)

ta = TeachingAssistant("Bob", 22, "S002", "Python Programming", 20)
ta.add_grade(3.9)
ta.add_grade(3.7)

# Demonstrate functionality
print(student.introduce())
print(f"Student GPA: {student.get_gpa():.2f}")

print("\n" + teacher.introduce())

print("\n" + ta.introduce())
print(f"TA GPA: {ta.get_gpa():.2f}")
print(f"TA Student ID: {ta.student_id}")
```

### Explanation
- Multi-level inheritance: `TeachingAssistant` inherits from `Student`, which inherits from `Person`
- `TeachingAssistant` has access to methods from both `Student` and `Person`
- Different classes can override the same method (`introduce()`) with their own version
- `TeachingAssistant` combines student attributes (grades, GPA) with teaching attributes
- This demonstrates a more complex class hierarchy
- Each level adds more specific behavior and attributes
- The TA can use `add_grade()` and `get_gpa()` inherited from `Student`

**Key Concepts**:
1. **Inheritance** allows code reuse by inheriting from parent classes
2. **IS-A relationship**: child IS-A type of parent (Dog IS-AN Animal)
3. **Method overriding**: child classes can replace parent methods
4. **Extension**: child classes add new attributes and methods
5. **Multi-level inheritance**: classes can inherit from classes that inherit from others
6. **Polymorphism**: treating different objects uniformly through a common interface
