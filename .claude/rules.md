# Savior Systems Coding Rules

- **Zero Unchecked Permissions**: Any permission requests must be documented in `11-privacy-policy-data-safety.md`. Do not add permissions in `AndroidManifest.xml` without architectural review.
- **Unique Style Schemes**: Base themes must use unique accent and background colors across different apps. Never reuse a single color file layout without changing values.
- **Compose Preview Support**: Every composable screen must define a `@Preview` composable parameter.
- **Coroutines Best Practices**: Run database actions on `Dispatchers.IO` and UI updates on `Dispatchers.Main`. Avoid custom thread blocks.
- **Offline First**: All user actions (like adding items, modifying lists) must execute locally first in Room/SQLite, with optional deferred synchronization.
