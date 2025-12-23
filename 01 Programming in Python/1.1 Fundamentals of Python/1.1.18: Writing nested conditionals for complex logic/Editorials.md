# Editorials: Writing Nested Conditionals for Complex Logic

## Problem 1: Age Group Classifier (Easy)

### Solution
```python
age = 25

if age >= 0:
    if age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 60:
        print("Adult")
    else:
        print("Senior")
else:
    print("Invalid age")
```

**Output:**
```
Adult
```

### Explanation
- Outer `if` checks if age is valid (>= 0)
- Inner conditions classify age groups:
  - 0-12: Child
  - 13-19: Teenager
  - 20-59: Adult
  - 60+: Senior
- If age is negative, prints "Invalid age"
- Nested structure ensures validation before classification

---

## Problem 2: Grade Calculator with Pass/Fail (Easy)

### Solution
```python
score = 75

if score >= 0 and score <= 100:
    if score >= 50:
        if score >= 90:
            print("Grade: A (Pass)")
        elif score >= 80:
            print("Grade: B (Pass)")
        elif score >= 70:
            print("Grade: C (Pass)")
        else:
            print("Grade: D (Pass)")
    else:
        print("Grade: F (Fail)")
else:
    print("Invalid score")
```

**Output:**
```
Grade: C (Pass)
```

### Explanation
- First condition validates score is between 0 and 100
- Second level checks if student passed (>= 50)
- Third level assigns letter grade based on score ranges
- Nested structure ensures: validation → pass/fail → grade assignment
- Clear hierarchy prevents invalid grades

---

## Problem 3: Movie Ticket Pricing (Easy)

### Solution
```python
age = 15
is_student = True

if age < 18:
    if is_student:
        price = 5
    else:
        price = 7
else:
    if is_student:
        price = 8
    else:
        price = 10

print(f"Ticket price: ${price}")
```

**Output:**
```
Ticket price: $5
```

### Explanation
- Outer condition splits by age (under 18 vs 18+)
- Inner conditions check student status
- Pricing matrix:
  - Child student: $5
  - Child non-student: $7
  - Adult student: $8
  - Adult non-student: $10
- Nested structure handles all 4 combinations

---

## Problem 4: Login Validation (Medium)

### Solution
```python
username = "admin"
password = "secret123"

if username:
    if password:
        if username == "admin":
            if password == "secret123":
                print("Login successful")
            else:
                print("Incorrect password")
        else:
            print("Username not found")
    else:
        print("Password cannot be empty")
else:
    print("Username cannot be empty")
```

**Output:**
```
Login successful
```

### Explanation
- First level: Check if username is provided
- Second level: Check if password is provided
- Third level: Verify username matches
- Fourth level: Verify password matches
- Provides specific error messages for each failure point
- Validates inputs before checking credentials

---

## Problem 5: Restaurant Bill Calculator (Medium)

### Solution
```python
bill_amount = 120
num_people = 4
service_quality = "good"

if num_people > 0:
    if service_quality == "excellent":
        tip_percent = 0.20
    elif service_quality == "good":
        tip_percent = 0.15
    else:
        tip_percent = 0.10

    tip = bill_amount * tip_percent
    total = bill_amount + tip
    per_person = total / num_people

    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Per person: ${per_person:.2f}")
else:
    print("Number of people must be positive")
```

**Output:**
```
Tip: $18.00
Total: $138.00
Per person: $34.50
```

### Explanation
- Validates num_people is positive before calculations
- Nested conditions determine tip percentage based on service quality
- Calculates tip, total, and per-person amounts
- Provides formatted output with 2 decimal places
- Prevents division by zero

---

## Problem 6: Student Scholarship Eligibility (Medium)

### Solution
```python
gpa = 3.8
income = 45000
extracurricular = True

if gpa >= 3.0:
    if income < 50000:
        if extracurricular:
            scholarship = "Full scholarship"
        else:
            scholarship = "Partial scholarship"
    else:
        if extracurricular and gpa >= 3.5:
            scholarship = "Partial scholarship"
        else:
            scholarship = "Not eligible"
else:
    scholarship = "Not eligible"

print(scholarship)
```

**Output:**
```
Full scholarship
```

### Explanation
- Three criteria: GPA, income, extracurricular activities
- Scholarship rules:
  - GPA >= 3.0 AND income < 50k AND extracurricular → Full
  - GPA >= 3.0 AND income < 50k → Partial
  - GPA >= 3.5 AND income >= 50k AND extracurricular → Partial
  - Otherwise → Not eligible
- Nested structure implements complex eligibility logic

---

## Problem 7: Temperature and Weather Advisory (Medium)

### Solution
```python
temperature = 95
humidity = 70

if temperature > 90:
    if humidity > 60:
        print("Heat advisory: Dangerous conditions")
        print("Stay indoors and drink water")
    else:
        print("Hot weather: Exercise caution")
elif temperature < 32:
    if humidity > 50:
        print("Freezing rain possible")
    else:
        print("Cold weather: Dress warmly")
else:
    print("Pleasant weather")
```

**Output:**
```
Heat advisory: Dangerous conditions
Stay indoors and drink water
```

### Explanation
- Outer conditions classify temperature ranges
- Inner conditions check humidity for additional warnings
- Combines temperature and humidity for comprehensive advisories
- Provides specific safety recommendations
- Handles multiple weather scenarios

---

## Problem 8: Access Control System (Hard)

### Solution
```python
has_keycard = True
pin_correct = True
is_business_hours = False
is_authorized_personnel = True

if has_keycard:
    if pin_correct:
        if is_business_hours:
            print("Access granted")
        else:
            if is_authorized_personnel:
                print("Access granted (after-hours)")
            else:
                print("Access denied: Not authorized for after-hours")
    else:
        print("Access denied: Incorrect PIN")
else:
    print("Access denied: No keycard")
```

**Output:**
```
Access granted (after-hours)
```

### Explanation
- Four levels of security checks:
  1. Keycard present
  2. PIN correct
  3. Business hours or authorized personnel
- Access rules:
  - Business hours: keycard + PIN
  - After hours: keycard + PIN + authorized personnel
- Provides specific denial reasons for debugging
- Implements defense-in-depth security

---

## Problem 9: Parking Fee Calculator (Hard)

### Solution
```python
hours = 5
vehicle_type = "car"
is_weekend = True

if vehicle_type == "motorcycle":
    base_rate = 2
elif vehicle_type == "car":
    base_rate = 5
else:
    base_rate = 10  # truck/van

if hours > 0:
    if hours <= 2:
        fee = base_rate * hours
    else:
        if is_weekend:
            # Weekend discount: first 2 hours regular, rest 50% off
            fee = (base_rate * 2) + (base_rate * 0.5 * (hours - 2))
        else:
            # Weekday: first 2 hours regular, rest full rate
            fee = base_rate * hours

    print(f"Parking fee: ${fee:.2f}")
else:
    print("Invalid hours")
```

**Output:**
```
Parking fee: $17.50
```

### Explanation
- Calculation: (5 * 2) + (5 * 0.5 * 3) = 10 + 7.5 = $17.50
- Three factors: vehicle type, hours, weekend status
- Pricing logic:
  - First 2 hours: base rate
  - Additional hours: weekend gets 50% discount
- Base rates: motorcycle $2, car $5, truck $10
- Nested structure handles complex pricing rules

---

## Problem 10: Student Performance Report (Hard)

### Solution
```python
attendance = 85
assignment_avg = 78
exam_score = 82

if attendance >= 75:
    if assignment_avg >= 70:
        if exam_score >= 80:
            status = "Excellent"
            recommendation = "Keep up the great work!"
        elif exam_score >= 60:
            status = "Good"
            recommendation = "Focus on exam preparation"
        else:
            status = "At risk"
            recommendation = "Attend tutoring sessions"
    else:
        status = "At risk"
        recommendation = "Complete missing assignments"
else:
    status = "Critical"
    recommendation = "Meet with academic advisor immediately"

print(f"Status: {status}")
print(f"Recommendation: {recommendation}")
```

**Output:**
```
Status: Excellent
Recommendation: Keep up the great work!
```

### Explanation
- Three performance metrics: attendance, assignments, exam
- Status categories:
  - Excellent: all metrics good
  - Good: attendance and assignments good, exam needs work
  - At risk: one metric failing
  - Critical: poor attendance
- Provides personalized recommendations
- Nested structure prioritizes attendance first

---

## Problem 11: Online Shopping Discount (Hard)

### Solution
```python
is_member = True
cart_total = 150
num_items = 8
is_first_purchase = False

if is_member:
    if cart_total >= 100:
        if num_items >= 5:
            discount = 0.25  # 25% off
        else:
            discount = 0.15  # 15% off
    else:
        discount = 0.10  # 10% off
else:
    if is_first_purchase:
        discount = 0.10  # 10% off for first-time buyers
    else:
        discount = 0  # No discount

final_price = cart_total * (1 - discount)
savings = cart_total * discount

print(f"Original: ${cart_total:.2f}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Savings: ${savings:.2f}")
print(f"Final price: ${final_price:.2f}")
```

**Output:**
```
Original: $150.00
Discount: 25%
Savings: $37.50
Final price: $112.50
```

### Explanation
- Discount rules:
  - Member + $100+ + 5+ items → 25%
  - Member + $100+ → 15%
  - Member → 10%
  - Non-member first purchase → 10%
  - Non-member → 0%
- Nested structure implements tiered discount system
- Calculates and displays savings

---

## Problem 12: Loan Approval System (Very Hard)

### Solution
```python
credit_score = 720
annual_income = 65000
existing_debt = 15000
employment_years = 3

debt_to_income = existing_debt / annual_income

if credit_score >= 700:
    if debt_to_income < 0.3:
        if employment_years >= 2:
            loan_approved = True
            interest_rate = 3.5
        else:
            if annual_income >= 70000:
                loan_approved = True
                interest_rate = 4.0
            else:
                loan_approved = False
                reason = "Insufficient employment history"
    else:
        if credit_score >= 750 and annual_income >= 80000:
            loan_approved = True
            interest_rate = 4.5
        else:
            loan_approved = False
            reason = "Debt-to-income ratio too high"
else:
    loan_approved = False
    reason = "Credit score too low"

if loan_approved:
    print("Loan approved!")
    print(f"Interest rate: {interest_rate}%")
else:
    print("Loan denied")
    print(f"Reason: {reason}")
```

**Output:**
```
Loan approved!
Interest rate: 3.5%
```

### Explanation
- Complex approval criteria:
  - Credit score >= 700
  - Debt-to-income ratio < 30%
  - Employment >= 2 years OR income >= 70k
- Special case: high credit (750+) and income (80k+) can override debt ratio
- Interest rates based on risk level (3.5% - 4.5%)
- Provides specific denial reasons
- Nested structure implements multi-factor decision tree

---

## Problem 13: Game Difficulty Selector (Very Hard)

### Solution
```python
player_level = 15
wins = 45
losses = 20
average_score = 8500

if player_level >= 10:
    win_rate = wins / (wins + losses)

    if win_rate >= 0.7:
        if average_score >= 9000:
            difficulty = "Expert"
            bonus_xp = 1.5
        else:
            difficulty = "Advanced"
            bonus_xp = 1.3
    elif win_rate >= 0.5:
        if average_score >= 7500:
            difficulty = "Intermediate"
            bonus_xp = 1.2
        else:
            difficulty = "Beginner+"
            bonus_xp = 1.1
    else:
        difficulty = "Beginner"
        bonus_xp = 1.0
else:
    difficulty = "Tutorial"
    bonus_xp = 1.0

print(f"Recommended difficulty: {difficulty}")
print(f"XP bonus multiplier: {bonus_xp}x")
```

**Output:**
```
Recommended difficulty: Intermediate
XP bonus multiplier: 1.2x
```

### Explanation
- Calculation: win_rate = 45/(45+20) = 0.69 (69%)
- Three factors: level, win rate, average score
- Difficulty tiers:
  - Expert: level 10+, 70%+ wins, 9000+ score
  - Advanced: level 10+, 70%+ wins
  - Intermediate: level 10+, 50%+ wins, 7500+ score
  - Beginner+: level 10+, 50%+ wins
  - Beginner: level 10+, under 50% wins
  - Tutorial: under level 10
- Bonus XP encourages harder difficulties
- Nested structure ensures balanced matchmaking

---

## Problem 14: Insurance Premium Calculator (Very Hard)

### Solution
```python
age = 28
has_accidents = False
years_driving = 8
vehicle_value = 25000
has_security_system = True

# Base premium
base_premium = 800

if age < 25:
    age_multiplier = 1.5
elif age < 30:
    age_multiplier = 1.2
else:
    age_multiplier = 1.0

if has_accidents:
    if years_driving < 5:
        accident_multiplier = 1.8
    else:
        accident_multiplier = 1.4
else:
    if years_driving >= 5:
        accident_multiplier = 0.9
    else:
        accident_multiplier = 1.0

if vehicle_value > 30000:
    vehicle_multiplier = 1.3
elif vehicle_value > 20000:
    vehicle_multiplier = 1.1
else:
    vehicle_multiplier = 1.0

if has_security_system:
    security_discount = 0.1
else:
    security_discount = 0

premium = base_premium * age_multiplier * accident_multiplier * vehicle_multiplier
premium = premium * (1 - security_discount)

print(f"Annual premium: ${premium:.2f}")
```

**Output:**
```
Annual premium: $950.40
```

### Explanation
- Calculation: 800 * 1.2 * 0.9 * 1.1 * 0.9 = $950.40
- Five factors affecting premium:
  - Age: younger drivers pay more
  - Accidents: increases premium significantly
  - Driving experience: experienced drivers get discount
  - Vehicle value: expensive cars cost more to insure
  - Security system: 10% discount
- Nested structure calculates multipliers independently
- Final premium is product of all factors
- Real-world insurance pricing model

---

## Problem 15: University Admission Decision (Very Hard)

### Solution
```python
gpa = 3.7
sat_score = 1350
extracurricular_count = 4
essay_score = 8  # out of 10
recommendation_quality = "excellent"

admission_points = 0

if gpa >= 3.5:
    if sat_score >= 1400:
        admission_points += 30
    elif sat_score >= 1200:
        admission_points += 20
    else:
        admission_points += 10
else:
    if sat_score >= 1450:
        admission_points += 15
    else:
        admission_points += 5

if extracurricular_count >= 5:
    if essay_score >= 8:
        admission_points += 20
    else:
        admission_points += 15
elif extracurricular_count >= 3:
    if essay_score >= 7:
        admission_points += 15
    else:
        admission_points += 10
else:
    admission_points += 5

if recommendation_quality == "excellent":
    admission_points += 15
elif recommendation_quality == "good":
    admission_points += 10
else:
    admission_points += 5

if admission_points >= 60:
    decision = "Accepted"
elif admission_points >= 45:
    decision = "Waitlisted"
else:
    decision = "Rejected"

print(f"Admission points: {admission_points}")
print(f"Decision: {decision}")
```

**Output:**
```
Admission points: 50
Admission decision: Waitlisted
```

### Explanation
- Point breakdown:
  - GPA 3.7 + SAT 1350 → 20 points
  - 4 activities + essay 8 → 15 points
  - Excellent recommendation → 15 points
  - Total: 50 points → Waitlisted
- Holistic admissions criteria:
  - Academic performance (GPA + SAT)
  - Extracurricular involvement
  - Essay quality
  - Recommendations
- Decision thresholds:
  - 60+ points → Accepted
  - 45-59 points → Waitlisted
  - Under 45 → Rejected
- Nested structure allows compensation (weak GPA can be offset by strong SAT)
- Models real university admissions process

---

## Key Concepts Demonstrated

1. **Validation First**: Check inputs before processing
2. **Hierarchical Logic**: Outer conditions control inner logic
3. **Clear Error Messages**: Specific feedback for each path
4. **Complex Decision Trees**: Multiple factors influence outcome
5. **Defense in Depth**: Layer security checks
6. **Readable Indentation**: Proper formatting shows structure
7. **Avoid Deep Nesting**: Refactor if more than 3-4 levels
8. **Calculate Once**: Store intermediate values
9. **Consistent Patterns**: Similar problems use similar structures
10. **Real-World Models**: Practice with authentic scenarios

## Best Practices

- Keep nesting to 3-4 levels maximum for readability
- Use meaningful variable names
- Add comments for complex conditions
- Consider using `and`/`or` to flatten simple nested conditions
- Test all possible paths through nested logic
- Provide specific feedback for each outcome
- Validate inputs before complex calculations
