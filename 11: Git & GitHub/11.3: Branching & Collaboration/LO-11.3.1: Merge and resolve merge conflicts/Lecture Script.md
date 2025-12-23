### **1. Set Context — What Happens After a Pull Request (3 minutes)**

* Recap briefly:

  * Code is developed on branches
  * Changes are pushed to remote
  * Pull Requests are reviewed and approved
* State clearly:

  * After approval, changes must enter the main codebase
* Introduce **merge** as the final step in collaboration.
* Emphasize that:

  * Development is already complete
  * Review decisions are already made
  * Merging is about **acceptance and integration**

---

### **2. Explain What a Merge Represents (4 minutes)**

* Explain that merging:

  * Integrates approved work into another branch (usually `main`)
  * Combines commit histories, not just files
* Clarify that:

  * Git records how two independent lines of work come together
  * Project history reflects collaboration and decision-making
* Emphasize modern practice:

  * Merges are usually performed via Pull Requests
  * This ensures review, access control, and traceability

---

### **3. Merging as a Decision Point (3 minutes)**

* Explain that a merge is not automatic acceptance.
* State that by merging, the team confirms:

  * Code meets quality standards
  * Changes align with project goals
  * Work is ready for shared use
* Reinforce that:

  * A merge marks a stable checkpoint in project history

---

### **4. When Merging Is Straightforward vs Complex (4 minutes)**

* Explain that merge behavior depends on branch history.
* Describe simple merge scenario:

  * One branch progressed
  * No overlapping changes
  * Git integrates automatically
* Describe complex scenario:

  * Both branches changed independently
  * Overlapping edits exist
  * Git must reconcile differences
* Introduce the term **merge conflict** as the result of ambiguity.

---

### **5. Define a Merge Conflict (4 minutes)**

* Define a merge conflict as:

  * Two branches modifying the same part of the same file
  * In incompatible ways
* Emphasize Git’s behavior:

  * Git does not guess
  * Git stops and asks for human input
* Clarify that:

  * The merge is paused
  * Resolution is mandatory before proceeding

---

### **6. Discuss Common Causes of Merge Conflicts (5 minutes)**

* Present typical scenarios:

  * Same lines edited in multiple branches
  * File deleted in one branch and edited in another
  * File renamed in one branch and modified in another
  * Long-lived branches falling behind `main`
  * Large refactors overlapping with active features
* Emphasize timing:

  * The longer branches live independently, the higher the risk

---

### **7. Explain What Happens Internally During a Conflict (4 minutes)**

* Explain Git’s internal behavior:

  * Merge process is paused
  * Conflicted files are marked
  * Repository enters a conflicted state
* Clarify that:

  * Normal commits are blocked
  * Merge must be resolved or aborted

---

### **8. Explain Conflict Markers Conceptually (5 minutes)**

* Explain that Git modifies conflicted files to show both versions.
* Describe conflict markers:

  * Current branch version
  * Incoming branch version
  * Clear separator between them
* Emphasize that:

  * Conflict markers are not valid code
  * They must be removed
  * A final decision must be made

---

### **9. Explain Conflict Resolution via CLI (Conceptual Flow) (5 minutes)**

* Walk through the conceptual responsibility of the developer:

  1. Identify conflicted files
  2. Open files manually
  3. Review both versions carefully
  4. Decide final correct logic
  5. Remove all conflict markers
  6. Save files
  7. Stage resolved files
  8. Complete the merge
* Emphasize:

  * Resolution is a thinking task
  * Not a mechanical action

---

### **10. Explain Conflict Resolution via GitHub UI (4 minutes)**

* Introduce GitHub’s web-based resolution option.
* Explain when it is useful:

  * Small conflicts
  * Easy-to-understand changes
  * Visual comparison preferred
* Explain what GitHub UI provides:

  * Side-by-side comparison
  * Editing capability
  * Automatic marker removal
  * Commit creation
* Reinforce that:

  * Internally, GitHub performs the same merge steps

---

### **11. Choosing the Right Resolution Approach (4 minutes)**

* Compare both approaches conceptually:

  * CLI resolution for complex, multi-file conflicts
  * GitHub UI for small, simple conflicts
* Emphasize that:

  * Both produce the same Git result
  * Choice depends on complexity and testing needs

---

### **12. Stress the Importance of Testing After Resolution (4 minutes)**

* Explain that resolving conflicts is not the final step.
* State required validation:

  * Application builds or runs
  * Tests pass
  * Core functionality works
* Emphasize risk:

  * Conflicts can introduce subtle bugs
  * Testing prevents silent failures

---

### **13. Finalizing the Merge (3 minutes)**

* Explain that after successful resolution and testing:

  * Merge is completed
  * Pull Request is finalized
  * Main branch receives updated code
* Reinforce that:

  * All collaborators then synchronize changes
  * Project history reflects the merge decision

---

### **14. Common Mistakes During Conflict Resolution (4 minutes)**

* Discuss frequent errors:

  * Leaving conflict markers in files
  * Removing required logic accidentally
  * Resolving without understanding the code
  * Skipping testing
* Reinforce:

  * Conflict resolution requires understanding and intent
  * It is a decision-making process

---

