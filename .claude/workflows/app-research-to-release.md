# Workflow: App Research to Release

This workflow guides the lifecycle of a single portfolio app:

```mermaid
graph TD
    A[01 Market ASO Docs] --> B[03 Core System Design]
    B --> C[07 Implementation plan]
    C --> D[Compose UI Screens]
    D --> E[AdMob Hook Injection]
    E --> F[Verification & Policy QA]
    F --> G[Play Console Submission]
```

## Step 1: Pre-requisites Validation
- Verify Room databases have schema export disabled or migration histories initialized.
- Check that package names match active Google Play Console registrations.

## Step 2: Handoff Verification
- Run task tests matching `10-qa-test-plan.md`.
- Verify compilation succeeds.
