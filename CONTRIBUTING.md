# Savior Systems: Contributing Guidelines

Welcome to Savior Systems' Android App Portfolio project. To maintain order across all 30 applications, developers must adhere to the following workflow instructions:

---

## 1. Environment Setup

*   **IDE**: Android Studio Koala (or latest stable release).
*   **JDK Version**: Java 17.
*   **Android SDK**: Target SDK 35, Build Tools 35.0.0.

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
    *   New features: `feat/app-name/feature-description`
    *   Fixes: `fix/app-name/bug-description`
    *   Docs: `docs/app-name/update-type`
2.  **Commit Messages**: Use Conventional Commits formatting:
    *   `feat(focuspulse): add custom interval picker`
    *   `fix(cgpa): adjust GPA weights calculation`
    *   `docs(waterlog): modify ASO keywords list`

---

## 3. Pull Request Standards

Before submitting a Pull Request (PR) to merge changes into the `main` branch, ensure:

1.  The project builds with zero errors.
2.  The `MASTER-CHECKLIST.md` checks have been performed and passed.
3.  The changes correspond directly to an assigned app task folder.
