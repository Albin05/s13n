# Pre-Read: Implement String Data Types

## What are Strings?

**Strings** are text data - any characters in quotes.

```python
name = "Alice"
message = 'Hello, World!'
email = "user@example.com"
```

Single `'` or double `"` quotes both work!

### Why Strings Are Different

You've learned numbers (int, float). Why do we need a separate type for text?

**Computers only understand numbers** (0s and 1s). When you write "Hello":
- The computer doesn't see letters
- It sees numbers: [72, 101, 108, 108, 111]
- Each letter has a number code
- Python handles this translation automatically!

This is why you can't do `"5" + 5` - one is the text character "5", the other is the number 5. They're stored completely differently.

### Simple Analogy

Think of a string like a **necklace**:
- Each character is a bead
- The beads are strung together in order
- "Hello" is 5 beads: H-e-l-l-o
- You can't have half a bead (can't split a character)
- The order matters: "Hello" ≠ "olleH"

### Why Order Matters

Unlike numbers (5 + 3 = 3 + 5), strings care about order:
- "cat" ≠ "act"
- "hello" ≠ "olleh"

This is because strings represent **language**, and language has grammar and meaning tied to order.

## String Operations

### Concatenation (Combining)
```python
first = "Hello"
second = "World"
combined = first + " " + second
print(combined)  # "Hello World"
```

### Repetition
```python
laugh = "ha" * 3
print(laugh)  # "hahaha"
```

### Length
```python
name = "Alice"
print(len(name))  # 5
```

## Special Characters
```python
# Use opposite quotes inside
message = "He said, 'Hello!'"
message = 'She said, "Hi!"'

# Or escape quotes
message = "He said, \"Hello!\""
```

## When to Use Strings
✅ Names, messages, text, emails, URLs, addresses

## Try It
```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)
```
