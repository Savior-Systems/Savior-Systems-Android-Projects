# Prompt: Generate GitHub Issues from Backlog

Use this prompt to convert a completed app's `13.BACKLOG-TASKS.md` into actionable GitHub Issues.

---

## Prompt

```
Act as a Technical Project Manager.

Parse the `13.BACKLOG-TASKS.md` file for App [APP_NAME] located in [APP_DIRECTORY].

Generate GitHub Issue templates in Markdown for each phase. Each issue must include:

1. **Title**: `[App XX] Phase Y: <Phase Name>` (e.g., `[App 06] Phase 1: Foundation & Data Layer`)
2. **Labels**: `enhancement`, `app-XX`, `phase-Y`
3. **Body**:
   - **Description**: A 2-sentence summary of what this phase accomplishes.
   - **Tasks** (checkbox list): Every `- [ ]` item from the phase.
   - **Definition of Done**:
     - All tasks checked off.
     - Code compiles without errors.
     - Unit tests for this phase pass.
   - **Dependencies**: List any phases that must be completed first.
   - **References**: Link to relevant blueprint documents (e.g., `04.TECHNICAL-ARCHITECTURE.md` for Phase 1).

Output each issue as a separate, copy-pasteable Markdown block separated by `---`.
```
