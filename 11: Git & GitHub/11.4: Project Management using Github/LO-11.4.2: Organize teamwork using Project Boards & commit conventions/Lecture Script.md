## 1. **Connect With the Previous Topic (3 minutes)**

- “Open the same GitHub repository we used in the last session.”
- “Keep the **Issues tab** open on one side.”

**Say clearly:**

> “In the previous session, we learned how to **define work**:
>
> - Issues tell us _what_ to do
> - Assignees tell us _who_ will do it
> - Labels tell us _what type_ of work
> - Milestones tell us _by when_”

Pause and ask:

> “But one question still remains —
> **What is happening right now?**”

---

**Explain the gap:**

- Issues alone do not show:

  - What is actively being worked on
  - What is blocked
  - What is completed visually

**Transition statement:**

> “This is where **Project Boards** and **commit conventions** come in.
> They help us **visualize work** and **maintain clean history**.”

---

## 2. **Introduce Project Boards (4 minutes)**

### **Show the Projects Tab (Do not create yet)**

- Click **Projects** tab in the repository.

**Explain verbally:**

> “A Project Board is a **visual tracker** for issues and pull requests.”

> “Instead of lists, we see **columns** that represent workflow stages.”

---

### Typical Columns (Explain conceptually)

- To Do
- In Progress
- Done

**Say:**

> “Each card you see here is either:
>
> - an Issue
> - or a Pull Request”

---

## 3. **Explain Kanban Workflow (4 minutes)**

Before clicking anything, explain:

> “GitHub boards follow **Kanban** — the same workflow used in industry.”

Explain Kanban simply:

- Visualize work
- Limit work in progress
- Move tasks step by step

**Mapping to GitHub:**

- Issue created → **To Do**
- Work starts → **In Progress**
- Work completed & closed → **Done**

---

**Emphasize:**

> “Movement of cards represents **real development flow**, not theory.”

---

## 4. **Create a Project Board Live (6 minutes)**

### **Step 1 — Create New Project**

- Click **New Project**
- Choose **Board**

**Say while doing:**

> “We always choose **Board** for Kanban-style tracking.”

---

### **Step 2 — Name the Board**

- Name: `Sprint 1 – Project Board`
- Create project

---

### **Step 3 — Create Columns**

Ensure these columns exist:

- To Do
- In Progress
- Done

**Say clearly:**

> “This board becomes the **control center** of our project.”

---

## 5. **Add Issues to the Board (5 minutes)**

### **Method 1 — Add from Board**

- Click **Add item**
- Search for an existing issue
- Add it to **To Do**

---

### **Method 2 — Add from Issue**

- Open an issue
- Assign it to the project

**Explain while showing:**

> “Issues and boards are **two views of the same data**.”

---

## 6. **Manage Work Using the Board (5 minutes)**

### **Live Demonstration**

- Drag an issue from:

  - **To Do → In Progress**

**Say:**

> “This indicates someone has **started working**.”

---

### **Move to Done**

- Close the issue
- Show that the card moves to **Done**

**Explain:**

> “Issue status and board status are synced automatically.”

---

📌 Emphasize discipline:

> “If you don’t move cards,
> your board becomes useless.”

---

## 7. **Introduce Pull Requests (PRs) (5 minutes)**

### **Explain Before Showing**

> “A Pull Request is a request to **merge code changes** into another branch.”

Explain why PRs exist:

- Code review
- Team discussion
- Quality control

---

### **Show Pull Requests Tab**

- Open **Pull Requests**

**Say:**

> “In professional teams, code **never goes directly to main**.”

---

## 8. **Link Issues to Pull Requests (6 minutes)**

### **Explain the Problem First**

> “If planning and coding are separate, tracking breaks.”

---

### **Show Linking Syntax (Explain Slowly)**

In PR description, type:

```bash
Fixes #12
```

or

```bash
Closes #5
```

---

### **Explain What Happens**

- PR is linked to the issue
- On merge:

  - Issue closes automatically
  - Board updates
  - Milestone progress updates

**Say clearly:**

> “This is automation working _for_ you.”

---

## 9. **Why Commit Messages Matter (4 minutes)**

### **Open Git Log (or show screenshot)**

**Say:**

> “Commits are not just code snapshots.
> They are **project documentation**.”

---

### **Show Bad Example**

- `final commit`
- `changes`
- `update`

**Explain:**

> “These messages are useless in real projects.”

---

## 10. **Introduce Conventional Commits (5 minutes)**

### **Explain Conceptually**

> “Conventional Commits is a **standard format** for commit messages.”

Explain benefits:

- Readability
- Consistency
- Automation readiness

---

### **Show Format**

```
<type>(optional scope): short description
```

---

### **Show Examples Live**

```bash
feat(auth): add login validation
fix(ui): fix button alignment
docs: update README
```

**Explain each part slowly.**

---

## 11. **Commit Types Explanation (4 minutes)**

Explain the table verbally:

- feat → new functionality
- fix → bug fix
- refactor → internal code changes
- docs → documentation
- chore → maintenance

**Say:**

> “From commit history alone,
> I should understand what changed.”

---

## 12. **Link Commits to Issues (4 minutes)**

### **Show Example Commit Message**

```bash
fix(auth): validate email format (#12)
```

Explain:

- `#12` links commit to issue
- Creates traceability
- Helps during debugging and audits

---
