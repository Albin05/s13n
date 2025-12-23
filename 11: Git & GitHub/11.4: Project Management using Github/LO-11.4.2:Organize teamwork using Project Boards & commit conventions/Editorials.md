## **4. Why are project boards more effective than issue lists for understanding real-time project progress?**

### **Problem Description**

Issue lists show all tasks but do not clearly communicate the **current working state** of each task.

### **Objective**

Explain how project boards improve visibility into ongoing, pending, and completed work.

### **Hint**

Think in terms of **workflow visualization** rather than task storage.

### **Short Explanation**

Project boards visually represent the workflow using columns, making it easy to see what work is pending, active, or completed at a glance.

### **Detailed Explanation**

While issue lists only show a flat collection of tasks, project boards organize issues into workflow stages such as *To Do*, *In Progress*, and *Done*. This visual layout allows teams to instantly understand project status, identify bottlenecks, and track progress in real time. It also improves collaboration by clearly showing ownership and movement of tasks across stages.

### **Constraints / Edge Cases (Optional)**

* Boards require manual updates if automation is not configured
* Poorly maintained boards can give misleading progress signals

---

## **5. Explain why professional teams follow commit message conventions instead of writing free-form commit messages.**

### **Problem Description**

Free-form commit messages often lack consistency and clarity, making project history difficult to understand.

### **Objective**

Explain the importance of structured commit messages in professional development.

### **Hint**

Consider automation, readability, and team collaboration.

### **Short Explanation**

Commit conventions create consistency, improve readability, and enable automation across the development lifecycle.

### **Detailed Explanation**

Professional teams follow commit message conventions (such as *Conventional Commits*) to maintain a clean and predictable commit history. Structured messages help team members quickly understand changes, enable automated versioning and changelog generation, and allow tools to link commits with issues and pull requests. This discipline is critical in large teams where multiple developers contribute simultaneously.

### **Constraints / Edge Cases (Optional)**

* Requires initial team onboarding and discipline
* Overly strict rules may slow down inexperienced contributors

---

## **6. Project Board Setup Task – Editorial**

### **Problem Description**

Teams need a way to visually track task progress instead of relying only on issue lists.

### **Objective**

Demonstrate how to set up and use a Kanban-style project board in **GitHub**.

### **Hint**

Use existing issues and focus on movement between columns.

### **Short Explanation**

A Kanban project board visually organizes issues into workflow stages, helping teams track progress efficiently.

### **Detailed Explanation**

In this task, a Kanban project board is created with three standard columns: *To Do*, *In Progress*, and *Done*. Existing issues are added as cards to the board. Moving an issue from *To Do* to *In Progress* reflects that active development has started. This setup mirrors real-world agile workflows and provides instant visibility into project status for the entire team.

### **Constraints / Edge Cases (Optional)**

* Issues must already exist to be added to the board
* Without automation, cards must be moved manually

---

## **7. Issue–PR–Commit Linking Task – Editorial**

### **Problem Description**

Disconnected issues, pull requests, and commits make it difficult to trace why changes were made.

### **Objective**

Demonstrate end-to-end traceability between planning and code changes.

### **Hint**

Use issue-closing keywords and conventional commit syntax.

### **Short Explanation**

Linking issues, pull requests, and commits ensures clear traceability and automatic task closure.

### **Detailed Explanation**

In this task, an issue is linked to a pull request using keywords like `Fixes #issueNumber`. When the pull request is merged, the linked issue closes automatically, ensuring accurate task tracking. Using a conventional commit message further standardizes the change history, making it easier to audit, automate releases, and understand the intent behind each change. This practice reflects professional development workflows.

### **Constraints / Edge Cases (Optional)**

* Issue-closing keywords work only when merging into the default branch
* Incorrect issue numbers prevent automatic closure

