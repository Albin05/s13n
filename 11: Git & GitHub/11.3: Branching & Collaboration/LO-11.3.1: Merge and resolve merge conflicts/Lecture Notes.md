## **1. Merge — How Approved Changes Enter the Main Codebase**

After a Pull Request is raised and reviewed, the final step in the collaboration process is **merging**. A merge is the operation through which approved changes from one branch are officially integrated into another branch, most commonly into the `main` branch.

At this stage, development work is already complete, code has been reviewed, and decisions have been recorded in the Pull Request discussion. Merging is therefore not about development, but about **acceptance and integration**.

From Git’s perspective, merging means combining the **commit history** of two branches. It does not simply copy files from one branch into another. Instead, it records how two independent lines of work come together, ensuring that the project history accurately reflects the evolution of the codebase.

In modern workflows, merges are rarely performed directly from the command line without context. Instead, they are usually executed through a Pull Request on the remote platform. This ensures that:

- Only reviewed and approved code is merged
- Access control rules are respected
- The merge action is auditable and traceable

A merge represents a **decision point**. By merging a Pull Request, the team confirms that the proposed changes meet quality standards, align with project goals, and are ready to become part of the shared codebase.

It is important to understand that merging can behave differently depending on the state of the branches involved. If no parallel changes occurred, Git may integrate changes in a straightforward way. If both branches evolved independently, Git must reconcile differences. When Git cannot do this automatically, it raises a merge conflict, which requires manual resolution.

At a conceptual level, merging serves three purposes:

- It integrates completed work into the main line of development
- It preserves a record of collaboration and decision-making
- It marks a stable checkpoint in the project history

Understanding what a merge represents conceptually is essential before learning how conflicts are detected and resolved.

---

## **2. What Is a Merge Conflict**

A merge conflict occurs when **two branches modify the same part of the same file in incompatible ways**, and Git cannot decide which version is correct.

Git is intentionally conservative.
If there is any ambiguity, it refuses to guess.

A conflict means:

- Git detected overlapping changes
- Human intervention is required
- The merge is paused until resolved

---

## **3. Common Causes of Merge Conflicts**

Conflicts usually arise due to timing and parallel work.

They commonly occur when:

- Two branches edit the same lines of a file
- One branch deletes a file while another modifies it
- A file is renamed in one branch and edited in another
- Long-running branches fall far behind `main`
- Large refactors overlap with feature development

The longer branches stay unmerged, the higher the probability of conflicts.

---

## **4. What Happens Internally When a Conflict Occurs**

When Git encounters a conflict:

- It pauses the merge operation
- It marks the conflicted files
- It inserts **conflict markers** into those files
- It requires manual resolution before proceeding

The repository enters a **conflicted state**, where normal commits are blocked until the conflict is resolved or the merge is aborted.

---

## **5. Understanding Conflict Markers**

When a conflict occurs, Git modifies the file to show both versions of the conflicting code.

A conflicted file contains markers like:

![Conflict Indicator](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/29216d01-1968-4352-9d6f-606c74dc553d/vkbLoaViDCX0pzbJ.png)

Meaning:

- `<<<<<<< HEAD` → current branch version
- `=======` → separator
- `>>>>>>> branch-name` → incoming branch version

These markers are **not valid code** and must be removed after deciding which changes to keep.

---

## **6. Resolving Merge Conflicts Using CLI (Conceptual Flow)**

When resolving conflicts via the command line, the responsibility lies entirely with the developer.

The conceptual steps are:

1. Identify which files are in conflict
2. Open the conflicted files manually
3. Review both versions carefully
4. Decide what the final correct code should be
5. Remove conflict markers
6. Save the file
7. Mark the conflict as resolved by staging the file
8. Complete the merge with a commit

At no point should conflict markers remain in the final code.

---

## **7. Resolving Merge Conflicts Using GitHub UI**

GitHub provides a web-based interface to resolve conflicts directly inside a Pull Request.

This approach is useful when:

- Conflicts are small
- Changes are easy to review
- You want a visual comparison

The GitHub UI:

- Shows both versions side by side
- Allows choosing or editing the final content
- Automatically removes conflict markers
- Commits the resolution to the branch

Behind the scenes, GitHub performs the same steps Git would locally.

---

## **8. Choosing Between CLI and GitHub UI**

Both approaches achieve the same result, but the choice depends on context.

CLI resolution is preferred when:

- Conflicts are complex
- Multiple files are involved
- Local testing is required

GitHub UI resolution is suitable when:

- Conflicts are small
- Changes are straightforward
- Quick resolution is needed

Professional teams often use both depending on the situation.

---

## **9. Testing After Conflict Resolution**

Resolving a conflict is not complete until the code is **validated**.

After resolution:

- The application should compile or run
- Tests (if present) should pass
- A quick functional check should be performed

Conflicts often introduce subtle bugs if resolved carelessly. Testing ensures correctness before final integration.

---

## **10. Finalizing the Merge**

Once conflicts are resolved and validated:

- The merge process is completed
- The Pull Request can be merged
- The main branch receives the updated code
- All collaborators can synchronize the changes

Only after successful resolution and testing should the merge be finalized.

---

## **11. Common Mistakes During Conflict Resolution**

Some frequent errors include:

- Leaving conflict markers in files
- Accidentally deleting required logic
- Resolving conflicts without understanding the code
- Skipping testing after resolution

Conflict resolution is a **decision-making process**, not a mechanical task.

---
