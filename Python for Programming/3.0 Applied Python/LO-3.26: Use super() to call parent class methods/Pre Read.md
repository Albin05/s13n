# Pre-Read: Use the super() Function

## What is super()?

`super()` calls the parent class's methods from the child class:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed

my_dog = Dog("Buddy", "Labrador")
print(my_dog.name)   # Buddy (from Animal)
print(my_dog.breed)  # Labrador (from Dog)
```

## Why Use super()?

1. **Extend functionality**: Add to parent behavior
2. **Code reuse**: Use parent's logic
3. **Avoid repetition**: Don't duplicate parent code

## Example: Employee

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"I'm {self.name}, {self.age} years old")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call Person's __init__
        self.employee_id = employee_id
    
    def introduce(self):
        super().introduce()  # Call Person's introduce
        print(f"Employee ID: {self.employee_id}")

emp = Employee("Alice", 30, "E001")
emp.introduce()
# I'm Alice, 30 years old
# Employee ID: E001
```
