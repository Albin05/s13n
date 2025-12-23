# Lecture Notes: Apply Inheritance

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.


---

<div align="center">

![Tree structure showing inheritance](https://images.unsplash.com/photo-1502101872923-d48509bff386?w=800&q=80)

*Inheritance allows classes to inherit properties from parent classes*

</div>

---
### Syntax

```python
class ParentClass:
    # Parent class code
    pass

class ChildClass(ParentClass):
    # Child class code
    pass
```

### Example: Animal Hierarchy

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

# Create objects
dog = Dog("Buddy")
dog.eat()   # Inherited from Animal
dog.bark()  # Defined in Dog

cat = Cat("Whiskers")
cat.eat()   # Inherited from Animal
cat.meow()  # Defined in Cat
```

## Multiple Levels of Inheritance

```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def feed_young(self):
        print("Feeding young...")

class Dog(Mammal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.breathe()     # From Animal
dog.feed_young()  # From Mammal
dog.bark()        # From Dog
```

## Real-World Example: Employees

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} is working")

class Developer(Employee):
    def code(self):
        print(f"{self.name} is coding")

class Manager(Employee):
    def manage(self):
        print(f"{self.name} is managing")

dev = Developer("Alice", 80000)
dev.work()  # From Employee
dev.code()  # From Developer

mgr = Manager("Bob", 90000)
mgr.work()    # From Employee
mgr.manage()  # From Manager
```

## Key Takeaways

1. **Inheritance syntax**: `class Child(Parent):`
2. **Code reuse**: Inherit parent functionality
3. **Specialization**: Add child-specific features
4. **Is-a relationship**: Dog IS-A Animal
5. **Multiple levels**: Grandparent → Parent → Child
