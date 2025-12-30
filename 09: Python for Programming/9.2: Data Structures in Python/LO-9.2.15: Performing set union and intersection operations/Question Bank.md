## Question Bank: Performing Set Union and Intersection Operations

**Total Duration:** 21 minutes

---

### Q1: Common Interests Finder

**Duration:** 3 minutes | **Difficulty:** Low | **Category:** Implementation | **Type:** Coding

**Problem:** Create a program that finds common interests between users.

**Input:**
```
3
alice: python web ai
bob: web mobile ai design
charlie: python ai data
```

**Output:**
```
Alice & Bob: ai web
Alice & Charlie: ai python
Bob & Charlie: ai
All three: ai
```

**Constraints:** 1 ≤ users ≤ 10, 1 ≤ interests ≤ 20

---

### Q2: Subscriber List Merger

**Duration:** 3 minutes | **Difficulty:** Low | **Category:** Implementation | **Type:** Coding

**Problem:** Merge subscriber lists from multiple campaigns, removing duplicates.

**Input:**
```
3
campaign1: alice@ex.com bob@ex.com charlie@ex.com
campaign2: bob@ex.com diana@ex.com
campaign3: charlie@ex.com eve@ex.com frank@ex.com
```

**Output:**
```
Total unique subscribers: 6
Subscribers: alice@ex.com bob@ex.com charlie@ex.com diana@ex.com eve@ex.com frank@ex.com
```

**Constraints:** 1 ≤ campaigns ≤ 10, 1 ≤ emails per campaign ≤ 50

---

### Q3: Multi-Platform User Analysis

**Duration:** 5 minutes | **Difficulty:** Medium | **Category:** Implementation | **Type:** Coding

**Problem:** Analyze user activity across multiple platforms.

**Input:**
```
web: alice bob charlie diana
mobile: bob diana eve frank
desktop: alice bob frank george
```

**Output:**
```
Active on all platforms: bob
Active on at least 2 platforms: alice bob diana frank
Web only: charlie
Mobile only: eve
Desktop only: george
Total unique users: 7
```

**Constraints:** 2 ≤ platforms ≤ 5, 1 ≤ users per platform ≤ 100

---

### Q4: Product Feature Comparison

**Duration:** 5 minutes | **Difficulty:** Medium | **Category:** Application | **Type:** Coding

**Problem:** Compare features across products and find recommendations.

**Input:**
```
3
ProductA: wifi bluetooth nfc camera
ProductB: wifi bluetooth camera gps
ProductC: bluetooth camera gps radio
budget: ProductA ProductB
premium: ProductB ProductC
```

**Output:**
```
Common to all products: bluetooth camera
Budget models offer: bluetooth camera gps nfc wifi
Premium models offer: bluetooth camera gps radio wifi
Exclusive to budget: nfc
Exclusive to premium: radio
Best value (most features): ProductA ProductB (4 features each)
```

**Constraints:** 2 ≤ products ≤ 10, 1 ≤ features ≤ 20

---

### Q5: Course Enrollment System

**Duration:** 5 minutes | **Difficulty:** Medium | **Category:** Application | **Type:** Coding

**Problem:** Manage course enrollments and find overlaps.

**Input:**
```
4
Python101: alice bob charlie diana
WebDev: bob charlie eve
DataScience: alice bob frank
AI: bob diana frank
find_taking_multiple
find_course_pairs
recommend alice
```

**Output:**
```
Students taking multiple courses:
- alice: 2 courses (DataScience Python101)
- bob: 4 courses (AI DataScience Python101 WebDev)
- charlie: 2 courses (Python101 WebDev)
- diana: 2 courses (AI Python101)
- frank: 2 courses (AI DataScience)

Course pairs with shared students:
- Python101 & WebDev: 2 students (bob charlie)
- Python101 & DataScience: 2 students (alice bob)
- Python101 & AI: 2 students (bob diana)
- WebDev & DataScience: 1 student (bob)
- WebDev & AI: 1 student (bob)
- DataScience & AI: 2 students (bob frank)

Recommendations for alice (based on classmates):
- WebDev: 2 classmates also take this
- AI: 2 classmates also take this
```

**Constraints:** 2 ≤ courses ≤ 20, 1 ≤ students ≤ 100

---

## Metadata Summary

| Problem | Duration | Difficulty | Prerequisite LOs | Category       | Type   | Key Concepts |
| ------- | -------- | ---------- | ---------------- | -------------- | ------ | ------------ |
| Q1      | 3        | Low        | 9.2.10, 9.2.12   | Implementation | Coding | & operator   |
| Q2      | 3        | Low        | 9.2.10, 9.2.12   | Implementation | Coding | \| operator  |
| Q3      | 5        | Medium     | 9.2.10, 9.2.12   | Implementation | Coding | &, \|, -     |
| Q4      | 5        | Medium     | 9.2.10, 9.2.12   | Application    | Coding | complex ops  |
| Q5      | 5        | Medium     | 9.2.10, 9.2.12   | Application    | Coding | analysis     |
