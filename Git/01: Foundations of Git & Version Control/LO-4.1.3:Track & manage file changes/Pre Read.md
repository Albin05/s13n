Git manages project changes through a clear flow of how files move between different areas before becoming part of the project history.

---

## **1. The Three-Area Model**

Git organizes files across three logical areas that represent their state.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/07d42e41-6c25-4883-8b81-04fcc2c94420/UMQizQ3zQGscDIJV.png)

**Working Directory**
Where files are created, edited, or deleted. Changes here are not tracked until staged.

**Staging Area (Index)**
A preparation zone that collects selected changes. This allows forming intentional and clean snapshots.

**Local Repository**
Stores committed snapshots permanently with unique commit IDs.

---

## **2. Checking File States**

`git status` displays which files are modified, which are staged, and which remain unstaged.
Example (conceptually):

- A modified file may appear under “changes not staged.”
- A newly added file may appear under “changes to be committed.”

---

## **3. Staging Changes**

`git add` moves selected files into the staging area.
Examples:

- Staging a single file
- Staging multiple files
- Staging all tracked and modified files

Staging allows grouping related updates into meaningful commits.

---

## **4. Creating Commits**

A commit acts as a snapshot of all staged changes.
Commit messages typically start with verbs such as _Add_, _Fix_, _Update_, _Remove_ and describe the purpose of the change clearly.
Example messages:

- Add navbar component
- Fix validation issue

---

## **5. Viewing Project History**

`git log` lists past commits with details like ID, author, and timestamp.
A condensed format shows just commit IDs and short messages to provide a quick view of progression.

---

## **6. Comparing Versions**

`git diff` highlights differences between two states:

- Working directory vs staging area
- Staging area vs last commit
- One commit vs another

Conceptually, added lines appear with a plus symbol and removed lines with a minus symbol, allowing careful review before saving work.

---

## **7. Workflow Overview**

A typical flow involves:

1. Editing files
2. Checking their state
3. Staging selected updates
4. Reviewing staged content
5. Creating a commit
6. Inspecting history afterward

---
