# Skill: Dependency Version Checker

## Purpose
Checks that all dependency versions across the portfolio are up-to-date and consistent, preventing version drift that causes compilation failures.

## When to Use
- Before scaffolding a new project.
- Monthly maintenance sweep across all apps.
- When a user reports a dependency conflict.

## Canonical Version Source
The single source of truth for all dependency versions is `.claude/context/portfolio-context.md` under the "Reusable Library & SDK Versions" section.

## Check Process

### Step 1: Read Current Versions
Parse the version table from `context/portfolio-context.md`.

### Step 2: Search for Latest Versions
For each critical dependency, check the latest stable version:

| Dependency | Check URL |
| :--- | :--- |
| Kotlin | `https://kotlinlang.org/docs/releases.html` |
| Compose BOM | `https://developer.android.com/develop/ui/compose/bom/bom-mapping` |
| Hilt | `https://github.com/google/dagger/releases` |
| Room | `https://developer.android.com/jetpack/androidx/releases/room` |
| Firebase BOM | `https://firebase.google.com/support/release-notes/android` |
| Google Ads SDK | `https://developers.google.com/admob/android/rel-notes` |

### Step 3: Compare & Report
Generate a table showing:
```
| Dependency | Current | Latest | Status |
| :--- | :--- | :--- | :--- |
| Kotlin | 2.0.0 | 2.0.21 | ⚠️ Update Available |
| Compose BOM | 2024.06 | 2024.06 | ✅ Current |
```

### Step 4: Update Portfolio Context
If updates are available, update the version table in `context/portfolio-context.md`.

## Agent Instructions
Use `search_web` or `read_url_content` to check latest releases.
Only recommend updating to **stable** releases, never alpha/beta/RC.
