# Post-Class Quiz: Format Output with F-strings

## Q1: Valid f-string?
A) f"Hello {name}"
B) "Hello {name}"f
C) "f Hello {name}"

<details><summary>Answer</summary>
A - f goes before quotes
</details>

## Q2: What prints?
```python
x = 10
print(f"{x * 2}")
```
A) x * 2
B) 20
C) {20}

<details><summary>Answer</summary>
B - Expressions are evaluated
</details>

## Q3: Format to 2 decimals?
```python
pi = 3.14159
```
A) f"{pi:.2f}"
B) f"{pi:2f}"
C) f"{pi.2f}"

<details><summary>Answer</summary>
A - :.2f format specifier
</details>

## Q4: What's wrong?
```python
name = "Bob"
print("Hello {name}")
```
A) Missing f
B) Wrong brackets
C) Nothing

<details><summary>Answer</summary>
A - Need f before string
</details>

## Q5: Can you do math in {}?
A) Yes
B) No
C) Only addition

<details><summary>Answer</summary>
A - Any expression works
</details>
