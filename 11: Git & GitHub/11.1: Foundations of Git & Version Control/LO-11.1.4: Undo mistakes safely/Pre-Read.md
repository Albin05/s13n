Working with Git involves making edits, staging them, and committing them. Mistakes can occur at any of these stages, and Git provides safe ways to undo or adjust those changes without losing work. The preread introduces how Git handles undo operations in the working directory, staging area, and repository.

---

## **1. Undoing Changes in the Working Directory**

The working directory contains uncommitted edits. These changes can be reverted back to the last committed version.
Concept example:

- A configuration file was edited incorrectly and needs to be reset
- Multiple files were changed accidentally and should be restored to a clean state

Restoring affects only uncommitted changes and does not touch the staging area.

---

## **2. Removing Files from the Staging Area**

Staging determines what goes into the next commit. If the wrong files were staged, they can be safely moved back to the working directory while keeping their edits intact.
Concept examples:

- A large log file was staged unintentionally
- Several files were added to staging, but only one of them should remain
- A clean staging area is needed before grouping changes logically

Unstaging affects only the staging area and preserves file modifications.

---

## **3. Modifying the Most Recent Commit**

Sometimes a commit contains a mistake—either in its message or its content. Git allows updating the most recent commit before it is shared.
Concept examples:

- A spelling error in the commit message
- A missing file that should have been part of the last commit
- A small correction that fits the previous change

Amending rewrites the last commit and updates its ID, but is safe as long as the commit has not been pushed.

---

## **4. Undoing Based on the File Lifecycle**

Actions differ depending on where the file currently sits:

- Working directory: discard changes
- Staging area: unstage changes
- Repository: adjust latest commit

This lifecycle helps determine the correct command for the correct situation.

---

## **5. Common Mistake Scenarios**

Concept examples covered in the session include:

1. Changes made incorrectly and needing discard
2. Files staged unintentionally
3. Missing updates that belong in the previous commit
4. Incorrect commit messages
5. Reviewing differences before undoing anything

These situations illustrate how undo operations keep the workflow safe and controlled.

---
