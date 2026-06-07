# Workflow: 03. Batch Documentation Sprint

This workflow is optimized for the aggressive 30-day documentation sprint where multiple apps are documented in sequence.

---

## Pre-Sprint Setup
1. Verify the master `README.md` at the repository root is current.
2. Verify `context/portfolio-context.md` color matrix is populated for all target apps.
3. Ensure git is clean: `git status` shows no uncommitted changes.

## Per-App Execution Loop (Repeat for each app)

### Step 1: Research (5–10 min)
- Run `search_web` for the app's category, architecture patterns, and ASO keywords.
- Identify the unique selling proposition (USP) that differentiates it from competitors.
- Identify any special offline calculation engines, sensors, or APIs required.

### Step 2: Generate Blueprints (15–25 min)
- Follow `workflows/01-blueprint-generation.md` exactly.
- Write all 14 files in 3 batches (4 + 4 + 6).
- Generate the premium app icon using the `generate_image` tool.

### Step 3: Quality Gate (2 min)
- Verify all 14 files exist.
- Verify the README has 13 linked rows with relative paths.
- Verify the icon PNG is saved in the app's directory.
- Verify no `file:///` absolute paths exist.

### Step 4: Git Commit & Push (1 min)
- `git add -A`
- `git commit -m "feat(XX-app-name): Complete deep research & full documentation suite with premium app icon"`
- `git push origin main`

### Step 5: Update Backlog (1 min)
- Mark the app as `[x]` in `tasks/backlog.md`.

---

## Sprint Velocity Targets
- **Target**: 3–4 apps per day during aggressive sprints.
- **Throughput**: ~20–30 minutes per app (research + writing + git).
- **Goal**: All 30 apps documented within 10 working days.
