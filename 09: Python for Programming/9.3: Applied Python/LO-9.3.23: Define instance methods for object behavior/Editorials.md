# Editorials: Define Instance Methods

## Problem 1
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Test the class
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")
```

### Explanation
- Instance methods are functions defined inside a class that operate on instance data
- The `area()` method uses `self` to access the instance's `length` and `width` attributes
- `self` is automatically passed as the first parameter when calling instance methods
- We call the method using `rect.area()`, which returns the calculated area
- Instance methods can access and modify the object's state through `self`

## Problem 2
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

# Test the class
account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(f"Final balance: ${account.balance}")
```

### Explanation
- Instance methods can modify the object's state through `self`
- Both `deposit()` and `withdraw()` take a parameter and use it to update `self.balance`
- Methods can perform actions (printing) and modify attributes
- The balance persists between method calls because it's stored in the instance
- This demonstrates encapsulating behavior with data in a single class

## Problem 3
```python
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def is_passing(self):
        return self.get_average() >= 60

# Test the class
student = Student("Alice", [75, 82, 68, 90])
print(f"Average: {student.get_average():.2f}")
print(f"Passing: {student.is_passing()}")

student.add_score(55)
print(f"New average: {student.get_average():.2f}")
print(f"Still passing: {student.is_passing()}")
```

### Explanation
- Instance methods can call other instance methods using `self.method_name()`
- The `is_passing()` method calls `self.get_average()` to avoid code duplication
- Methods can return different data types (number, boolean)
- The `add_score()` method modifies the mutable list attribute
- Edge case handling: `get_average()` checks for empty list to avoid division by zero
- This demonstrates how methods work together to provide functionality

## Problem 4
```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        print(f"Added {name} (${price}) to cart")

    def remove_item(self, name):
        for i, item in enumerate(self.items):
            if item["name"] == name:
                self.items.pop(i)
                print(f"Removed {name} from cart")
                return
        print(f"{name} not found in cart")

    def get_total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    def display_cart(self):
        print("\n=== Shopping Cart ===")
        if len(self.items) == 0:
            print("Cart is empty")
        else:
            for item in self.items:
                print(f"- {item['name']}: ${item['price']}")
            print(f"\nTotal: ${self.get_total()}")

# Test the class
cart = ShoppingCart()
cart.add_item("Laptop", 999)
cart.add_item("Mouse", 25)
cart.add_item("Keyboard", 75)
cart.remove_item("Mouse")
cart.display_cart()
```

### Explanation
- Methods can work with complex data structures (lists of dictionaries)
- `add_item()` creates a dictionary and appends it to the list
- `remove_item()` iterates through the list to find and remove an item
- `get_total()` demonstrates accumulation pattern within a method
- `display_cart()` uses another method (`get_total()`) for calculation
- Methods provide a clean interface for complex operations
- The `return` statement in `remove_item()` exits early after finding the item

## Problem 5
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read_pages(self, num_pages):
        self.current_page += num_pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        print(f"Read {num_pages} pages. Now on page {self.current_page}")

    def bookmark(self):
        return self.current_page

    def progress_percentage(self):
        if self.pages == 0:
            return 0
        return (self.current_page / self.pages) * 100

    def reset(self):
        self.current_page = 0
        print("Book reset to beginning")

    def __str__(self):
        progress = self.progress_percentage()
        return (f"'{self.title}' by {self.author}\n"
                f"Pages: {self.current_page}/{self.pages} "
                f"({progress:.1f}% complete)")

# Test the class
book = Book("Python Mastery", "John Doe", 300)
book.read_pages(100)
print(f"Progress: {book.progress_percentage():.1f}%")

book.read_pages(50)
print(f"Bookmark at page: {book.bookmark()}")

print("\n" + str(book))

# Try to read beyond the end
book.read_pages(200)
print(f"Final page: {book.current_page}")
```

### Explanation
- The `__str__()` method is a special method that defines string representation
- It's called automatically when using `print()` or `str()` on the object
- `read_pages()` includes boundary checking to prevent exceeding total pages
- Methods can perform calculations and return formatted results
- `progress_percentage()` uses division and multiplication for percentage calculation
- Multiple methods work together to create a cohesive object behavior
- The class maintains state (current_page) that persists across method calls

**Key Concepts**:
1. **Instance methods** operate on object data through `self`
2. **Method chaining**: methods can call other methods using `self`
3. **State management**: methods can read and modify object attributes
4. **Special methods** like `__str__()` customize object behavior
5. **Return values**: methods can return data for external use
6. **Side effects**: methods can print, modify state, or perform other actions
