## **Q1. Why is merging considered a “decision point” rather than a development activity?**

### **Problem Description**

In collaborative development, code written in branches must eventually be integrated into a shared codebase.

### **Objective**

Explain why merging represents a formal decision rather than ongoing development.

### **Hint**

Think about review, approval, and responsibility.

### **Short Explanation**

Merging is a decision to accept changes into the shared codebase, not to create them.

### **Detailed Explanation**

Merging is considered a **decision point** because it happens after development is complete and reviews are done. At this stage, the team decides whether the changes meet quality standards and are ready to be included in the shared branch. Once merged, the code affects all contributors, making the action accountable and deliberate rather than exploratory development.

### **Constraints / Edge Cases (Optional)**

- Emergency merges may skip full review
- Admin overrides can bypass normal approvals

---

## **Q2. Why testing is important after resolving a merge conflict**

### **Problem Description**

Merge conflicts require manual edits, which can unintentionally introduce errors.

### **Objective**

Explain why testing is required after conflict resolution.

### **Hint**

Think about human error during manual edits.

### **Short Explanation**

Testing ensures that conflict resolution did not introduce hidden bugs.

### **Detailed Explanation**

When resolving merge conflicts, developers manually combine code from different branches. This process can accidentally break logic, remove required code, or introduce syntax errors. Testing the application after resolving conflicts validates that the final merged code works as expected and that no regressions were introduced during manual resolution.

### **Constraints / Edge Cases (Optional)**

- Small changes may still cause major issues
- Automated tests may not cover all edge cases

---

## **Q3. Merge Without Conflict (Basic Workflow) – Editorial**

### **Problem Description**

Not all merges result in conflicts; understanding clean merges is essential for beginners.

### **Objective**

Demonstrate a clean feature-branch merge using Pull Requests.

### **Hint**

Ensure changes do not overlap with main branch edits.

### **Short Explanation**

Non-overlapping changes allow Git to merge branches automatically.

### **Detailed Explanation**

In this workflow, a repository is created and a base commit is pushed to `main`. A feature branch (`feature-a`) is created where additional lines are added to `app.txt` without modifying the same lines changed in `main`. When a Pull Request is raised from `feature-a` to `main`, Git automatically merges the changes without conflict. After merging, the feature branch is deleted to keep the repository clean. This demonstrates the ideal and most common merge scenario in team workflows using **GitHub**.

### **Constraints / Edge Cases (Optional)**

- Even small overlapping edits can cause conflicts
- Branch deletion should happen only after merge confirmation

---

## **Q4. Merge With Conflict (Conflict Resolution Workflow) – Editorial**

### **Problem Description**

Conflicts occur when multiple branches modify the same lines of a file.

### **Objective**

Demonstrate how to identify, resolve, and safely complete a conflicting merge.

### **Hint**

Focus on conflict markers and manual resolution.

### **Short Explanation**

Merge conflicts require manual intervention to decide which changes to keep.

### **Detailed Explanation**

In this workflow, a branch (`feature-b`) modifies the same lines in `app.txt` that were also changed in `main`. When a Pull Request is raised, Git detects conflicting changes and blocks automatic merging. The developer must resolve the conflict either using the command line or GitHub’s UI by choosing or combining changes and removing conflict markers. After resolving the conflict and verifying the final content, the merge is completed. This process ensures correctness and intentional integration of competing changes.

### **Constraints / Edge Cases (Optional)**

- Incorrect conflict resolution can break functionality
- Conflict markers must be completely removed before merge

---
