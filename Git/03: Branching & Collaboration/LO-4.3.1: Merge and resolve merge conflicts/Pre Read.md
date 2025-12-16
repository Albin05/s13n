In collaborative development, changes are not complete until they are merged into the shared codebase. Merging is the step where reviewed and approved work becomes part of the main branch, marking an official integration point in the project’s history.

---

### **Real-World Problems Without a Clear Merge Process**

Unreviewed code reaches the main branch.
Parallel changes overwrite each other.
No clear record of why or when changes were accepted.
Bugs enter production without accountability.

Reflective question:
How do teams safely accept changes without breaking stable code?

---

### **What a Merge Represents**

A merge is the act of integrating one branch’s commit history into another, usually into `main`.
It is not about writing new code, but about accepting completed work after review.

- Integrates approved changes
- Preserves collaboration history
- Marks a stable checkpoint in the project

Merges usually happen through Pull Requests to ensure review and traceability.

---

### **Why Merges Sometimes Fail Automatically**

When two branches evolve independently, Git must reconcile differences.
If the same part of a file is changed in incompatible ways, Git refuses to guess and stops the merge.

This situation is called a **merge conflict**.

---

### **What a Merge Conflict Means**

A merge conflict indicates ambiguity, not an error.

- Git detected overlapping changes
- Automatic merge was not safe
- Human decision is required
- Integration is paused until resolved

Conflicts protect the codebase from unintended data loss.

---

### **Common Causes of Merge Conflicts**

Conflicts typically occur when parallel work overlaps.

Examples include:

- Editing the same lines in a file
- Deleting a file in one branch while modifying it in another
- Renaming files during active development
- Long-running branches falling behind main

The longer branches remain separate, the higher the risk.

---

### **What Happens During a Conflict**

When a conflict occurs, Git pauses the merge and marks the affected files.
These files are temporarily modified to show both versions of the conflicting changes.

![Merge Conflict](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/29216d01-1968-4352-9d6f-606c74dc553d/vkbLoaViDCX0pzbJ.png)

The repository enters a conflicted state until a decision is made.

---

### **Resolving Conflicts Conceptually**

Resolving a conflict involves reviewing both versions, deciding the correct final code, and removing all conflict markers.
Once resolved, the merge can continue and be completed.

Conflict resolution is a reasoning task, not a mechanical one.

---

### **CLI vs GitHub UI Resolution**

Conflicts can be resolved locally using Git or directly on GitHub.

Local resolution is preferred for complex changes requiring testing.
GitHub’s interface is useful for small, straightforward conflicts with visual comparison.

Both approaches achieve the same outcome.

---

### **Why Testing After Resolution Matters**

Conflict resolution can unintentionally introduce bugs.
Testing ensures that the integrated code still works as expected before final acceptance.

A merge is complete only after validation.

---

### **Quick Self-Check**

- Do you understand why a merge is being accepted?
- Can you explain both sides of a conflict?
- Did you validate the code after resolving it?

These questions ensure merges are intentional and safe.

---
