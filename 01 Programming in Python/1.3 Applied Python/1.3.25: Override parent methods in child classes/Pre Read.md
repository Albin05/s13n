# Pre-Read: Override Methods

## Method Overriding

Child classes can replace parent methods with their own version:

```python
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):  # Override!
        print("Woof!")

class Cat(Animal):
    def speak(self):  # Override!
        print("Meow!")

dog = Dog()
dog.speak()  # Woof! (uses Dog's version)

cat = Cat()
cat.speak()  # Meow! (uses Cat's version)
```

## Why Override Methods?

1. **Customize behavior**: Each child has specific implementation
2. **Polymorphism**: Same method, different behavior
3. **Flexibility**: Change parent behavior as needed

## Example: Shapes

```python
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):  # Override!
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Override!
        return 3.14 * self.radius ** 2

square = Square(5)
print(square.area())  # 25

circle = Circle(3)
print(circle.area())  # 28.26
```
