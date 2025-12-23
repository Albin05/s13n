## 1. **Set Context (3 minutes)**

- Keep Open VS Code project folder say 'First-Git-Project'. Keep terminal open”

---

## 2. **Demonstrate the 3-Area Model (Working → Staging → Repository) (6 minutes)**

### Show the image, explain how Working logic of Git

### **Step 1 — Show Working Directory**

“Create a new file named `demo.txt` in your project.
Type this line inside it:
`Hello Git`
Save the file.”

“Now go to the terminal and run:”

```bash
git status
```

**Tell them what to observe:**
“Notice Git says this file is _untracked_. That means it’s only in the **working directory**, not tracked by Git yet.”

---

### **Step 2 — Move a File to Staging**

“Now stage the file. Run:”

```bash
git add demo.txt
```

“Check status again:”

```bash
git status
```

“Observe the difference — now the file is in the **staging area**.
Git is ready to take a clean snapshot of it.”

---

### **Step 3 — Commit to Repository**

“Let’s save this snapshot permanently. Run:”

```bash
git commit -m "Add demo.txt with initial text"
```

“Now that snapshot is stored in your **local repository**.”

---

## **Explore `git status` — Live Feedback Loop**

“Make a small edit in `demo.txt`. Add one more line:
`Learning staging`
Save it.”

“Run:”

```bash
git status
```

“Point out what Git shows: unstaged changes.
This is your real-time dashboard — use it constantly.”

---

## 3. **Repeat the process with another example and allow students to practice the same ( 5 minutes)**

## 4. **Practice Staging Variants (3 minutes)**

“Try staging everything with:”

```bash
git add .
```

“Undo that using:”

```bash
git reset
```

“Now stage only updates (no new files):”

```bash
git add -u
```

Explain while demonstrating:
“These variations help you control _what exactly_ goes into a commit.”

---

## 5. **Commit Cleanly — Commanding Good Messages**

“Now commit again. Use a meaningful message:”

```bash
git commit -m "Update demo.txt with learning note"
```

“Short, action-based, present tense. No vague ‘final commit’ messages in this class.”

---

## 6. **View History Using `git log`**

“Run:”

```bash
git log --oneline
```

“Keep the output open. Explain each commit represents a snapshot of your project at a moment in time.”

---

## 7. **Compare Changes Using `git diff` (3 minutes)**

### **A. Compare Working Directory vs Staged**

“Modify the file again.
Add: `Diff practice`
Save it.”

“Now run:”

```bash
git diff
```

“Explain: this shows what is changed but _not yet staged_.”

---

### **B. Compare Staged vs Last Commit**

“Stage it:”

```bash
git add demo.txt
```

“Now run:”

```bash
git diff --staged
```

“This shows what will be committed.”

---

### **C. Compare Two Commits**

“Copy two commit IDs from `git log --oneline` and run something like:”

```bash
git diff a1b2c3d f4e5d6a
```

“Explain how Git highlights additions (+) and deletions (−).”

---

## 8. **Full Workflow Practice — Students Perform (5 minutes)**

Let students tries with another example,
Give the following command sequence as a drill:

1. “Edit any file.”
2. “Run `git status`.”
3. “Stage using `git add <file>`.”
4. “Check with `git diff --staged`.”
5. “Commit with a meaningful message.”
6. “View your commit using `git log --oneline`.”

Walk around (or observe screens) while they perform.
