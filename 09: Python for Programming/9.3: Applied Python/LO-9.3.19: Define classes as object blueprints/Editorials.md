## Editorials: Define Classes as Object Blueprints

---

### Q1 Solution

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

print(f"{car1.year} {car1.make} {car1.model}")  # 2022 Toyota Camry
print(f"{car2.year} {car2.make} {car2.model}")  # 2023 Honda Civic
```

---

### Q2 Solution

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(5, 3)
print(f"Area: {r.area()}")           # Area: 15
print(f"Perimeter: {r.perimeter()}")  # Perimeter: 16
```

---

### Q3 Solution

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

acc = BankAccount("Alice")
acc.deposit(100)
acc.withdraw(30)
print(acc.get_balance())  # 70
acc.withdraw(80)          # Insufficient funds
```

---

### Q4 Solution

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def highest(self):
        if not self.grades:
            return None
        return max(self.grades)

s = Student("Alice")
s.add_grade(85)
s.add_grade(92)
s.add_grade(78)
print(f"Average: {s.average()}")    # Average: 85.0
print(f"Highest: {s.highest()}")    # Highest: 92
```

---

### Q5 Solution

```python
import random

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title):
        self.songs.append(title)

    def remove_song(self, title):
        if title in self.songs:
            self.songs.remove(title)

    def shuffle(self):
        random.shuffle(self.songs)

    def __len__(self):
        return len(self.songs)

p = Playlist("Road Trip")
p.add_song("Song A")
p.add_song("Song B")
p.add_song("Song C")
print(len(p))          # 3
p.remove_song("Song B")
print(len(p))          # 2
p.shuffle()
print(p.songs)         # Randomized order
```

