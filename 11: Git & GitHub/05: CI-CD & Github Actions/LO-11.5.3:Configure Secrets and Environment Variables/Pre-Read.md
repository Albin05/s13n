Modern applications rarely work in isolation. They depend on configuration values that change across environments and must be handled carefully. This topic explains **why configuration must be separated from code** and how secure handling of such values fits into automated workflows.

---

## **1. Why Configuration Cannot Live in Code**

In real projects, code is shared, reviewed, and stored publicly or semi-publicly.
If sensitive or environment-specific values are embedded directly in files, they become difficult to protect and easy to misuse.

Conceptually:

- Code should describe _logic_
- Configuration should describe _context_
- Security should not depend on developers remembering what to hide

Separating configuration from code is a foundational industry practice.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/sample/secrets-vs-config-overview.png)

---

## **2. Two Types of Configuration Values**

Not all configuration values carry the same risk.
This leads to a clear distinction between **general configuration** and **sensitive data**.

Some values simply control behavior, while others grant access.
Treating them the same would either reduce security or reduce flexibility.

This distinction exists to answer one question clearly:

> _What happens if this value is accidentally exposed?_

---

## **3. Environment Variables: Controlling Behavior**

Environment variables represent **non-sensitive settings** that influence how an application runs.

Conceptually, they are used to:

- Switch between environments
- Enable or disable features
- Adjust logging or debugging behavior

They are allowed to be visible because exposure does not create direct harm.

---

## **4. Secrets: Protecting Access**

Secrets represent **credentials and keys** that must remain confidential.

Their defining characteristics are:

- Stored securely
- Hidden from logs
- Never exposed in plain text

Secrets exist to ensure that even if automation logs are visible, **access is never leaked**.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/sample/secret-masking-ci.png)

---

## **5. Role of Secrets & Variables in Automation**

Secrets and environment variables are not part of application logic.
They are injected **only at runtime**, when automation executes.

This allows:

- The same code to run in multiple environments
- Secure values to change without new commits
- Pipelines to remain reusable and safe

This separation is a key marker of **professional CI/CD design**.

---

## **6. Scope and Visibility as a Design Choice**

Configuration values can apply at different levels:

- Entire automation flow
- A specific automated job
- A single execution step

This layered visibility allows precise control, preventing unnecessary exposure while keeping workflows flexible.

---

## **7. Automation Does Not Self-Update**

One important mental model:

- Automation runs with the configuration available _at the time it starts_
- Changes to configuration do not affect past executions

This reinforces the idea that configuration and execution are **deliberately decoupled**.

---

## **8. Security as a Habit, Not a Feature**

Most security failures come from convenience, not complexity.

Professional environments assume:

- Logs may be read
- Repositories may be shared
- Mistakes will happen

Secrets and environment variables exist to **reduce the impact of human error**, not to rely on perfect behavior.

---

### **Mental Model to Carry Forward**

Code should be reusable.
Configuration should be flexible.
Secrets should be invisible.
