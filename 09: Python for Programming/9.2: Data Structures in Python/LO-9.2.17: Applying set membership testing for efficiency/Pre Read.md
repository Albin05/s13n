## Pre-Read: Set Membership Testing for Efficiency

**Duration:** 5 minutes

---

## What Is Membership Testing?

Membership testing is asking **"Is this item in the collection?"** - and sets answer this question **1000x faster** than lists! This is where sets become **superpowers**.

### Simple Analogy

**List membership like searching a pile of papers**:
- **Question**: "Is invoice #5427 in this stack?"
- **Method**: Pick up paper 1... check... nope. Paper 2... check... nope. Paper 3...
- **1000 papers**: Might need to check all 1000!
- **Slow**: Like searching without organization

**Set membership like file cabinet with labels**:
- **Question**: "Is invoice #5427 here?"
- **Method**: Go directly to drawer #5427 → instant answer!
- **1000 drawers**: Still instant!
- **Fast**: Organized system = direct access

### The Speed Difference (Mind-Blowing!)

**Scenario**: Check if 1000 items are valid against a list of 10,000 approved items.

**Using list** (old way):
```python
approved_list = [... 10,000 items ...]  # list
# Each check: ~5,000 comparisons (average)
# 1000 checks: 5,000,000 operations!
# Time: Several seconds
```

**Using set** (smart way):
```python
approved_set = {... 10,000 items ...}  # set
# Each check: 1 lookup
# 1000 checks: 1,000 operations!
# Time: Milliseconds!
```

**5000x faster!** Same code, different data structure!

### When This Matters

**Rule of thumb**: If checking membership **more than a few times**, convert to set first!

**Example - Spam filter**:
```python
# BAD - checking list repeatedly (slow!)
spam_words_list = ['viagra', 'lottery', 'winner', ...]  # 1000s of words
for email in inbox:  # 1000s of emails
    for word in email.split():
        if word in spam_words_list:  # O(n) each time!
            # This gets SUPER slow!

# GOOD - convert to set once (fast!)
spam_words_set = set(spam_words_list)  # one-time conversion
for email in inbox:
    for word in email.split():
        if word in spam_words_set:  # O(1) each time!
            # Lightning fast!
```

**Conversion cost**: O(n) once
**Benefit**: O(1) for every subsequent check
**Breakeven**: After just 2-3 checks, you're already winning!

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
