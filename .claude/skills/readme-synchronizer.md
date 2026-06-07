# Skill: Master README Synchronizer

## Purpose
Keeps the root-level `README.md` of the entire repository in sync with the current state of all 30 app directories.

## When to Use
- After completing documentation for a new app.
- After renaming or restructuring an app directory.
- Periodically during the sprint to ensure accuracy.

## Execution Steps

### Step 1: Scan All Directories
Use `list_dir` on the root of the repository to identify all app directories (numbered `01.` through `30.`).

### Step 2: Determine Status
For each directory, determine the documentation status:
- **✅ Complete**: 14 `.md` files + at least one `.png` icon.
- **🔄 In Progress**: Between 1 and 13 `.md` files.
- **📋 Template Only**: Only the initial template files (e.g., a placeholder README).

### Step 3: Update Root README Table
Locate the project listing table in the root `README.md`. Update each row to reflect:
- Current documentation status.
- Correct relative link to the app's `README.md`.
- App's primary color hex and category.

### Step 4: Update Counters
Update any summary counters (e.g., "Documentation Progress: 6/30 apps complete").

### Step 5: Commit
If changes were made, commit with: `docs: sync root README with current project status`.

## Agent Instructions
1. Always scan live — never rely on cached status.
2. Preserve any custom sections in the root README (like the GCP project table).
3. Only update rows that have actually changed.
