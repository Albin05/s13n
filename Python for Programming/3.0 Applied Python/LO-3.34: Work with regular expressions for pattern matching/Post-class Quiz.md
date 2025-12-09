# Post-Class Quiz: Work with Regular Expressions

## Q1: What does \d match in a regex pattern?
A) Any letter
B) Any digit
C) Any whitespace

<details><summary>Answer</summary>
B) Any digit

Explanation: `\d` matches any digit character (0-9). Use `\D` to match non-digits.
</details>

## Q2: What's the difference between re.search() and re.match()?
A) No difference
B) search() finds anywhere in string, match() only from the beginning
C) match() is faster

<details><summary>Answer</summary>
B) search() finds anywhere in string, match() only from the beginning

Explanation: `re.match()` checks only at the start of the string, while `re.search()` scans through the entire string to find a match.
</details>

## Q3: What does the + quantifier mean?
A) 0 or more occurrences
B) 1 or more occurrences
C) Exactly 1 occurrence

<details><summary>Answer</summary>
B) 1 or more occurrences

Explanation: `+` means one or more occurrences. Use `*` for zero or more, and `?` for zero or one.
</details>

## Q4: Why use raw strings (r"") for regex patterns?
A) They're required by Python
B) They prevent backslashes from being interpreted as escape sequences
C) They make regex faster

<details><summary>Answer</summary>
B) They prevent backslashes from being interpreted as escape sequences

Explanation: Raw strings treat backslashes literally, which is important for regex patterns that use `\d`, `\w`, etc.
</details>

## Q5: What does this pattern match? r"^\d{3}-\d{4}$"
A) Any phone number
B) Format like 123-4567 (exactly)
C) Any number with a dash

<details><summary>Answer</summary>
B) Format like 123-4567 (exactly)

Explanation: `^` means start, `\d{3}` means exactly 3 digits, `-` is literal, `\d{4}` means exactly 4 digits, `$` means end. Matches format like "123-4567" only.
</details>
