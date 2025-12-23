## **Q1. Why are project boards more effective than issue lists for understanding real-time project progress?**

### **Problem Description**

Issue lists show tasks, but they do not clearly communicate the current state of work at a glance.

### **Objective**

Explain why project boards provide better real-time visibility than plain issue lists.

### **Hint**

Think about workflow stages and visual tracking.

### **Short Explanation**

Project boards visually represent the workflow, making progress easier to understand.

### **Detailed Explanation**

Project boards organize issues into workflow stages such as _To Do_, _In Progress_, and _Done_. This visual layout makes it immediately clear what work is pending, what is actively being worked on, and what is completed. Unlike flat issue lists, boards highlight progress, bottlenecks, and workload distribution in real time, which helps teams make faster decisions.

### **Constraints / Edge Cases (Optional)**

- Boards must be kept up to date to remain accurate
- Poorly designed columns can misrepresent progress

---

## **Q2. Why professional teams follow commit message conventions instead of free-form commit messages**

### **Problem Description**

Unstructured commit messages make project history difficult to understand and maintain.

### **Objective**

Explain the importance of commit message conventions in professional teams.

### **Hint**

Consider consistency, automation, and collaboration.

### **Short Explanation**

Commit conventions bring consistency, clarity, and automation support.

### **Detailed Explanation**

Professional teams follow commit message conventions to maintain a clean and readable commit history. Structured messages clearly communicate _what_ changed and _why_, making collaboration easier. Conventions also enable automation such as changelog generation, versioning, and issue linking, which is not possible with random free-form messages.

### **Constraints / Edge Cases (Optional)**

- Requires initial team discipline
- Overly strict rules may slow beginners initially

---

## **Q3. Project Board Setup Task – Editorial**

### **Problem Description**

Teams need a way to track work progress visually rather than relying only on issue lists.

### **Objective**

Demonstrate visual task tracking using a Kanban-style project board in **GitHub**.

### **Hint**

Use existing issues and move them across workflow stages.

### **Short Explanation**

A Kanban board visually tracks issues as they move through the workflow.

### **Detailed Explanation**

In this task, a Kanban project board is created with three columns: _To Do_, _In Progress_, and _Done_. Existing issues are added as cards to the board. Moving an issue from _To Do_ to _In Progress_ reflects that active development has started. This setup mirrors real-world agile workflows and allows the entire team to instantly understand project status.

### **Constraints / Edge Cases (Optional)**

- Issues must exist before being added to the board
- Manual movement is required unless automation is enabled

---

## **Q4. Issue–PR–Commit Linking Task – Editorial**

### **Problem Description**

Without proper linking, it becomes difficult to trace why code changes were made.

### **Objective**

Demonstrate traceability between issues, pull requests, and commits.

### **Hint**

Use issue-closing keywords and reference issue numbers.

### **Short Explanation**

Linking issues, PRs, and commits ensures clear traceability and accountability.

### **Detailed Explanation**

In this task, an issue is linked to a Pull Request using keywords such as `Fixes #issueNumber`. When the Pull Request is merged, the linked issue closes automatically. Using a conventional commit message that references the issue number ensures that code changes can always be traced back to a specific task or requirement. This practice is essential for audits, reviews, and professional project management.

### **Constraints / Edge Cases (Optional)**

- Auto-closing works only when merging into the default branch
- Incorrect issue numbers break the linkage
