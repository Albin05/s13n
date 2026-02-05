# Decision Making - Logic vs Experience

## Learning Objectives

By the end of this lesson, you will be able to:
- Distinguish between logic-based and experience-based decisions
- Understand why ML uses experience over logic
- Apply this concept to real problems

## Two Ways Humans Make Decisions

### 1. Using Logic and Reasoning

**Example: Buying a Mobile Phone**

Look at features logically:
- Camera quality: 48MP vs 12MP
- Battery life: 5000mAh vs 4000mAh
- Screen size: 6.5" vs 5.8"
- Storage: 128GB vs 64GB
- Price: $800 vs $600

Make decision using logical rules:
- If price < $700 AND battery > 4500mAh → Buy
- Otherwise → Don't buy

![](https://images.unsplash.com/photo-1575571536958-38aa1227786a?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb)

### 2. Using Experiences

**Same Example: Buying Mobile Phone**

Watch YouTube reviews:
- Reviewers test features
- Share their experiences
- Provide opinions

Gather information from others' experiences:
- "Battery lasts 2 days with normal use"
- "Camera struggles in low light"
- "Phone heats up during gaming"

Make decision based on collective experiences.

## Machine Learning = Experience-Based Decisions

Machine Learning is similar to our second method!

**Key Question:** How can computers have experiences? 🤔

**Answer:** They can't! So we feed them DATA.

Data = Computer's version of experience

## Example: Will Student Pass Exam?

### Logic-Based Approach
```
IF study_hours > 5 AND attendance > 80%:
    prediction = "PASS"
ELSE:
    prediction = "FAIL"
```

**Problem:** Rules may not capture reality!

### Experience-Based Approach (ML)

**Data (Past Students):**
```
Student 1: 6 hours study, 85% attendance → PASSED
Student 2: 3 hours study, 70% attendance → FAILED
Student 3: 4 hours study, 90% attendance → PASSED
Student 4: 5 hours study, 65% attendance → FAILED
...100 more students
```

**ML Model:** Learns patterns from this data
- Not simple rules
- Complex relationships
- Accounts for exceptions

## Why Experience Over Logic?

### Logic-Based Rules
**Pros:**
- Clear and explainable
- No data needed
- Fast to create

**Cons:**
- Hard to define complex rules
- Miss edge cases
- Don't adapt to new patterns

### Experience-Based (ML)
**Pros:**
- Handles complexity
- Adapts to patterns in data
- Works when rules unclear

**Cons:**
- Needs lots of data
- Less explainable
- Can't work without data

## Real-World Example: Email Spam

**Logic Approach:**
```python
if "FREE" in email or "CLICK HERE" in email:
    spam = True
```
**Problem:** Spammers adapt!

**ML Approach:**
- Learn from 1 million emails
- Discover subtle patterns
- Adapt as spam evolves

## Summary

1. Two decision types: Logic vs Experience
2. ML uses experience-based decisions
3. Data replaces human experience for computers
4. ML better for complex, pattern-based problems
5. Logic better for clear, rule-based problems

## Practice

1. Give 2 examples where logic-based rules work best
2. Give 2 examples where experience-based ML works best
3. Why can't computers have "experiences" like humans?
4. What replaces experience for machines?
