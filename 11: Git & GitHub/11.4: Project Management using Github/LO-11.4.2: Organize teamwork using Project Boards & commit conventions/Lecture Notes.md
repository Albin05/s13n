## 1. Connecting With the Previous Topic

In the previous topic, we learned how to:

- Break work into **Issues**
- Assign responsibility using **Assignees**
- Organize work using **Labels**
- Track progress using **Milestones**

However, those tools answer _what_ work exists and _who_ owns it.

They do **not clearly show**:

- What work is currently being done
- What is pending
- What is already completed

This gap is filled by **Project Boards** and **commit conventions**, which help teams **visualize workflow and maintain clean project history**.

---

## 2. What Are Project Boards?

A **Project Board** is a **visual way to track the status of issues and pull requests** using columns.

GitHub Project Boards follow the **Kanban methodology**, which organizes work into stages.

Typical columns:

- **To Do** – Work not started
- **In Progress** – Work currently being done
- **Done** – Completed work

Each card on the board represents:

- An **Issue**
- Or a **Pull Request (PR)**

---

## 3. Why Use Project Boards?

Project boards help teams:

- See the current state of the project at a glance
- Avoid confusion about task status
- Prevent multiple people working on the same task unknowingly
- Coordinate teamwork visually

Unlike issues (which are lists), boards show **workflow movement**.

---

## 4. Kanban Workflow in GitHub

Kanban is a workflow method based on:

- Limiting work in progress
- Visualizing flow
- Moving tasks step-by-step

In GitHub:

- Issues start in **To Do**
- Move to **In Progress** when work begins
- Move to **Done** once completed and closed

This mirrors how real development teams work.

---

## 5. Creating a Project Board in GitHub

### Steps to Create a Project Board

1. Open your **GitHub repository**
2. Click the **Projects** tab
3. Click **New Project**
4. Choose **Board** (Kanban-style)
5. Give the project a name
6. Create default columns:

   - To Do
   - In Progress
   - Done

Once created, the board becomes the **visual control center** of the project.

---

## 6. Adding Issues to the Project Board

Issues created earlier can be added as cards.

### How to Add Issues to the Board

**Method 1: From the board**

- Click **Add item**
- Search and select existing issues

**Method 2: From the issue**

- Open an issue
- Assign it to a project

Each issue now appears as a card that can be moved across columns.

---

## 7. Managing Work Using the Board

As work progresses:

- Move issue cards from **To Do → In Progress**
- Move to **Done** when the work is completed

This movement reflects **real-time progress**.

📌 Important note:

- Closing an issue often moves it to **Done**
- The board stays in sync with issue status

---

## 8. Pull Requests (PRs) and Team Collaboration

A **Pull Request (PR)** is a request to merge code changes into the main branch.

PRs are important because:

- Code is reviewed before merging
- Team members can comment and suggest changes
- Quality and standards are maintained

PRs can also be:

- Linked to issues
- Tracked on project boards

---

## 9. Linking Issues to Pull Requests

Linking issues and PRs connects **planning** with **execution**.

### How to Link an Issue to a PR

When creating a PR, mention the issue number in the PR description using keywords:

```
Fixes #12
Closes #5
Resolves #20
```

What happens:

- The PR gets linked to the issue
- When the PR is merged, the issue is **automatically closed**
- Milestone and board progress update automatically

This creates **clean automation**.

---

## 10. Why Commit Messages Matter

Commits are not just code snapshots; they are **documentation of changes**.

Poor commit messages:

- Are unclear
- Break automation
- Make history hard to read

Professional teams follow **commit conventions** to keep history clean and meaningful.

---

## 11. What Are Conventional Commits?

**Conventional Commits** is a standardized format for writing commit messages.

It helps:

- Humans understand changes easily
- Tools automate versioning and changelogs
- Maintain consistency across the team

---

## 12. Conventional Commit Format

Basic structure:

```
<type>(optional scope): short description
```

Example:

```
feat(auth): add login validation
fix(ui): resolve button alignment issue
docs: update README
```

---

## 13. Common Commit Types

| Type     | Meaning                  |
| -------- | ------------------------ |
| feat     | New feature              |
| fix      | Bug fix                  |
| docs     | Documentation change     |
| style    | Formatting changes       |
| refactor | Code restructuring       |
| test     | Adding or updating tests |
| chore    | Maintenance tasks        |

---

## 14. Linking Commits to Issues

Commits can also reference issues.

Example:

```
fix(auth): validate email format (#12)
```

This:

- Links the commit to the issue
- Creates traceability between code and tasks

---

## 15. Benefits of Commit Conventions

Using conventions helps:

- Read commit history quickly
- Identify bug fixes vs features
- Enable automation tools later
- Maintain professional-quality repositories

For student projects, this builds **industry-ready habits**.

---

## 16. End-to-End Team Workflow (Putting Everything Together)

1. Create issues for tasks
2. Assign labels, assignees, milestones
3. Add issues to the project board
4. Move issues across Kanban columns
5. Create PRs linked to issues
6. Use conventional commits
7. Merge PRs → issues close automatically

This forms a **complete, professional workflow**.

---
