# Guide: The 14-File Blueprint Standard

This guide explains the exact purpose, format, and quality expectations for every document generated in a Savior Systems app directory.

---

## The 14 Required Files

| # | Filename | Purpose | Key Quality Checks |
| :--- | :--- | :--- | :--- |
| 01 | `01.PRD-REQUIREMENTS.md` | Product vision, user personas, feature list, KPIs, and success metrics. | Must have at least 2 named personas. Features must map to user stories. |
| 02 | `02.UI-UX-DESIGN-SYSTEM.md` | Color palette (with hex codes), typography rules, component tokens, animation specs. | Must define both Light and Dark mode palettes. Must specify at least 2 micro-animations. |
| 03 | `03.FUNCTIONAL-FLOWS.md` | Mermaid navigation diagram, screen transition map, state management rules. | Must include a Mermaid `graph TD` diagram. Must cover edge cases (e.g., empty states, errors). |
| 04 | `04.TECHNICAL-ARCHITECTURE.md` | Directory tree, MVVM layer descriptions, key engine logic (with Kotlin code samples). | Must show the full package structure. Must include at least one Kotlin code block. |
| 05 | `05.DATABASE-SCHEMA.md` | Room entity schemas, DAO queries (with Flow return types), DataStore keys. | Must define all columns with types and constraints. Must include `Flow`-based queries. |
| 06 | `06.ADMOB-MONETIZATION-MAP.md` | Ad format strategy, placement rules, frequency caps, and content category blocks. | Must define strict interstitial cooldown timers. Must list zero-ad zones. |
| 07 | `07.ASO-PLAY-STORE-LISTING.md` | App title (≤30 chars), short description (≤80 chars), full description, keyword matrix. | Must have a keyword table with Primary and Secondary columns. |
| 08 | `08.PLAY-POLICY-SAFETY.md` | Permissions audit (Required vs STRIPPED), Data Safety form responses, alarm justification. | Must explicitly list permissions NOT used with 🚫. Must have Data Safety table. |
| 09 | `09.TESTING-ASSURANCE-PLAN.md` | Unit test targets, integration tests, manual QA matrix, performance benchmarks. | Must cover at least 3 edge cases. Must define cold start time target. |
| 10 | `10.TRANSLATIONS-LOCALIZATION.md` | Full `strings.xml` dump, localization targets, unit/format conversion logic. | Must include the complete base `strings.xml`. Must list priority locales. |
| 11 | `11.GRAPHIC-ASSETS-MANIFEST.md` | Icon specs, adaptive icon layers, screenshot captions, feature graphic design. | Must define Foreground, Background, and Monochrome icon layers. |
| 12 | `12.LOGGING-ANALYTICS.md` | Custom Firebase events (with parameters), Crashlytics keys, strict PII rules. | Must define at least 4 custom events. Must have a "NEVER log" section. |
| 13 | `13.BACKLOG-TASKS.md` | Phased development checklist with `- [ ]` items grouped by weekly sprints. | Must have at least 5 phases. Must include a V2 Future Enhancements section. |
| 14 | `README.md` | Master index table linking to all 13 docs above, key differentiators, GCP SOP. | All links must be relative. Must include an App Icon embed. |

---

## Cross-Referencing Rules
- The README links to all 13 siblings using **relative paths** (e.g., `[PRD](01.PRD-REQUIREMENTS.md)`).
- The `11.GRAPHIC-ASSETS-MANIFEST.md` references the icon PNG using a relative path.
- Never use absolute `file:///` paths — they break on GitHub.

---

## Quality Gate Checklist (Before Committing)
1. ☐ All 14 files exist in the app's directory.
2. ☐ The README table has 13 linked rows.
3. ☐ A premium app icon PNG has been generated and saved.
4. ☐ No `file:///` absolute paths exist in any `.md` file.
5. ☐ No placeholder text like `[TODO]`, `[PLACEHOLDER]`, or `$(@{...})` remains.
6. ☐ The color palette in `02.UI-UX-DESIGN-SYSTEM.md` does not duplicate another app (check `context/portfolio-context.md`).
