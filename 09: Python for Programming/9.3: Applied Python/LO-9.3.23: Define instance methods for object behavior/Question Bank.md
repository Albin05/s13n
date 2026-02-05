# Question Bank: Define Instance Methods

## Problem 1 (Easy)
Create a class `Rectangle` with attributes `length` and `width`. Define an instance method `area()` that calculates and returns the area of the rectangle.

Test your class by creating a rectangle with length 5 and width 3, and print its area.

## Problem 2 (Easy)
Create a class `BankAccount` with an attribute `balance` initialized to 0. Define instance methods `deposit(amount)` and `withdraw(amount)` that modify the balance accordingly. Create an account, deposit $100, withdraw $30, and print the final balance.

## Problem 3 (Medium)
Create a class `Student` with attributes `name` and `scores` (a list). Define the following instance methods:
- `add_score(score)`: adds a score to the list
- `get_average()`: returns the average of all scores
- `is_passing()`: returns `True` if average is 60 or above, `False` otherwise

Test with a student who has scores [75, 82, 68, 90].

## Problem 4 (Medium)
Create a class `ShoppingCart` with an attribute `items` (a list of dictionaries with keys "name" and "price"). Define these instance methods:
- `add_item(name, price)`: adds an item to the cart
- `remove_item(name)`: removes the first item with that name
- `get_total()`: returns the total price of all items
- `display_cart()`: prints all items with their prices

Test by adding 3 items, removing 1, and displaying the cart with total.

## Problem 5 (Hard)
Create a class `Book` with attributes `title`, `author`, `pages`, and `current_page` (starts at 0). Define these instance methods:
- `read_pages(num_pages)`: advances current_page by num_pages (not exceeding total pages)
- `bookmark()`: returns the current page number
- `progress_percentage()`: returns the percentage of the book read
- `reset()`: sets current_page back to 0
- `__str__()`: returns a formatted string with book info and reading progress

Create a book with 300 pages, read 100 pages, print progress, read 50 more, then print the book object.
