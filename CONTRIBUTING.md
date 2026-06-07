# Savior Systems: Contributing Guidelines

Welcome to Savior Systems' Android App Portfolio project. To maintain order and high release velocities across all 30 applications, developers must adhere to the following setup, coding, and submission guidelines.

---

## 📂 Navigation Index
Before committing code, familiarize yourself with these master references:
*   [Main README](README.md) — Portfolio-level overview and list of projects.
*   [Developer Guide](DEVELOPER-GUIDE.md) — Technical tech stack specifications and project setup steps.
*   [Master Submission Checklist](MASTER-CHECKLIST.md) — Pre-flight requirements every app must pass before store submission.
*   [AI Agent Operating System](AI-AGENT-OPERATING-SYSTEM.md) — Context rules and prompt guidelines for AI coding helpers.

---

## 1. Environment Setup

*   **IDE**: Android Studio Meerkat (or latest stable release).
*   **JDK Version**: Java 17.
*   **Android SDK**: Target SDK 35, Build Tools 35.0.0.
*   **Version Control**: Git.

For detailed setup instructions, including gradle configuration files and Gradle Version Catalogs, review [Section 3 of the Developer Guide](DEVELOPER-GUIDE.md#3-project-setup-for-each-app).

---

## 2. Git Workflow

We use a standard branch isolation strategy:

```
                  ┌──────────────────────┐
                  │         main         │
                  └──────────┬───────────┘
                             │ (branch)
                             ▼
                  ┌──────────────────────┐
                  │    feat/feature-name │
                  └──────────┬───────────┘
                             │ (PR review)
                             ▼
                  ┌──────────────────────┐
                  │         main         │
                  └──────────────────────┘
```

1.  **Branch Conventions**:
    *   New features: `feat/app-name/feature-description` (e.g. `feat/12-todo/swipe-gestures`)
    *   Fixes: `fix/app-name/bug-description`
    *   Docs: `docs/app-name/update-type`
2.  **Commit Messages**: Use Conventional Commits formatting:
    *   `feat(focuspulse): add custom interval picker`
    *   `fix(cgpa): adjust GPA weights calculation`
    *   `docs(waterlog): modify ASO keywords list`

---

## 3. Pull Request Standards

Before submitting a Pull Request (PR) to merge changes into the `main` branch, you must verify:

1.  The project builds locally with zero errors.
2.  The validation checks listed in the [Master Submission Checklist](MASTER-CHECKLIST.md) have been performed and marked as passed.
3.  The changes correspond directly to the assigned app task folder (e.g., `12. Minimalist To-Do/`).
4.  No absolute paths (`file:///`) are included in any documentation or code blocks. Always use relative path linking.
