## Pre-Read: Set Membership Testing for Efficiency

**Duration:** 5 minutes

---

### What You'll Learn

How to use sets for **blazing fast** lookups. The `in` operator works with both lists and sets, but sets are dramatically faster.

---

### The Speed Difference

```python
# List: checks each element one by one → O(n)
my_list = [1, 2, 3, 4, 5]
3 in my_list  # checks 1, 2, 3 → found!

# Set: hash table lookup → O(1)
my_set = {1, 2, 3, 4, 5}
3 in my_set  # instant lookup → found!
```

For 5 elements, both are fast. For 1 million elements, the set is thousands of times faster.

---

### Real-World Example

```python
# Checking if a username is taken
taken_usernames = {'alice', 'bob', 'charlie'}

new_user = 'dave'
if new_user not in taken_usernames:
    print("Username available!")
```

---

### Also: Subset Checking

```python
required = {'Python', 'SQL'}
skills = {'Python', 'SQL', 'Git'}

if required.issubset(skills):
    print("You qualify!")  # True — has all required
```

---

### Try This

```python
vowels = set('aeiou')
word = 'hello'
for char in word:
    if char in vowels:
        print(f"{char} is a vowel")
```

What will print?
