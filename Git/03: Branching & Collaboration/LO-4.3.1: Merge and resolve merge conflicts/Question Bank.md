
### **Q1. What does a Git merge primarily represent in a collaborative workflow?**

A) Copying files from one branch to another
B) Deleting the source branch after development
C) Integrating approved changes and recording collaboration history
D) Automatically resolving all conflicts

**Correct Answer:** C

---

### **Q2. When does Git raise a merge conflict?**

A) Whenever a branch is merged into `main`
B) When two branches modify the same part of a file in incompatible ways
C) When a branch has more commits than `main`
D) When GitHub permissions are missing

**Correct Answer:** B

---

### **Q3. What do conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) indicate?**

A) Syntax errors in code
B) Uncommitted local changes
C) Different versions of conflicting code that require manual resolution
D) Corrupted repository state

**Correct Answer:** C

---



### **Q4. Why is merging considered a “decision point” rather than a development activity?**

(Answer in 3–4 lines.)

*Expected focus:*
Approval, review completion, acceptance into shared codebase, accountability.

---

### **Q5. After resolving a merge conflict, why is testing the application important before finalizing the merge?**

(Explain briefly.)

*Expected focus:*
Avoiding hidden bugs, validation after manual changes.

---





### **Q6. Merge Without Conflict (Basic Workflow)**

**Task:**
Perform the following steps and submit the GitHub repository link:

1. Create a new GitHub repository
2. Clone it locally
3. Add a file **app.txt** with some content
4. Commit and push to `main`
5. Create a branch **feature-a**
6. Modify **app.txt** by adding new lines (no overlapping changes)
7. Commit and push the branch
8. Raise a Pull Request from **feature-a → main**
9. Merge the Pull Request
10. Delete the feature branch after merge

> ⚠️ **Submission Instruction:**
> Submit the **GitHub repository link** clearly showing:
>
> * Branches
> * Commits
> * Pull Requests
> * Merge (with or without conflict)


---

### **Q7. Merge With Conflict (Conflict Resolution Workflow)**

**Task:**
Using the same repository or a new one:

1. Create a branch **feature-b**
2. Modify the **same lines** in **app.txt** that were modified in `main`
3. Commit and push the branch
4. Raise a Pull Request from **feature-b → main**
5. Encounter a merge conflict
6. Resolve the conflict **(CLI or GitHub UI)**
7. Ensure conflict markers are removed
8. Complete the merge
9. Verify the final content is correct

**Submission:**

* GitHub repository link
* Pull Request showing conflict and resolution

---

