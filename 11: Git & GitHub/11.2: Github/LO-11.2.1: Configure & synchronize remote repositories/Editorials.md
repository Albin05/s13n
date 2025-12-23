## **Q1. What is a remote repository, and why is it important for team collaboration?**

### **Problem Description**

In team environments, developers need a shared place to store and access the project code.

### **Objective**

Explain what a remote repository is and why it is essential for collaboration.

### **Hint**

Think of a shared source of truth and teamwork.

### **Short Explanation**

A remote repository is a shared, central version of the project used by all team members.

### **Detailed Explanation**

A **remote repository** is a centrally hosted copy of a project that multiple developers can access and synchronize with. It acts as a **shared source of truth**, ensuring everyone works from the same baseline. Remote repositories enable collaboration, code sharing, reviews, backups, and coordinated development across teams, especially in distributed environments.

### **Constraints / Edge Cases (Optional)**

- Requires internet access to sync changes
- Conflicts may occur if multiple changes overlap

---

## **Q2. How local and remote repositories work together in Git**

### **Problem Description**

Git uses both local and remote repositories, which can confuse beginners.

### **Objective**

Explain how local and remote repositories interact using commit, push, and pull.

### **Hint**

Think of local work first, then sharing.

### **Short Explanation**

Git follows a local-first workflow where changes are shared explicitly.

### **Detailed Explanation**

In **Git**, developers first make changes and create **commits locally**, even without internet access. These commits remain private until explicitly shared using `git push` to the remote repository. To receive updates from teammates, developers use `git pull`, which fetches and merges remote changes into the local repository. This controlled synchronization allows flexibility, safety, and better collaboration.

### **Constraints / Edge Cases (Optional)**

- Forgetting to pull can lead to conflicts
- Push may fail if remote has newer commits

---

## **Q3. “I committed my changes, so my teammates can see them.” — Is this correct?**

### **Problem Description**

There is a common misunderstanding about when changes become visible to others.

### **Objective**

Clarify the difference between committing and sharing changes.

### **Hint**

Where does the commit live?

### **Short Explanation**

No, commits are local until they are pushed to a remote repository.

### **Detailed Explanation**

This statement is **incorrect**. A `git commit` saves changes only in the **local repository**. Teammates cannot see these changes until the developer uses `git push` to send the commits to the remote repository. Until then, the work exists only on the developer’s machine and is invisible to others.

### **Constraints / Edge Cases (Optional)**

- Commits on feature branches are also invisible until pushed
- Force-push can overwrite shared history if misused

---

## **Q4. Typical end-to-end collaboration flow using a remote repository**

### **Problem Description**

Understanding collaboration requires seeing the complete workflow from start to finish.

### **Objective**

List the standard steps involved in collaborative Git development.

### **Hint**

Start from remote and end with merge and sync.

### **Short Explanation**

Collaboration follows a structured flow from cloning to merging.

### **Detailed Explanation**

A typical end-to-end collaboration flow is:

1. Start from a **remote repository**
2. Clone or fork the repository locally
3. Create a branch and make local changes
4. Commit changes locally
5. Push commits to the remote repository
6. Create a Pull Request
7. Review and discuss changes
8. Merge the Pull Request into the main branch
9. Pull the latest changes to keep local repository in sync

This workflow ensures safe collaboration, review, and code quality.

### **Constraints / Edge Cases (Optional)**

- Conflicts may occur during merge
- Review delays can slow down integration
