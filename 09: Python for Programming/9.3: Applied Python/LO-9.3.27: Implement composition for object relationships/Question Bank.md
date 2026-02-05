# Question Bank: Implement Composition

## Problem 1 (Easy)
Create a class `Engine` with attributes `horsepower` and `type`. Create a class `Car` that has an `Engine` object as an attribute (composition). The Car should have attributes `brand`, `model`, and `engine`. Test by creating a car with an engine and printing its details.

## Problem 2 (Easy)
Create a class `Address` with attributes `street`, `city`, and `zipcode`. Create a class `Person` that has an `Address` object as an attribute. Add a method `display_info()` that prints the person's name and full address. Test by creating a person with an address.

## Problem 3 (Medium)
Create a library system using composition:
- `Book` class with attributes `title`, `author`, `isbn`
- `Library` class that contains a list of `Book` objects
- Add methods to Library: `add_book(book)`, `remove_book(isbn)`, `find_book(title)`, `list_all_books()`

Create a library, add 3 books, find one by title, remove one by ISBN, and list all remaining books.

## Problem 4 (Medium)
Create a computer system using composition:
- `CPU` class with attributes `brand`, `speed`, `cores`
- `RAM` class with attributes `size`, `type`
- `Storage` class with attributes `capacity`, `type` (SSD/HDD)
- `Computer` class that contains CPU, RAM, and Storage objects
- Add method `get_specs()` that returns formatted specifications

Create a computer and display its full specifications.

## Problem 5 (Hard)
Create a university course enrollment system using composition:
- `Student` class with `name`, `student_id`, and list of enrolled courses
- `Professor` class with `name`, `employee_id`, and `department`
- `Course` class with `course_code`, `name`, `professor` (Professor object), and list of enrolled students (Student objects)
- `Department` class with `name` and list of courses

Implement methods:
- `Course.enroll_student(student)`: adds student to course and course to student
- `Course.get_enrollment_count()`: returns number of enrolled students
- `Department.add_course(course)`: adds course to department
- `Department.get_total_enrollment()`: returns total students across all courses

Create a department, add 2 courses with professors, enroll students in courses, and display enrollment statistics.
