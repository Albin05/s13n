# **Q4. Why is merging considered a “decision point” rather than a development activity?**

### **1. Title**

Merge as a Decision Point in Collaboration

### **2. Problem Description**

Explain why merging is treated as a confirmation step rather than a coding activity.

### **3. Objective**

Understand the conceptual role of merging in professional Git workflows.

### **4. Hint**

Think about what happens _before_ a merge is allowed.

### **5. Short Explanation**

Merging confirms that reviewed and approved work is ready to become part of the shared codebase.

### **6. Detailed Explanation**

In modern workflows, development is completed **before** a merge happens.
By the time a Pull Request reaches the merge stage:

- The code has already been written
- Reviews and discussions are complete
- Quality and intent are validated

Merging records a **team decision** that the changes are acceptable and stable.
It integrates histories, preserves collaboration context, and marks a stable checkpoint in the project’s evolution.

### **7. Constraints / Edge Cases (optional)**

Direct merges without review bypass this decision-making process and are discouraged in team environments.

---

# **Q5. Why is testing important after resolving a merge conflict?**

### **1. Title**

Importance of Testing After Conflict Resolution

### **2. Problem Description**

Explain why testing must be performed after resolving merge conflicts.

### **3. Objective**

Understand the risks involved in manual conflict resolution.

### **4. Hint**

Conflict resolution involves human decisions, not automated merges.

### **5. Short Explanation**

Conflict resolution can introduce subtle bugs, so testing ensures correctness before final integration.

### **6. Detailed Explanation**

When a merge conflict occurs, Git cannot decide which code is correct.
A developer manually edits files, removes conflict markers, and chooses the final logic.

This process may:

- Accidentally remove required functionality
- Introduce syntax or logical errors
- Break integrations between features

Testing after resolution ensures that:

- The application still runs
- Features behave as expected
- No regressions were introduced

Only after validation should the merge be finalized.

### **7. Constraints / Edge Cases (optional)**

Skipping tests may allow broken code to enter the main branch.

---

# **Q6. Merge Without Conflict (Basic Workflow)**

### **1. Title**

Clean Merge Using a Pull Request

### **2. Problem Description**

Perform a standard merge workflow where no conflicts occur.

### **3. Objective**

Practice integrating approved changes into `main` using a Pull Request.

### **4. Hint**

Ensure feature branch changes do not overlap with main branch changes.

### **5. Short Explanation**

Changes are developed in a feature branch, reviewed via a PR, and merged cleanly into `main`.

### **6. Detailed Explanation**

**Local steps:**

```bash
git clone <repo-url>
cd <repo-name>

echo "Initial content" > app.txt
git add app.txt
git commit -m "Add initial app file"
git push origin main

git checkout -b feature-a
echo "Feature A content" >> app.txt
git add app.txt
git commit -m "Add feature A content"
git push origin feature-a
```

**Remote (GitHub) steps:**

1. Open Pull Request from `feature-a → main`
2. Review changes
3. Merge Pull Request
4. Delete feature branch

This represents the ideal merge flow with no conflicts.

### **7. Constraints / Edge Cases (optional)**

If main changes before merging, conflicts may still arise.

---

# **Q7. Merge With Conflict (Conflict Resolution Workflow)**

### **1. Title**

Handling and Resolving Merge Conflicts

### **2. Problem Description**

Create a merge conflict, resolve it correctly, and finalize the merge.

### **3. Objective**

Develop confidence in detecting, resolving, and completing conflict merges.

### **4. Hint**

Conflicts occur when the same lines are modified in parallel branches.

### **5. Short Explanation**

Git pauses the merge, marks conflicting files, and requires manual resolution.

### **6. Detailed Explanation**

**Local steps (example):**

```bash
git checkout -b feature-b
echo "Conflicting change" > app.txt
git add app.txt
git commit -m "Conflicting update"
git push origin feature-b
```

**Remote steps:**

1. Raise Pull Request from `feature-b → main`
2. GitHub reports a merge conflict
3. Open conflict resolution (CLI or GitHub UI)
4. Review both versions
5. Decide final correct content
6. Remove conflict markers
7. Mark file as resolved and complete merge
8. Verify final content

Conflict markers like `<<<<<<<`, `=======`, `>>>>>>>` must **never remain** in the final code.

### **7. Constraints / Edge Cases (optional)**

- Multiple conflicted files increase complexity
- Poor understanding of code can lead to incorrect resolutions

---
