# Question Bank: Writing Nested Conditionals for Complex Logic

## Problem 1: Age Group Classifier (Easy)

Write a program that classifies a person's age into categories. If age is valid (>= 0), classify as:
- Child: 0-12
- Teenager: 13-19
- Adult: 20-59
- Senior: 60+

If age is negative, print "Invalid age".

Test with age = 25.

**Expected Output:**
```
Adult
```

**Hint:** Use outer if for validation, inner elif chain for classification.

---

## Problem 2: Grade Calculator with Pass/Fail (Easy)

Write a program that assigns letter grades and pass/fail status. If score is valid (0-100):
- A: 90-100 (Pass)
- B: 80-89 (Pass)
- C: 70-79 (Pass)
- D: 60-69 (Pass)
- F: Below 60 (Fail)

If score is invalid, print "Invalid score".

Test with score = 85.

**Expected Output:**
```
Grade: B (Pass)
```

**Hint:** Outer if validates range, first inner if checks pass/fail, second inner if assigns grade.

---

## Problem 3: Movie Ticket Pricing (Easy)

Calculate movie ticket price based on age and student status:
- Child (under 18) student: $5
- Child non-student: $7
- Adult (18+) student: $8
- Adult non-student: $10

Test with age = 15, is_student = True.

**Expected Output:**
```
Ticket price: $5
```

**Hint:** Outer if checks age, inner if checks student status for each age group.

---

## Problem 4: Login Validation (Medium)

Write a login system that checks:
1. Is username provided?
2. Is password provided?
3. Does username match "admin"?
4. Does password match "secret123"?

Provide specific error messages for each failure point.

Test with username = "admin", password = "secret123".

**Expected Output:**
```
Login successful
```

**Hint:** Use 4 levels of nesting, one for each check. Provide specific error in each else.

---

## Problem 5: Restaurant Bill Calculator (Medium)

Calculate tip and total for a restaurant bill:
- Validate num_people > 0
- Determine tip based on service quality:
  - "excellent": 20%
  - "good": 15%
  - "poor": 10%
- Calculate total and per-person amount

Test with bill_amount = 120, num_people = 4, service_quality = "good".

**Expected Output:**
```
Tip: $18.00
Total: $138.00
Per person: $34.50
```

**Hint:** Outer if validates people count, inner elif chain determines tip percentage.

---

## Problem 6: Student Scholarship Eligibility (Medium)

Determine scholarship based on criteria:
- If GPA >= 3.0:
  - If income < $50k:
    - If has extracurriculars → Full scholarship
    - Else → Partial scholarship
  - Else:
    - If has extracurriculars AND GPA >= 3.5 → Partial scholarship
    - Else → Not eligible
- If GPA < 3.0 → Not eligible

Test with gpa = 3.8, income = 45000, extracurricular = True.

**Expected Output:**
```
Full scholarship
```

**Hint:** Three levels of nesting for three criteria.

---

## Problem 7: Temperature and Weather Advisory (Medium)

Issue weather advisories based on temperature and humidity:
- If temp > 90:
  - If humidity > 60 → "Heat advisory: Dangerous conditions"
  - Else → "Hot weather: Exercise caution"
- If temp < 32:
  - If humidity > 50 → "Freezing rain possible"
  - Else → "Cold weather: Dress warmly"
- Else → "Pleasant weather"

Test with temperature = 95, humidity = 70.

**Expected Output:**
```
Heat advisory: Dangerous conditions
Stay indoors and drink water
```

**Hint:** Use elif for temperature ranges, nested if for humidity checks.

---

## Problem 8: Access Control System (Hard)

Implement a 4-level security system:
- Has keycard?
  - PIN correct?
    - Is business hours?
      - Grant access
    - Else:
      - Is authorized personnel?
        - Grant access (after-hours)
      - Else:
        - Deny: Not authorized for after-hours

Provide specific denial reasons.

Test with has_keycard = True, pin_correct = True, is_business_hours = False, is_authorized_personnel = True.

**Expected Output:**
```
Access granted (after-hours)
```

**Hint:** Four levels of nesting with specific messages at each failure point.

---

## Problem 9: Parking Fee Calculator (Hard)

Calculate parking fee based on:
- Vehicle type: motorcycle ($2/hr), car ($5/hr), truck ($10/hr)
- Hours parked
- Weekend discount: After 2 hours, remaining hours are 50% off on weekends

Formula for weekend: (base_rate × 2) + (base_rate × 0.5 × (hours - 2))

Test with hours = 5, vehicle_type = "car", is_weekend = True.

**Expected Output:**
```
Parking fee: $17.50
```

**Hint:** Set base rate first, then calculate fee using nested if for hours and weekend.

---

## Problem 10: Student Performance Report (Hard)

Generate performance status and recommendation:
- If attendance >= 75%:
  - If assignment_avg >= 70%:
    - If exam_score >= 80 → "Excellent" / "Keep up the great work!"
    - Elif exam_score >= 60 → "Good" / "Focus on exam preparation"
    - Else → "At risk" / "Attend tutoring sessions"
  - Else → "At risk" / "Complete missing assignments"
- Else → "Critical" / "Meet with academic advisor immediately"

Test with attendance = 85, assignment_avg = 78, exam_score = 82.

**Expected Output:**
```
Status: Excellent
Recommendation: Keep up the great work!
```

**Hint:** Three levels for three metrics, with different recommendations at each level.

---

## Problem 11: Online Shopping Discount (Hard)

Calculate discount based on membership and cart:
- If member:
  - If cart_total >= $100:
    - If num_items >= 5 → 25% off
    - Else → 15% off
  - Else → 10% off
- Else:
  - If first_purchase → 10% off
  - Else → No discount

Calculate final price and savings.

Test with is_member = True, cart_total = 150, num_items = 8, is_first_purchase = False.

**Expected Output:**
```
Original: $150.00
Discount: 25%
Savings: $37.50
Final price: $112.50
```

**Hint:** Nested structure for tiered discounts, calculate savings at end.

---

## Problem 12: Loan Approval System (Very Hard)

Approve loan based on multiple criteria:
- If credit_score >= 700:
  - If debt_to_income < 0.3:
    - If employment_years >= 2 → Approve at 3.5%
    - Else:
      - If annual_income >= $70k → Approve at 4.0%
      - Else → Deny: "Insufficient employment history"
  - Else:
    - If credit_score >= 750 AND income >= $80k → Approve at 4.5%
    - Else → Deny: "Debt-to-income ratio too high"
- Else → Deny: "Credit score too low"

Test with credit_score = 720, annual_income = 65000, existing_debt = 15000, employment_years = 3.

**Expected Output:**
```
Loan approved!
Interest rate: 3.5%
```

**Hint:** Calculate debt_to_income first, then use multi-level nesting with specific denial reasons.

---

## Problem 13: Game Difficulty Selector (Very Hard)

Recommend game difficulty based on player stats:
- If player_level >= 10:
  - Calculate win_rate = wins / (wins + losses)
  - If win_rate >= 0.7:
    - If average_score >= 9000 → "Expert" (1.5x XP)
    - Else → "Advanced" (1.3x XP)
  - Elif win_rate >= 0.5:
    - If average_score >= 7500 → "Intermediate" (1.2x XP)
    - Else → "Beginner+" (1.1x XP)
  - Else → "Beginner" (1.0x XP)
- Else → "Tutorial" (1.0x XP)

Test with player_level = 15, wins = 45, losses = 20, average_score = 8500.

**Expected Output:**
```
Recommended difficulty: Intermediate
XP bonus multiplier: 1.2x
```

**Hint:** Calculate win_rate first, use nested structure for difficulty tiers.

---

## Problem 14: Insurance Premium Calculator (Very Hard)

Calculate annual insurance premium with multiple factors:
- Age multiplier:
  - Under 25: 1.5x
  - 25-29: 1.2x
  - 30+: 1.0x
- Accident history:
  - If has_accidents:
    - If years_driving < 5 → 1.8x
    - Else → 1.4x
  - Else:
    - If years_driving >= 5 → 0.9x
    - Else → 1.0x
- Vehicle value:
  - Over $30k: 1.3x
  - $20k-$30k: 1.1x
  - Under $20k: 1.0x
- Security system: -10% discount

Base premium: $800
Formula: base × age_mult × accident_mult × vehicle_mult × (1 - security_discount)

Test with age = 28, has_accidents = False, years_driving = 8, vehicle_value = 25000, has_security_system = True.

**Expected Output:**
```
Annual premium: $950.40
```

**Hint:** Calculate each multiplier independently using nested ifs, then combine at end.

---

## Problem 15: University Admission Decision (Very Hard)

Calculate admission points and make decision:

**GPA and SAT:**
- If GPA >= 3.5:
  - SAT >= 1400 → 30 points
  - SAT >= 1200 → 20 points
  - Else → 10 points
- Else:
  - SAT >= 1450 → 15 points
  - Else → 5 points

**Extracurriculars and Essay:**
- If activities >= 5:
  - Essay >= 8 → 20 points
  - Else → 15 points
- Elif activities >= 3:
  - Essay >= 7 → 15 points
  - Else → 10 points
- Else → 5 points

**Recommendation:**
- "excellent" → 15 points
- "good" → 10 points
- Else → 5 points

**Decision:**
- 60+ points → Accepted
- 45-59 points → Waitlisted
- Below 45 → Rejected

Test with gpa = 3.7, sat_score = 1350, extracurricular_count = 4, essay_score = 8, recommendation_quality = "excellent".

**Expected Output:**
```
Admission points: 50
Decision: Waitlisted
```

**Hint:** Calculate points for each category using nested ifs, sum points, then decide based on total.

---

## Problem 16: Shipping Cost Calculator (Hard)

Calculate shipping cost based on:
- Weight tiers with base costs
- Destination zones (domestic/international)
- Express shipping option

Rules:
- If weight <= 5kg:
  - If domestic:
    - If express → $15
    - Else → $8
  - Else (international):
    - If express → $30
    - Else → $20
- Elif weight <= 20kg:
  - If domestic:
    - If express → $25
    - Else → $15
  - Else:
    - If express → $50
    - Else → $35
- Else:
  - If domestic:
    - If express → $40
    - Else → $25
  - Else:
    - If express → $80
    - Else → $50

Test with weight = 3, is_domestic = True, is_express = False.

**Expected Output:**
```
Shipping cost: $8
```

**Hint:** Three-level nesting: weight tier, then destination, then shipping speed.

---

## Problem 17: Job Application Screener (Hard)

Screen job applicants based on qualifications:
- If has_degree:
  - If years_experience >= 5:
    - If has_certifications → "Interview: Senior Position"
    - Else → "Interview: Mid-Level Position"
  - Elif years_experience >= 2:
    - If has_certifications → "Interview: Mid-Level Position"
    - Else → "Interview: Entry-Level Position"
  - Else:
    - If has_certifications → "Interview: Entry-Level Position"
    - Else → "Application under review"
- Else:
  - If years_experience >= 10:
    - If has_certifications → "Interview: Mid-Level Position"
    - Else → "Application under review"
  - Else → "Not qualified"

Test with has_degree = True, years_experience = 6, has_certifications = True.

**Expected Output:**
```
Interview: Senior Position
```

**Hint:** First check degree, then experience tiers, then certifications.

---

## Problem 18: Tax Bracket Calculator (Hard)

Calculate income tax based on complex brackets:
- If income <= $10,000 → 0% tax
- Elif income <= $40,000:
  - If has_dependents:
    - If num_dependents >= 3 → 5% tax
    - Else → 8% tax
  - Else → 10% tax
- Elif income <= $85,000:
  - If has_dependents:
    - If num_dependents >= 3 → 12% tax
    - Else → 15% tax
  - Else → 18% tax
- Else (income > $85,000):
  - If has_dependents:
    - If num_dependents >= 3 → 20% tax
    - Else → 24% tax
  - Else → 28% tax

Calculate tax amount.

Test with income = 50000, has_dependents = True, num_dependents = 2.

**Expected Output:**
```
Tax: $7500.00 (15%)
```

**Hint:** Nested structure for income brackets, then dependent status, then number of dependents.

---

## Problem 19: Loyalty Rewards Calculator (Medium)

Calculate loyalty points earned:
- If member_years >= 5:
  - If purchase_amount >= $200:
    - If is_birthday_month → 3x points
    - Else → 2x points
  - Else → 1.5x points
- Elif member_years >= 2:
  - If purchase_amount >= $200 → 1.5x points
  - Else → 1.2x points
- Else:
  - If purchase_amount >= $200 → 1.2x points
  - Else → 1.0x points

Base: 1 point per dollar
Formula: purchase_amount × multiplier

Test with member_years = 6, purchase_amount = 250, is_birthday_month = False.

**Expected Output:**
```
Points earned: 500
```

**Hint:** Check membership tenure, then purchase amount, then special bonuses.

---

## Problem 20: Workout Intensity Recommender (Medium)

Recommend workout intensity based on fitness level and health:
- If fitness_level == "beginner":
  - If has_health_issues:
    - If age >= 50 → "Light intensity, 20 minutes"
    - Else → "Light intensity, 30 minutes"
  - Else:
    - If age >= 50 → "Moderate intensity, 30 minutes"
    - Else → "Moderate intensity, 45 minutes"
- Elif fitness_level == "intermediate":
  - If has_health_issues → "Moderate intensity, 30 minutes"
  - Else:
    - If age >= 50 → "Moderate intensity, 45 minutes"
    - Else → "High intensity, 45 minutes"
- Else (advanced):
  - If has_health_issues → "Moderate intensity, 45 minutes"
  - Else → "High intensity, 60 minutes"

Test with fitness_level = "beginner", has_health_issues = False, age = 35.

**Expected Output:**
```
Recommendation: Moderate intensity, 45 minutes
```

**Hint:** First check fitness level, then health status, then age for modifications.
