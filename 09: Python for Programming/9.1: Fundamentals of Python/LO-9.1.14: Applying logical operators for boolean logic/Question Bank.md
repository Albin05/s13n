### **1. Write a program that:**

1. Takes user's age and whether they have a driver's license (yes/no)
2. Determines if they can drive (age >= 18 AND has license)
3. Prints the result

Example:
```
Enter your age: 20
Do you have a license? (yes/no): yes
Can drive: True
```

---

### **2. Write a program that checks if it's a good day to go outside:**

1. Take inputs for is_weekend (yes/no) and is_sunny (yes/no)
2. Good day if it's weekend OR sunny
3. Print the result

Example:
```
Is it weekend? (yes/no): no
Is it sunny? (yes/no): yes
Good day to go outside: True
```

---

### **3. Write a program that checks if a student passed a course:**

1. Take exam score (0-100) and whether assignment was submitted (yes/no)
2. Student passes if score >= 60 AND assignment submitted
3. Also check if student got excellent grade (score >= 90 AND assignment submitted)
4. Print both results

Example:
```
Enter exam score: 85
Was assignment submitted? (yes/no): yes
Passed: True
Excellent: False
```

---

### **4. Write a login validator that checks:**

1. Username is not empty (length > 0)
2. Password is at least 8 characters
3. Both conditions must be true to login
4. Print if login is valid

Example:
```
Enter username: alice
Enter password: secure123
Login valid: True
```

---

### **5. Write a program that determines if someone can watch a movie:**

1. Take age, has parent with them (yes/no), and movie rating (G/PG/PG13/R)
2. Rules:
   - G: Anyone can watch
   - PG: Anyone can watch
   - PG13: Age >= 13 OR has parent
   - R: Age >= 17 OR (age >= 13 AND has parent)
3. Print if they can watch

Example:
```
Enter your age: 15
Is parent with you? (yes/no): no
Movie rating (G/PG/PG13/R): PG13
Can watch movie: True
```

Hint: Use multiple `and`/`or` combinations!

---

