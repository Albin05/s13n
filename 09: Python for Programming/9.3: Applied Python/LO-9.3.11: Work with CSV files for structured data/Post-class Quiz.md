# Post-Class Quiz: Work with CSV Files

## Q1: What does csv.reader() return when reading a CSV file?
A) A string containing the entire file
B) A dictionary for each row
C) An iterator that yields lists for each row
D) A tuple of all rows

<details><summary>Answer</summary>
C - csv.reader() returns an iterator that yields each row as a list of strings. Each element in the list represents a column value.
</details>

## Q2: What is the purpose of newline='' when opening a CSV file for writing?
A) It adds extra line breaks
B) It prevents extra blank lines on Windows
C) It removes all newlines from the data
D) It's only required on Mac systems

<details><summary>Answer</summary>
B - The newline='' parameter prevents extra blank lines from being inserted between rows on Windows systems. It ensures consistent behavior across platforms.
</details>

## Q3: What method is used to skip the header row when using csv.reader()?
A) reader.skip()
B) reader.next()
C) next(reader)
D) reader[1:]

<details><summary>Answer</summary>
C - Use next(reader) to skip the first row (header). The next() function moves the iterator forward by one position.
</details>

## Q4: How does csv.DictReader differ from csv.reader?
A) DictReader is faster
B) DictReader returns each row as a dictionary
C) DictReader can only read files with headers
D) DictReader requires fewer imports

<details><summary>Answer</summary>
B - csv.DictReader uses the first row as keys and returns each subsequent row as a dictionary, making it easier to access columns by name instead of index.
</details>

## Q5: What type are all values when read from a CSV file?
A) Integers for numbers, strings for text
B) The same type as they were when written
C) All values are strings
D) Python automatically detects the type

<details><summary>Answer</summary>
C - All values read from a CSV file are strings. You must explicitly convert them using int(), float(), etc., if you need numeric operations.
</details>
