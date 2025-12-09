# Pre-Read: Extract List Portions with Slicing

## Slicing Syntax

```python
list[start:stop]
```

Extracts items from `start` to `stop-1`.

## Examples

```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[1:4]  # [1, 2, 3]
numbers[:3]   # [0, 1, 2] (first 3)
numbers[3:]   # [3, 4, 5] (from index 3 to end)
```

## Reverse a List

```python
numbers[::-1]  # [5, 4, 3, 2, 1, 0]
```
