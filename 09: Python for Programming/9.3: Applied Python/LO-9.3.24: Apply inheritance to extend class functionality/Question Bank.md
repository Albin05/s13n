# Question Bank: Apply Inheritance

## Problem 1 (Easy)
Create a base class `Animal` with attributes `name` and `age`, and a method `make_sound()` that prints "Some generic sound". Then create a child class `Dog` that inherits from `Animal`. Test by creating a dog and calling `make_sound()`.

## Problem 2 (Easy)
Create a base class `Vehicle` with attributes `brand` and `model`. Create a child class `Car` that inherits from `Vehicle` and adds a new attribute `num_doors`. Create a car object with brand "Toyota", model "Camry", and 4 doors, then print all attributes.

## Problem 3 (Medium)
Create a base class `Employee` with attributes `name`, `id`, and `salary`. Add a method `get_details()` that returns formatted employee information. Create two child classes:
- `Manager`: adds attribute `department` and includes it in details
- `Developer`: adds attribute `programming_language` and includes it in details

Create one manager and one developer, and print their details.

## Problem 4 (Medium)
Create a base class `Shape` with a method `area()` that returns 0. Create child classes:
- `Circle`: has attribute `radius` and calculates area using πr²
- `Square`: has attribute `side` and calculates area using side²
- `Triangle`: has attributes `base` and `height` and calculates area using ½ × base × height

Create one of each shape and print their areas. Use `import math` for π.

## Problem 5 (Hard)
Create a class hierarchy for a school system:
- Base class `Person` with attributes `name`, `age`, and method `introduce()`
- `Student` inherits from `Person`, adds `student_id` and `grades` (list), and methods `add_grade(grade)` and `get_gpa()`
- `Teacher` inherits from `Person`, adds `employee_id`, `subject`, and `years_experience`
- `TeachingAssistant` inherits from `Student`, adds `subject_taught` and `hours_per_week`

Create instances of all three types and demonstrate their functionality, showing that `TeachingAssistant` has both student and teaching capabilities.
