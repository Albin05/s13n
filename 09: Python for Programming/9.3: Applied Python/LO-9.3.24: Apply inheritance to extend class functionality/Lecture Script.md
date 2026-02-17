# Lecture Script: LO-66 Apply Inheritance


### CS Theory Bite

> **Origin**: Inheritance models **taxonomic hierarchies** (Simula 67) — like biological classification. The **Liskov Substitution Principle** (1987): anywhere a parent works, a child should work too.
>
> **Analogy**: Inheritance is like **genetic traits** — children inherit features from parents but can develop their own unique characteristics.
>
> **Why it matters**: Inheritance enables code reuse — write common behavior once, specialize in subclasses.


## [0:00-0:02] Hook (2 min)
**Say**: "Think about vehicles. All vehicles move, but a car drives, a plane flies, and a boat sails. They share common features but have unique behaviors. That's inheritance! We create a parent class with shared features, then child classes with specialized features."

**Demo**:
```python
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):  # Car inherits from Vehicle
    def drive(self):
        print("Driving on road!")

car = Car()
car.move()   # Inherited from Vehicle!
car.drive()  # Defined in Car
```

**Say**: "Car automatically gets move() from Vehicle. No code duplication!"

## [0:02-0:06] Basic Inheritance Syntax (4 min)

**Say**: "Let's build an animal hierarchy."

**Live Code**:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Cat inherits from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

# Test it
dog = Dog("Buddy")
dog.eat()   # From Animal
dog.sleep() # From Animal
dog.bark()  # From Dog

cat = Cat("Whiskers")
cat.eat()   # From Animal
cat.meow()  # From Cat
```

**Point out**: "Dog and Cat both get eat() and sleep() from Animal, plus they add their own unique methods!"

**Emphasize**: "Syntax: class ChildClass(ParentClass): — that's it!"

## [0:06-0:10] Why Use Inheritance? (4 min)

**Say**: "Inheritance prevents code duplication. Watch what happens WITHOUT inheritance:"

**Show the problem**:
```python
# Without inheritance - code duplication!
class Dog:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def bark(self):
        print("Woof!")

class Cat:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")  # Duplicated!
    def meow(self):
        print("Meow!")
```

**Say**: "We wrote eat() and sleep() TWICE! If we fix a bug in one, we have to fix it everywhere. Inheritance solves this!"

## [0:10-0:14] Real-World Example: Employees (4 min)

**Say**: "Let's model a company with different types of employees."

**Live Code**:
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

    def get_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

class Developer(Employee):
    def code(self):
        print(f"{self.name} is writing code")

    def debug(self):
        print(f"{self.name} is fixing bugs")

class Manager(Employee):
    def manage(self):
        print(f"{self.name} is managing the team")

    def hold_meeting(self):
        print(f"{self.name} is holding a meeting")

# Create employees
dev = Developer("Alice", 80000)
dev.work()      # From Employee
dev.get_info()  # From Employee
dev.code()      # From Developer

mgr = Manager("Bob", 90000)
mgr.work()         # From Employee
mgr.get_info()     # From Employee
mgr.hold_meeting() # From Manager
```

**Say**: "Every employee can work() and get_info(). Developers can code(), managers can hold_meeting(). Inheritance lets us organize this cleanly!"

## [0:14-0:18] Multiple Levels of Inheritance (4 min)

**Say**: "Inheritance can go multiple levels: grandparent → parent → child."

**Live Code**:
```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):  # Mammal inherits from Animal
    def feed_young(self):
        print("Feeding young with milk")

class Dog(Mammal):  # Dog inherits from Mammal
    def bark(self):
        print("Woof!")

dog = Dog()
dog.breathe()     # From Animal (grandparent)
dog.feed_young()  # From Mammal (parent)
dog.bark()        # From Dog (itself)
```

**Point out**: "Dog inherits from Mammal, which inherits from Animal. So Dog gets ALL methods from both!"

**Draw on board/show**:
```
Animal
  ↓
Mammal
  ↓
Dog
```

## [0:18-0:21] Practice Challenge (3 min)

**Challenge**: "Create a Shape hierarchy. Shape (parent) has area(). Rectangle and Circle (children) can calculate their own areas."

**Skeleton**:
```python
class Shape:
    def describe(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # TODO: return area
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # TODO: return area
        pass

# Test
rect = Rectangle(5, 3)
rect.describe()  # Should work (inherited)
print(rect.area())

circle = Circle(4)
circle.describe()  # Should work (inherited)
print(circle.area())
```

**Solution**:
```python
def area(self):  # In Rectangle
    return self.width * self.height

def area(self):  # In Circle
    return 3.14159 * self.radius ** 2
```

## [0:21-0:23] When to Use Inheritance (2 min)

**Say**: "Use inheritance when there's an IS-A relationship."

**Examples**:
- Dog IS-A Animal ✓
- Car IS-A Vehicle ✓
- Developer IS-A Employee ✓

**Anti-examples**:
- Car HAS-A Engine (composition, not inheritance!)
- Student HAS-A Backpack (not inheritance!)

**Rule of thumb**: "If you can say 'X is a Y' naturally, use inheritance. If you say 'X has a Y', don't use inheritance!"

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **Inheritance syntax**: `class Child(Parent):`
2. **Child inherits all**: Attributes and methods from parent
3. **Add specialization**: Child adds its own unique features
4. **Code reuse**: Write shared code once in parent
5. **IS-A relationship**: Use when child IS-A type of parent

**Benefits**:
- Less code duplication
- Easier to maintain
- Logical organization
- Extensible design

**Common Mistake**: "Don't forget to pass parent class name in parentheses! class Dog(Animal):, not class Dog:!"

**Closing**: "Inheritance is one of the pillars of OOP. Master it, and you can build complex, organized systems! Next, we'll learn how to override parent methods to customize behavior even more."
