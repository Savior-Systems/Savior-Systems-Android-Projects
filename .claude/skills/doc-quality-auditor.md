# Skill: Documentation Quality Auditor

## Purpose
Performs a comprehensive quality audit on a completed app's 14-file documentation suite, identifying missing sections, placeholder text, broken links, and structural violations.

## When to Use
- After completing the 14 files for any app.
- Before committing and pushing documentation to `main`.
- When reviewing an older app's docs for staleness.

## Audit Checklist

### Structural Checks
1. ☐ All 14 files exist (`01.PRD` through `13.BACKLOG` + `README.md`).
2. ☐ Each file has a top-level `# Title` heading.
3. ☐ Each file has at least 30 lines of content (not just headers).
4. ☐ `README.md` has a documentation directory table with exactly 13 rows.
5. ☐ An app icon `.png` file exists in the directory.

### Content Checks
6. ☐ `01.PRD` has at least one named user persona.
7. ☐ `02.UI-UX` defines both Light and Dark mode palettes with hex codes.
8. ☐ `03.FUNCTIONAL-FLOWS` contains a Mermaid diagram (` ```mermaid `).
9. ☐ `04.TECHNICAL-ARCHITECTURE` contains a directory tree and at least one Kotlin code block.
10. ☐ `05.DATABASE-SCHEMA` has table definitions with column types and constraints.
11. ☐ `06.ADMOB` defines an interstitial frequency cap.
12. ☐ `07.ASO` has title ≤ 30 chars and short description ≤ 80 chars.
13. ☐ `08.PLAY-POLICY` has a permissions audit listing both Required and STRIPPED permissions.
14. ☐ `09.TESTING` has at least 3 manual QA edge cases.
15. ☐ `10.TRANSLATIONS` has a complete `strings.xml` block.
16. ☐ `11.GRAPHIC-ASSETS` defines Foreground, Background, and Monochrome icon layers.
17. ☐ `12.LOGGING` defines at least 4 custom Firebase events.
18. ☐ `13.BACKLOG` has at least 5 phases with `- [ ]` items and a V2 section.

### Link & Path Checks
19. ☐ Zero `file:///` absolute paths in any `.md` file.
20. ☐ Zero `[TODO]`, `[PLACEHOLDER]`, or `$(@{...})` template variables.
21. ☐ README icon embed uses relative path.

## Execution Method
Use `grep_search` to scan for forbidden patterns (`file:///`, `TODO`, `PLACEHOLDER`).  
Use `list_dir` to verify file counts.  
Use `view_file` on each file to verify content length and key structural elements.

## Output
Generate a markdown report:
```
## Audit Report: [App Name]

| Check | Status | Notes |
| :--- | :--- | :--- |
| 14 files exist | ✅ | All present |
| Mermaid diagram in 03 | ✅ | Found |
| file:/// links | ❌ | 2 found in README.md |
```
