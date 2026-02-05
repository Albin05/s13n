# Question Bank: Work with CSV Files

## Problem 1 (Easy)
Write a program that reads a CSV file named `products.csv` containing product names and prices, and prints each product with its price. The CSV file has the format:
```
product,price
Laptop,999
Mouse,25
Keyboard,75
```

## Problem 2 (Easy)
Create a CSV file named `students.csv` with columns `name`, `age`, and `grade`. Write data for at least 3 students using `csv.writer`.

## Problem 3 (Medium)
Read a CSV file named `scores.csv` containing student names and test scores:
```
name,score
Alice,85
Bob,92
Charlie,78
Diana,95
```
Calculate and print the average score of all students.

## Problem 4 (Medium)
You have a list of dictionaries representing employees:
```python
employees = [
    {"name": "Alice", "department": "Engineering", "salary": 80000},
    {"name": "Bob", "department": "Marketing", "salary": 65000},
    {"name": "Charlie", "department": "Engineering", "salary": 75000}
]
```
Write this data to a CSV file named `employees.csv` using `csv.DictWriter`.

## Problem 5 (Hard)
Read a CSV file named `sales.csv` with columns `product`, `quantity`, and `price`:
```
product,quantity,price
Laptop,5,999
Mouse,50,25
Keyboard,20,75
Monitor,10,300
```
Calculate and print:
1. The total revenue for each product (quantity × price)
2. The product that generated the most revenue
3. The total revenue from all products

**Hint**: Use `csv.DictReader` to read the file and keep track of the maximum revenue.
