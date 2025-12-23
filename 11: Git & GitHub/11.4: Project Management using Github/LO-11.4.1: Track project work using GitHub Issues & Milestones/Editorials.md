## **Q1. Why GitHub Issues are preferred over external task-tracking tools**

### **Problem Description**

Software teams often use separate tools for code hosting and task tracking, which can create fragmentation and loss of context.

### **Objective**

Explain why GitHub Issues are more effective than external tools for managing software projects.

### **Hint**

Think about proximity to code, collaboration, and traceability.

### **Short Explanation**

GitHub Issues keep tasks directly connected to the code and development workflow.

### **Detailed Explanation**

GitHub Issues are preferred because they provide **centralized tracking alongside the source code** in **GitHub**. Developers can discuss issues, reference commits, and link pull requests in one place, improving collaboration. Each issue can be traced directly to code changes through commit messages and PR links, creating strong **traceability** between requirements, bugs, and actual implementations—something external tools often struggle to maintain seamlessly.

### **Constraints / Edge Cases (Optional)**

- Limited advanced reporting compared to dedicated PM tools
- Large non-technical teams may need additional tooling

---

## **Q2. Difference between Labels and Milestones in GitHub Project Management**

### **Problem Description**

GitHub provides multiple ways to organize issues, but each serves a different purpose.

### **Objective**

Differentiate clearly between Labels and Milestones with examples.

### **Hint**

One is for categorization, the other for planning over time.

### **Short Explanation**

Labels classify issues, while milestones group issues toward a release goal.

### **Detailed Explanation**

**Labels** are used for **categorization and filtering** issues based on type or priority.
_Example:_ An issue labeled `bug` indicates a defect that needs fixing.

**Milestones** represent **time-bound goals or releases** and track progress across multiple issues.
_Example:_ A milestone named `Version 1.0 Release` groups all issues required to complete the first release and shows progress as issues are closed.

### **Constraints / Edge Cases (Optional)**

- Labels do not show progress percentage
- Issues can belong to only one milestone at a time

---

## **Q3. Mini Project: GitHub Issue Management Setup – Editorial**

### **Problem Description**

Without structured issue management, projects quickly become unorganized and hard to track.

### **Objective**

Demonstrate proper usage of GitHub Issues, Labels, and Assignees in a real repository.

### **Hint**

Ensure every issue is categorized and owned.

### **Short Explanation**

This task sets up a clean and organized issue-tracking system using GitHub.

### **Detailed Explanation**

In this mini project, a new repository is created with a clear purpose described in `README.md`. Five issues are added to represent bugs, features, and documentation work. Custom labels (`bug`, `enhancement`, `documentation`) are created and assigned to categorize issues effectively. Assigning yourself as the assignee establishes ownership and accountability. This mirrors real-world workflows where clarity, prioritization, and responsibility are essential.

### **Constraints / Edge Cases (Optional)**

- Labels must exist before assignment
- Screenshots should clearly show labels and assignees

---

## **Q4. Milestone Planning & Progress Tracking – Editorial**

### **Problem Description**

Projects without release-level planning lack visibility into progress and deadlines.

### **Objective**

Show how milestones help plan releases and track completion.

### **Hint**

Observe how closing issues affects milestone progress.

### **Short Explanation**

Milestones group issues and visually track progress toward a release.

### **Detailed Explanation**

A milestone named `Version 1.0 Release` represents a defined release goal with a due date. By adding multiple issues to the milestone, GitHub automatically tracks progress using a completion bar. Closing issues updates the progress percentage in real time. Documenting the milestone purpose in `README.md` helps contributors understand project goals and timelines, making planning more transparent and structured.

### **Constraints / Edge Cases (Optional)**

- Progress updates only when issues are closed
- Poorly scoped milestones can give misleading progress
