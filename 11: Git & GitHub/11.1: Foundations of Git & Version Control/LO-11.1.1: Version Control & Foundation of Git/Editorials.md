## **1. Define Version Control System (VCS)**

### **Problem Description**

When multiple changes are made to a project over time, it becomes difficult to track what changed, when it changed, and who made the change.

### **Objective**

Define what a Version Control System is and explain its core purpose.

### **Hint**

Think about tracking changes, history, and collaboration.

### **Short Explanation**

A Version Control System helps manage and track changes to files over time.

### **Detailed Explanation**

A **Version Control System (VCS)** is a software tool that records changes made to files so that developers can review history, compare versions, and revert to earlier states if needed. It enables multiple people to work on the same project simultaneously without overwriting each other’s work. VCS also provides accountability by maintaining a record of who made each change and why.

### **Constraints / Edge Cases (Optional)**

- Without proper usage, history can still become messy
- Learning curve exists for beginners

---

## **2. Why manually copying project folders is not a reliable version-management method**

### **Problem Description**

Many beginners manage versions by duplicating folders like `project_v1`, `project_v2`, or `final_final`, which quickly becomes confusing.

### **Objective**

Explain why manual folder copying is a poor approach to version management.

### **Hint**

Consider scalability, accuracy, and collaboration.

### **Short Explanation**

Manual copying is error-prone and does not provide reliable version tracking.

### **Detailed Explanation**

Manually copying project folders does not maintain a clear history of changes and makes it difficult to identify what was modified between versions. It wastes storage space, increases the risk of losing work, and completely breaks down in collaborative environments. There is no built-in way to merge changes, track authorship, or safely revert to a specific state, making it unsuitable for real-world software development.

### **Constraints / Edge Cases (Optional)**

- May work only for very small, solo, short-term projects
- Becomes unmanageable as the project grows

---

## **3. Why Git has become the industry standard (two strong reasons)**

### **Problem Description**

There are many version control tools available, yet one dominates the software industry.

### **Objective**

Evaluate why **Git** is widely adopted as the industry standard.

### **Hint**

Focus on architecture and workflow efficiency.

### **Short Explanation**

Git is fast, reliable, and designed for modern collaborative development.

### **Detailed Explanation**

Git has become the industry standard primarily because of its **distributed architecture**, where every developer has a complete copy of the repository, enabling offline work and fast operations. Additionally, Git offers **powerful branching and merging**, allowing developers to experiment safely, work in parallel, and integrate changes efficiently. These features make Git highly scalable and ideal for both small teams and large enterprise projects.

### **Constraints / Edge Cases (Optional)**

- Git can be complex for beginners
- Poor branching practices can cause confusion

---
