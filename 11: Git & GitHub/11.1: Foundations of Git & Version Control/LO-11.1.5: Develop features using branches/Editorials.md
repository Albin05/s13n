## **Q1. What is meant by “isolated development” when using Git branches?**

### **Problem Description**

When multiple developers work on the same project, changes can interfere with each other if not properly separated.

### **Objective**

Explain the concept of isolated development in the context of Git branches.

### **Hint**

Think about working independently without affecting the main code.

### **Short Explanation**

Isolated development means working on changes separately without impacting the main branch.

### **Detailed Explanation**

In **Git**, isolated development refers to creating branches where developers can work on features, fixes, or experiments independently. Changes made in a branch do not affect the main codebase until they are explicitly merged. This allows safe experimentation and parallel development.

### **Constraints / Edge Cases (Optional)**

- Poor merge practices can still introduce conflicts
- Long-lived branches may drift from main

---

## **Q2. Why is branch cleanup considered a best practice in Git?**

### **Problem Description**

Over time, repositories can accumulate many unused or merged branches.

### **Objective**

Explain why deleting unused branches is important.

### **Hint**

Think about clarity, maintenance, and confusion.

### **Short Explanation**

Branch cleanup keeps the repository clean and easy to manage.

### **Detailed Explanation**

Branch cleanup is considered a best practice because merged or unused branches no longer serve a purpose. Keeping them can clutter the repository, confuse team members, and make branch management harder. Deleting such branches improves readability, reduces mistakes, and ensures developers focus only on active work.

### **Constraints / Edge Cases (Optional)**

- Branches should be deleted only after successful merge
- Some teams keep long-lived branches for releases

---

## **Q3. Create a project and work using branches**

### **Problem Description**

Understanding Git branching requires hands-on practice with creating, switching, and committing in branches.

### **Objective**

Demonstrate creating a repository, working on a feature branch, and committing changes.

### **Hint**

Follow the standard Git branching workflow.

### **Short Explanation**

This task shows how to create and work in a feature branch.

### **Detailed Explanation**

```bash
mkdir branch-demo
cd branch-demo

git init

echo "Initial content" > app.txt
git add app.txt
git commit -m "Initial commit on main"

git branch feature-update
git switch feature-update

echo "Feature branch update" >> app.txt
git add app.txt
git commit -m "Update app.txt in feature branch"

git switch main
```

### **Constraints / Edge Cases (Optional)**

- Git may use `master` instead of `main` in older versions
- File must be staged before committing

---

## **Q4. Merge a feature branch and clean it up**

### **Problem Description**

After completing feature development, changes must be merged and the branch removed.

### **Objective**

Demonstrate merging a branch and deleting it safely.

### **Hint**

Merge first, then delete.

### **Short Explanation**

Merged branches can be safely deleted to keep the repository clean.

### **Detailed Explanation**

```bash
git merge feature-update
git branch -d feature-update
git branch
```

- `git merge feature-update` merges the feature branch into `main`
- `git branch -d feature-update` deletes the merged branch
- `git branch` verifies the remaining branches

### **Constraints / Edge Cases (Optional)**

- `-d` prevents deletion if branch is not fully merged
- Use `-D` only when you are sure
