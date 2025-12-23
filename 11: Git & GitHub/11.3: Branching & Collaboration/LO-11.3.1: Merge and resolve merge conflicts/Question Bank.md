### **Q1. Why is merging considered a “decision point” rather than a development activity?**

(Answer in 3–4 lines.)

_Expected focus:_
Approval, review completion, acceptance into shared codebase, accountability.

---

### **Q2. After resolving a merge conflict, why is testing the application important before finalizing the merge?**

(Explain briefly.)

_Expected focus:_
Avoiding hidden bugs, validation after manual changes.

---

### **Q3. Merge Without Conflict (Basic Workflow)**

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
> - Branches
> - Commits
> - Pull Requests
> - Merge (with or without conflict)

---

### **Q4. Merge With Conflict (Conflict Resolution Workflow)**

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

- GitHub repository link
- Pull Request showing conflict and resolution

---
