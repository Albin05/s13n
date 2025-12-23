### **Q1. What is the primary goal of using `git rebase` instead of `git merge`?**

A) To delete old commits
B) To preserve branch structure exactly as it happened
C) To create a cleaner, linear commit history
D) To avoid committing changes

**Correct Answer:** C

---

### **Q2. Which statement best describes what rebase does?**

A) It combines two histories by creating a merge commit
B) It rearranges commits by replaying them on top of another branch
C) It deletes commits from the feature branch
D) It synchronizes local and remote repositories

**Correct Answer:** B

---

### **Q3. On which branch should rebase typically be performed?**

A) `main` branch
B) Any shared branch
C) Feature branch owned by the developer
D) Remote-tracking branch

**Correct Answer:** C

---

### **Q4. Why does rebase generate new commit IDs, and why does this matter?**

(Answer in 3–4 lines.)

*Expected focus:*
History rewriting, commit hash change, impact on shared branches.

---

### **Q5. In what real-world scenario is rebase safer and more appropriate than merge?**

(Explain briefly.)

*Expected focus:*
Updating feature branch with latest main before merge.

---


### **Q6. Rebase a Feature Branch onto Main (No Conflicts)**

**Task:**
Perform the following steps and write the Git commands used:

1. Create a repository named **rebase-demo**
2. Create a file **app.txt** and commit it on `main`
3. Create a branch **feature-login**
4. Add new content to **app.txt** and commit it
5. Switch back to `main` and make another commit on **app.txt**
6. Switch to **feature-login**
7. Rebase **feature-login** onto `main`
8. Verify that the commit history is linear

> ⚠️ **Instruction:**
> Perform these tasks locally using Git.
> Submit the **terminal commands used** or a **repository link** if required by your course.

---

### **Q7. Handle a Rebase Conflict**

**Task:**
Using the same repository or a new one:

1. Create a conflict by modifying the same lines in **app.txt** on both `main` and **feature-ui**
2. Start rebasing **feature-ui** onto `main`
3. Encounter a conflict
4. Resolve the conflict manually
5. Stage the resolved file
6. Continue the rebase
7. Abort the rebase if required

Write the Git commands used at each step.

> ⚠️ **Instruction:**
> Perform these tasks locally using Git.
> Submit the **terminal commands used** or a **repository link** if required by your course.

---

