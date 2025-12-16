### **1. Introduce the Importance of Commit History (5 minutes)**

- Begin by shifting focus from code to history:

  - Code correctness is important
  - Commit history explains _how_ the code reached its current state

- Explain how commit history is used in real projects:

  - Debugging regressions
  - Understanding past decisions
  - Auditing changes

- Present the common issue:

  - Feature branches live for days or weeks
  - Main branch keeps moving
  - When branches are merged carelessly, history becomes cluttered

- Raise guiding questions:

  - Why does commit history become hard to read?
  - Is there a way to integrate changes without polluting history?

---

### **2. Introduce Rebase as the Conceptual Solution (4 minutes)**

- Introduce **rebase** as a Git operation that changes the base of a branch.
- Explain the key idea:

  - Commits are not merged as-is
  - They are replayed on top of another branch

- Clarify the mental model:

  - Merge → combines histories
  - Rebase → rearranges history

- Emphasize that:

  - Final code remains the same
  - Only commit history changes

---

### **3. Position Rebase as an Alternative to Merge (4 minutes)**

- Explain what happens with a normal merge:

  - Parallel histories remain visible
  - Merge commits appear

- Explain the downside:

  - History becomes harder to follow
  - Too many branches and merge points

- Present rebase as an alternative:

  - Feature commits are placed on top of the latest main branch
  - History becomes linear
  - No additional merge commit is created

- Emphasize that rebase prioritizes **readability over historical branching accuracy**.

---

### **4. Present a Real-World Rebase Scenario (5 minutes)**

- Describe a typical workflow:

  - Developer creates a feature branch
  - Work continues for some time
  - Other changes are merged into `main`

- Explain the problem:

  - Feature branch becomes outdated

- Compare outcomes:

  - Without rebase → merge commit, messy history
  - With rebase → clean, updated branch

- Emphasize:

  - This is the most common and safest use of rebase
  - Rebase prepares the branch for a clean merge

---

### **5. Explain the Basic Rebase Workflow (Conceptual) (5 minutes)**

- Explain that rebase must be done on the **feature branch**.
- Walk through the conceptual steps:

  - Switch to feature branch
  - Rebase it onto the latest main branch

- Describe what Git does internally:

  - Temporarily removes feature commits
  - Updates branch pointer to latest main
  - Replays commits one by one

- Mention that:

  - If there are no conflicts, rebase completes automatically

---

### **6. Explain What Changes After a Rebase (4 minutes)**

- Describe the results of a successful rebase:

  - Feature branch now starts from latest main
  - Commit IDs are regenerated
  - History becomes linear

- Explain the benefit:

  - When merging later, Git can often fast-forward
  - Main branch history remains clean

- Reinforce:

  - Rebase reshapes history intentionally

---

### **7. Explain Conflict Handling During Rebase (Conceptual) (5 minutes)**

- Explain that rebase may pause if conflicts occur.
- Describe the paused state:

  - Git stops at the conflicting commit
  - Developer must resolve conflicts manually

- Explain the continuation flow:

  - Conflicts resolved
  - Rebase continues

- Also explain aborting:

  - Rebase can be cancelled
  - Branch returns to original state

- Emphasize:

  - Rebase conflicts are resolved one commit at a time
  - This often makes conflicts easier to understand

---

### **8. Explain Rebase and Remote Repositories (4 minutes)**

- Explain that rebase rewrites commit history.
- Emphasize the rule:

  - Rebase should be done **before pushing**

- Explain the risk:

  - Rebasing pushed branches changes shared history

- Introduce the safety rule:

  - Rebase only branches you own

- Mention that forced pushing may be required after rebase:

  - This must be done carefully
  - Only when the developer understands the impact

---

### **9. Compare Rebase vs Merge for Decision-Making (5 minutes)**

- Explain merge characteristics:

  - Preserves full development story
  - Shows parallel work clearly

- Explain rebase characteristics:

  - Produces clean, linear history
  - Easier to read and debug

- Present common team practice:

  - Rebase feature branches
  - Merge into main after review

- Emphasize:

  - Choice depends on team standards and policies

---
