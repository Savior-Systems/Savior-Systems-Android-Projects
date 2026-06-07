# CLAUDE.md — Savior Systems AI Agent Boot Configuration

> **AUTO-SCAN DIRECTIVE**: Before executing ANY user request, the agent MUST scan the `.claude/` directory to load context, rules, skills, and gotchas. This is non-negotiable and must happen at the start of every new conversation or session.

---

## 🔄 Boot Sequence (Execute Before ANYTHING Else)

When a new session starts or the agent is invoked for the first time, follow this exact sequence:

### Step 1: Load Core Context
1. Read `.claude/CLAUDE.md` (this file) — understand the project mission.
2. Read `.claude/rules.md` — understand hard constraints.
3. Read `.claude/persona.md` — adopt the correct persona.
4. Read `.claude/gotchas.md` — internalize known traps.

### Step 2: Load Portfolio State
5. Read `.claude/context/portfolio-context.md` — understand GCP config, color matrix, and SDK versions.
6. Read `.claude/tasks/backlog.md` — understand what's done and what's next.

### Step 3: Identify Applicable Workflows & Skills
7. Scan `.claude/workflows/` — identify which workflow applies to the current request.
8. Scan `.claude/skills/` — identify which skills might be triggered.
9. Scan `.claude/prompts/` — identify reusable prompts that match the task.
10. Scan `.claude/guides/` — load implementation standards relevant to the task.

**Only after completing this boot sequence should the agent begin processing the user's request.**

---

## 🎯 Core Mission

- **Organization**: Savior Systems
- **Project**: Building a portfolio of 30 isolated, high-performance, strictly offline Android utility apps.
- **Tech Stack**: Kotlin, Jetpack Compose (Material 3), Clean Architecture (MVVM), Room Database, Hilt, Jetpack DataStore, AdMob, Firebase Analytics.
- **Compliance**: 100% offline-first. Zero backend syncing of PII. Strict Google Play Data Safety compliance.

---

## 📐 The 14-Document Standard

Every app MUST have exactly 14 detailed blueprint files before implementation begins. See `guides/android-doc-generation.md` for full specifications.

| # | File | Purpose |
|---|------|---------|
| 01 | `01.PRD-REQUIREMENTS.md` | Product requirements, personas, KPIs |
| 02 | `02.UI-UX-DESIGN-SYSTEM.md` | Color palette, typography, animations |
| 03 | `03.FUNCTIONAL-FLOWS.md` | Navigation diagram, state transitions |
| 04 | `04.TECHNICAL-ARCHITECTURE.md` | MVVM tree, engines, dependencies |
| 05 | `05.DATABASE-SCHEMA.md` | Room entities, DAOs, DataStore keys |
| 06 | `06.ADMOB-MONETIZATION-MAP.md` | Ad placements, frequency caps |
| 07 | `07.ASO-PLAY-STORE-LISTING.md` | Store title, description, keywords |
| 08 | `08.PLAY-POLICY-SAFETY.md` | Permissions audit, Data Safety form |
| 09 | `09.TESTING-ASSURANCE-PLAN.md` | Unit tests, manual QA, benchmarks |
| 10 | `10.TRANSLATIONS-LOCALIZATION.md` | Base strings.xml, locale targets |
| 11 | `11.GRAPHIC-ASSETS-MANIFEST.md` | Icon specs, screenshots, feature graphic |
| 12 | `12.LOGGING-ANALYTICS.md` | Firebase events, Crashlytics, PII rules |
| 13 | `13.BACKLOG-TASKS.md` | Phased dev backlog with V2 roadmap |
| 14 | `README.md` | Master index with all links + GCP SOP |

---

## 📁 .claude/ Directory Map

```
.claude/
├── CLAUDE.md                              # THIS FILE — Boot config & mission
├── rules.md                               # Hard coding & behavioral constraints
├── persona.md                             # Agent persona definitions
├── gotchas.md                             # Known traps & anti-patterns (10 items)
│
├── context/
│   └── portfolio-context.md               # GCP details, eCPM data, SDK versions, color matrix
│
├── tasks/
│   └── backlog.md                         # Master progress tracker (30 apps)
│
├── workflows/
│   ├── 01-blueprint-generation.md         # SOP for creating 14-file blueprints
│   ├── app-research-to-release.md         # Full app lifecycle (research → Play Store)
│   ├── 03-batch-documentation-sprint.md   # Aggressive 30-day sprint velocity workflow
│   ├── 04-interlinking-audit.md           # Cross-app link & color integrity checks
│   └── 05-git-operations.md              # Conventional commits & branch strategy
│
├── prompts/
│   ├── generate-app-docs.md               # Trigger prompt for 14-file generation
│   ├── aso-optimization.md                # ASO copywriting prompt
│   ├── review-play-policy-risk.md         # Play Policy compliance audit prompt
│   ├── create-github-issues.md            # Convert backlog phases to GitHub Issues
│   ├── generate-app-icon.md               # Premium icon generation prompt
│   └── deep-research.md                   # Pre-blueprint competitive & technical research
│
├── guides/
│   ├── android-doc-generation.md          # The 14-file standard with quality gates
│   ├── admob-implementation-standard.md   # AdMob SDK setup, UMP consent, test IDs
│   ├── firebase-integration-standard.md   # Firebase BOM, event naming, PII rules
│   └── play-store-account-safety.md       # Account protection, spam avoidance, click policies
│
└── skills/
    ├── link-integrity-checker.md          # Find & fix broken file:/// links
    ├── portfolio-progress-reporter.md     # Live 30-app status table generator
    ├── color-uniqueness-validator.md      # Prevent Play Store "spam" color collisions
    ├── gcp-firebase-manager.md            # gcloud CLI commands for project management
    ├── doc-quality-auditor.md             # 21-point quality audit for 14-file suites
    ├── screenshot-generator.md            # Play Store screenshot composition & specs
    ├── gradle-project-scaffolder.md       # Bootstrap code projects from blueprints
    ├── data-safety-form-generator.md      # Pre-fill Data Safety questionnaire
    ├── dependency-version-checker.md      # Audit SDK versions for freshness
    ├── localization-expander.md            # Generate translated strings.xml files
    └── readme-synchronizer.md             # Keep root README in sync with all 30 apps
```

---

## ⚡ Execution Rules

1. **All code must be production-ready**, compiling, and fully localized into `strings.xml`.
2. **Never use placeholder assets** — generate them using the `generate_image` tool.
3. **Links MUST use GitHub-compatible relative paths** — NEVER `file:///`.
4. **Automate git** — stage, commit (conventional format), and push after every milestone.
5. **Cross-reference `context/portfolio-context.md`** before assigning colors to new apps.
6. **Review `gotchas.md`** before modifying any code to avoid known traps.
7. **Zero Research Gaps**: Conduct exhaustive research before building plans. Blueprints must be world-class, clean, easy to navigate, and heavily interlinked.
8. **No Placeholders**: Do not drop simplified mockups or logic; all database, architecture, and utility structures must have production-ready code blocks so developer compilation can proceed without assumptions.
9. **Monetization Focus**: Optimize every listing, data safety sheet, and SDK setup mapping to maximize AdMob eCPMs and ensure strict Play Store policy compliance.
