### **Rebase & Commit History — Pre-Read**

In collaborative projects, code quality alone is not enough. The commit history explains how the code evolved, why decisions were made, and how changes were introduced over time. A clean history improves debugging, reviews, and long-term maintenance.

---

### **Why Commit History Becomes Hard to Read**

In real projects, feature branches often live for days or weeks while the main branch continues to evolve. When these branches are merged repeatedly, the history fills with merge commits and parallel paths, making it difficult to follow the actual sequence of changes.

Reflective question:
How can changes be integrated without cluttering the project history?

---

### **What Rebase Is Conceptually**

Rebase is a Git operation that changes the starting point of a branch.
Instead of combining histories, it replays commits on top of another branch, creating a cleaner and more linear history.

The final code remains the same; only the commit history is reorganized.

---

### **Rebase vs Merge — The Core Difference**

A merge preserves the complete branching story, including parallel paths and merge commits.
Rebase rearranges commits so that changes appear as if they were developed on top of the latest main branch.

Rebase favors readability, while merge favors historical accuracy.

---

### **A Common Real-World Rebase Scenario**

A developer works on a feature branch while other changes are merged into main. Over time, the feature branch becomes outdated. Rebasing updates the branch onto the latest main, preparing it for a clean integration.

This is the most common and safest use of rebase.

---

### **What Happens During a Rebase**

When rebasing, Git temporarily removes the feature commits, moves the branch to the latest base, and reapplies each commit in order. If there are no conflicts, this process completes automatically.

If conflicts occur, Git pauses and waits for manual resolution.

---

### **What Changes After Rebase**

After rebasing, the branch starts from the latest main branch.
Commit IDs change, history becomes linear, and future merges are often fast-forward, keeping the main branch clean.

Rebase intentionally reshapes history.

---

### **Conflict Handling in Rebase**

Conflicts during rebase are resolved one commit at a time.
This makes it easier to understand which change caused the conflict. The process can either continue after resolution or be aborted to restore the original branch state.

---

### **Rebase and Remote Repositories**

Rebase rewrites commit history and should be done before pushing to a remote. Rebasing already-pushed branches can disrupt collaborators and usually requires force pushing, which must be done carefully.

A common rule is to rebase only branches you own.

---

### **Choosing Between Rebase and Merge**

Merge preserves the full development story and is safer for shared branches.
Rebase produces a clean, linear history that is easier to read and debug.

Most teams rebase feature branches locally and merge them into main after review, based on agreed team practices.

---

