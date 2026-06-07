# Skill: Portfolio Progress Reporter

## Purpose
Generates a structured progress report showing the documentation status of all 30 apps in the portfolio.

## When to Use
- At the start or end of each working session.
- When the user asks "how far are we?" or "what's the status?"
- During the 30-day sprint to track velocity.

## Execution Steps

1. **Scan all 30 directories**: For each app folder (e.g., `01. FocusPulse Timer/`), check if the following files exist:
   - All 13 numbered markdown files (`01.PRD-REQUIREMENTS.md` through `13.BACKLOG-TASKS.md`)
   - `README.md`
   - At least one `.png` icon file

2. **Calculate completion**: 
   - 14/14 files + icon = ✅ Complete
   - 1-13 files = 🔄 Partial (X/14)
   - 0 files (only template) = ⬜ Not Started

3. **Output**: Generate a markdown table with columns:
   - App #
   - App Name
   - Status (✅/🔄/⬜)
   - Files Count (X/14)
   - Icon (✅/❌)

4. **Velocity Metrics**:
   - Total completed: X/30
   - Completion percentage: X%
   - Estimated days remaining at current velocity

## Agent Instructions
Run this skill using file system tools (`list_dir` on each directory) to count files. Do NOT rely on cached state — always scan live.
