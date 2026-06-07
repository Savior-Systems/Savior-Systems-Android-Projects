# Workflow: 04. Cross-App Interlinking Audit

This workflow ensures that all apps in the portfolio are properly cross-referenced and that the master README stays in sync.

---

## Trigger Conditions
Run this workflow when:
- A new app's documentation is completed.
- The master `README.md` needs updating.
- A batch of apps has been completed and needs verification.

## Steps

### Step 1: Verify Master README
- Open the root `README.md`.
- Ensure every app folder with completed documentation has a row in the master table.
- Verify all links in the master README use relative paths and point to the correct `README.md` inside each app folder.

### Step 2: Verify Per-App READMEs
- For each completed app, open its `README.md`.
- Ensure the documentation directory table has 13 rows linking to files `01` through `13`.
- Ensure the GCP & Firebase section references `hopeful-breaker-426606-h9`.
- Ensure the App Icon is embedded with a relative path.

### Step 3: Cross-Reference Color Uniqueness
- Open `context/portfolio-context.md`.
- Verify that no two apps share the same primary hex color.
- If a conflict is found, update the newer app's `02.UI-UX-DESIGN-SYSTEM.md`.

### Step 4: Link Integrity Check
Run a grep across the entire repository for any remaining `file:///` absolute links:
```bash
grep -rn "file:///" --include="*.md" .
```
If any results are found, fix them immediately using a Python script to convert to relative paths.

### Step 5: Commit Fixes
If any fixes were made, commit with: `fix: interlinking audit corrections`.
