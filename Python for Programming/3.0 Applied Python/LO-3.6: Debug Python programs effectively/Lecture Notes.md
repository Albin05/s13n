# Lecture Notes: Debug Python Programs

## Debug Python Programs

Using debugging techniques to find and fix bugs


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---
### Key Concepts

**Core principle**: print(), pdb, logging, try-except

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Print Debugging

```python
def calculate_total(prices):
    print(f"DEBUG: prices = {prices}")
    total = sum(prices)
    print(f"DEBUG: total = {total}")
    return total

calculate_total([10, 20, 30])
```

#### Example 2: Using pdb Debugger

```python
import pdb

def complex_function(x, y):
    pdb.set_trace()  # Debugger stops here
    result = x * 2
    result = result + y
    return result

# Commands in pdb:
# n - next line
# s - step into
# c - continue
# p variable - print variable
# q - quit
```

#### Example 3: Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def process_order(order_id):
    logging.debug(f"Processing order {order_id}")
    logging.info(f"Order {order_id} validated")
    logging.warning(f"Low stock for order {order_id}")
    logging.error(f"Payment failed for order {order_id}")
```

### Best Practices

1. Write clear, readable code
2. Handle errors appropriately
3. Follow Python conventions
4. Document your code
5. Test thoroughly

### Common Mistakes

1. Not handling edge cases
2. Overcomplicating simple tasks
3. Not following naming conventions

### Key Takeaways

1. Understanding the core concept is essential
2. Practice with real examples
3. Apply best practices
4. Avoid common pitfalls
5. Write clean, maintainable code
