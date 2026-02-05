## Question Bank: Create Objects from Class Definitions

---

### Q1: Creating Multiple Objects (3 minutes, Low Difficulty)

Create a `Book` class with `title`, `author`, and `pages`. Create 3 book objects and store them in a list. Print each book's title.

**Key Concepts:** Object instantiation, lists of objects

---

### Q2: Object Identity (3 minutes, Low Difficulty)

Create two `Point` objects with the same x and y values. Demonstrate that they are different objects using `is` and `==`. Then add an `__eq__` method to compare by values.

**Key Concepts:** Object identity vs equality, __eq__

---

### Q3: Factory Pattern (5 minutes, Medium Difficulty)

Create a `User` class with `name`, `email`, and `role`. Add a class method `from_string(s)` that creates a User from a comma-separated string like `"Alice,alice@mail.com,admin"`.

**Key Concepts:** Class methods, alternative constructors

---

### Q4: Object Collections (5 minutes, Medium Difficulty)

Create a `TaskList` class that manages `Task` objects (each with `title`, `done` status). Implement `add_task()`, `complete_task(title)`, `pending()` returning incomplete tasks, and `summary()`.

**Key Concepts:** Objects managing other objects

---

### Q5: Dynamic Object Creation (7 minutes, Medium-High Difficulty)

Write a function `create_objects(class_type, data_list)` that takes a class and a list of dictionaries, creating an instance for each dict using keyword unpacking. Test with a `Product` class.

**Key Concepts:** Dynamic instantiation, **kwargs unpacking

