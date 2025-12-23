## **Q1. Purpose of setting an upstream branch using `git push -u`**

### **Problem Description**

When pushing a branch to a remote repository for the first time, Git needs to know which remote branch it should track.

### **Objective**

Explain why the `-u` (upstream) flag is used during the first push.

### **Hint**

Think about future `git push` and `git pull` commands.

### **Short Explanation**

Setting an upstream branch links the local branch to a remote branch.

### **Detailed Explanation**

Using `git push -u origin branch-name` sets an **upstream relationship** between the local branch and the remote branch. After this is done, Git knows where to push and pull from by default. This allows developers to use simple commands like `git push` and `git pull` without specifying the remote and branch every time.

### **Constraints / Edge Cases (Optional)**

- Required only for the first push of a branch
- Upstream can be changed later if needed

---

## **Q2. Difference between `git fetch` and `git pull` (and why fetch is safer)**

### **Problem Description**

Developers often need to update their local repository with changes from the remote repository.

### **Objective**

Differentiate between `git fetch` and `git pull` and explain why fetch is safer.

### **Hint**

One updates references only, the other updates code automatically.

### **Short Explanation**

`git fetch` downloads changes without merging, while `git pull` fetches and merges automatically.

### **Detailed Explanation**

`git fetch` retrieves the latest changes from the remote repository and updates remote-tracking branches, but it **does not modify the working directory**. This allows developers to review changes before merging.
`git pull` performs a fetch followed by an automatic merge, which can introduce conflicts immediately. Fetch is considered safer because it gives developers full control over when and how changes are merged.

### **Constraints / Edge Cases (Optional)**

- Pull can cause unexpected conflicts
- Fetch requires an extra merge step

---

## **Q3. Local to Remote Workflow (First Push)**

### **Problem Description**

A local Git repository must be connected to a remote repository to enable sharing and collaboration.

### **Objective**

Demonstrate the first-time push workflow from local to remote.

### **Hint**

Initialize locally, then link and push to remote.

### **Short Explanation**

The first push connects the local repository to a remote and uploads initial commits.

### **Detailed Explanation**

In this task, a local repository is created and a `README.md` file is committed. A remote repository is then created on **GitHub** and linked using `git remote add origin`. The code is pushed using `git push -u origin main`, which uploads the commit and sets the upstream branch. This establishes the foundation for all future collaboration.

### **Constraints / Edge Cases (Optional)**

- Remote repository must exist before pushing
- Branch name (`main` vs `master`) must match

---

## **Q4. Feature Branch → Push → Pull Request → Merge**

### **Problem Description**

Direct commits to the main branch can introduce unstable code.

### **Objective**

Demonstrate a safe feature-based workflow using branches and Pull Requests.

### **Hint**

Changes flow through a feature branch before reaching main.

### **Short Explanation**

Feature branches isolate work and are merged through Pull Requests.

### **Detailed Explanation**

In this workflow, a new branch `feature-update` is created from `main`. Changes are committed locally and pushed to the remote repository. A Pull Request is then raised to merge the feature branch into `main`. After review and successful merge, the feature branch is deleted to keep the repository clean. This process ensures code review, traceability, and controlled integration.

### **Constraints / Edge Cases (Optional)**

- Merge conflicts may need manual resolution
- Branch deletion should happen only after merge

---

## **Q5. Collaboration Workflow with Pull Requests**

### **Problem Description**

Multiple developers working on the same repository need a structured collaboration process.

### **Objective**

Demonstrate collaboration using Pull Requests, either with a real collaborator or a simulated workflow.

### **Hint**

Think in terms of ownership, review, and controlled merging.

### **Short Explanation**

Pull Requests enable collaboration, review, and safe merging of changes.

### **Detailed Explanation**

In this task, changes are made in a separate branch (`collab-feature`) either by a collaborator or via solo simulation. The branch is pushed to GitHub and a Pull Request is raised against `main`. The Pull Request allows review, discussion, and approval before merging. Once merged, the changes become part of the main branch, demonstrating a real-world collaborative workflow.

### **Constraints / Edge Cases (Optional)**

- Fork-based workflows are used in open-source projects
- Review delays can slow integration

---
