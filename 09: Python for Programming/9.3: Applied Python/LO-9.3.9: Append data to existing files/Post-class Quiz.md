# Append to Files

## What does append mode do?
A) Overwrites the entire file
B) Adds content to the end of file
C) Reads the file

<details><summary>Answer</summary>
B - Adds content to the end without erasing existing data
</details>

## Which mode to append?
A) "w"
B) "r"
C) "a"

<details><summary>Answer</summary>
C - "a" is append mode
</details>

## What if file doesn't exist?
```python
with open("new.txt", "a") as f:
    f.write("Hello")
```
A) Error
B) File is created
C) Nothing happens

<details><summary>Answer</summary>
B - File is created if it doesn't exist
</details>

## What's the output?
```python
with open("test.txt", "w") as f:
    f.write("A\n")
with open("test.txt", "a") as f:
    f.write("B\n")
with open("test.txt", "a") as f:
    f.write("C\n")
```
A) Only C
B) A B C
C) C B A

<details><summary>Answer</summary>
B - A B C (write creates with A, then append adds B and C)
</details>

## Best use case for append?
A) Creating a new file
B) Log files
C) Overwriting old data

<details><summary>Answer</summary>
B - Log files are perfect for append mode (add entries over time)
</details>
