## **Q4. Why GitHub Issues are preferred over external task-tracking tools for managing software projects**

### **Problem Description**

Software teams need a reliable way to track bugs, features, and tasks while maintaining a strong connection between planning and actual code changes.

### **Objective**

Explain why **GitHub Issues** are more effective than external task-tracking tools.

### **Hint**

Focus on integration with code, collaboration, and traceability.

### **Short Explanation**

GitHub Issues are preferred because they keep task tracking tightly integrated with the codebase and development workflow.

### **Detailed Explanation**

GitHub Issues provide **centralized tracking directly alongside the source code**, eliminating the need to switch between multiple tools. Developers, testers, and reviewers collaborate in one place through comments, mentions, and references. Issues can be linked directly to commits and pull requests, creating strong **traceability** between tasks and code changes. This tight integration improves transparency, reduces communication gaps, and ensures that every change in the code can be traced back to a requirement or bug.

### **Constraints / Edge Cases (Optional)**

- GitHub Issues may lack advanced reporting compared to dedicated project management tools
- Large non-technical teams may require additional tooling

---

## **Q5. Differentiate between Labels and Milestones in GitHub Project Management**

### **Problem Description**

GitHub provides multiple organizational tools, but each serves a different purpose in project management.

### **Objective**

Clearly differentiate between **Labels** and **Milestones** with examples.

### **Hint**

Think of _classification_ vs _planning over time_.

### **Short Explanation**

Labels categorize issues, while milestones group issues toward a time-bound goal.

### **Detailed Explanation**

**Labels** are used to **classify and filter issues** based on their nature, such as `bug`, `enhancement`, or `high-priority`.
_Example:_ An issue tagged with the label `bug` indicates a defect that needs fixing.

**Milestones**, on the other hand, represent **time-bound goals or releases** and help track progress across multiple issues.
_Example:_ A milestone named `Version 1.0 Release` may include all issues required to complete the first stable release of the product.

### **Constraints / Edge Cases (Optional)**

- Labels do not track progress percentage
- Milestones require manual issue assignment

---

## **Q6. Mini Project: GitHub Issue Management Setup – Editorial**

### **Problem Description**

A project without structured issue management becomes difficult to track, prioritize, and maintain.

### **Objective**

Demonstrate proper setup and usage of GitHub Issues, Labels, and Assignees in a real repository.

### **Hint**

Ensure every issue is clearly categorized and owned.

### **Short Explanation**

This task establishes a structured issue-tracking system using GitHub’s built-in tools.

### **Detailed Explanation**

In this mini project, a new repository is created with a clear purpose defined in `README.md`. Five issues are added to represent different types of work—bugs, features, and documentation. Custom labels (`bug`, `enhancement`, `documentation`) are created to categorize issues, making filtering and prioritization easier. Assigning yourself as the assignee ensures accountability. This setup mirrors real-world project workflows where clarity, ownership, and organization are essential.

### **Constraints / Edge Cases (Optional)**

- Labels must be created before assignment
- Screenshots must clearly show labels and assignees

---

## **Q7. Milestone Planning & Progress Tracking – Editorial**

### **Problem Description**

Without release-level planning, teams struggle to measure progress and meet deadlines.

### **Objective**

Show how milestones help in planning releases and tracking progress.

### **Hint**

Observe how issue completion affects milestone progress.

### **Short Explanation**

Milestones group related issues and visually track progress toward a release goal.

### **Detailed Explanation**

A milestone named `Version 1.0 Release` represents a concrete release target with a defined due date. By assigning multiple issues to the milestone, GitHub automatically tracks progress using a completion bar. Closing even a single issue updates the progress percentage, giving real-time visibility into release readiness. Documenting the milestone purpose in `README.md` reinforces planning clarity and helps contributors understand project goals.

### **Constraints / Edge Cases (Optional)**

- Progress updates only when issues are closed
- Issues can belong to only one milestone at a time
