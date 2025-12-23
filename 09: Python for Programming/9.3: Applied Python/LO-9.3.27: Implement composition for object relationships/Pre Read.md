# Pre-Read: Implement Composition

## What is Composition?

Composition means building complex objects from simpler objects ("has-a" relationship):

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        self.engine.start()

my_car = Car()
my_car.start()  # Engine started
```

## Composition vs Inheritance

- **Inheritance**: "is-a" relationship (Dog IS-A Animal)
- **Composition**: "has-a" relationship (Car HAS-A Engine)

## Example: Computer

```python
class CPU:
    def process(self):
        print("Processing...")

class RAM:
    def load(self):
        print("Loading into RAM...")

class Computer:
    def __init__(self):
        self.cpu = CPU()     # HAS-A CPU
        self.ram = RAM()     # HAS-A RAM
    
    def run_program(self):
        self.ram.load()
        self.cpu.process()

pc = Computer()
pc.run_program()
# Loading into RAM...
# Processing...
```
