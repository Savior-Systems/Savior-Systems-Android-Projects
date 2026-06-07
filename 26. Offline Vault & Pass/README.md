# Offline Vault & Pass — Master Index
```
Welcome to the design and development blueprint directory for **Offline Vault & Pass**. This is a documentation-first repository designed to instruct human developers or AI agents on building this application from scratch.
```
## 📂 Documentation Directory Map
Click on any of the sections below to navigate to the specific blueprint:
```
*   [01. PRD-REQUIREMENTS.md](01.PRD-REQUIREMENTS.md) — Feature list, user stories, and target personas.
*   [02. UI-UX-DESIGN-SYSTEM.md](02.UI-UX-DESIGN-SYSTEM.md) — Accent colors, layout, and dynamic typography sets.
*   [03. FUNCTIONAL-FLOWS.md](03.FUNCTIONAL-FLOWS.md) — Screens, backstack routing, and user transitions.
*   [04. TECHNICAL-ARCHITECTURE.md](04.TECHNICAL-ARCHITECTURE.md) — MVVM directory mappings and clean state controls.
*   [05. DATABASE-SCHEMA.md](05.DATABASE-SCHEMA.md) — Room tables, DAO query blueprints, and shared keys.
*   [06. ADMOB-MONETIZATION-MAP.md](06.ADMOB-MONETIZATION-MAP.md) — Ad formats, triggers, and the 180s cooldown settings.
*   [07. ASO-PLAY-STORE-LISTING.md](07.ASO-PLAY-STORE-LISTING.md) — Prepared titles, descriptions, and keywords.
*   [08. PLAY-POLICY-SAFETY.md](08.PLAY-POLICY-SAFETY.md) — Permission checks, data declarations, and privacy rules.
*   [09. TESTING-ASSURANCE-PLAN.md](09.TESTING-ASSURANCE-PLAN.md) — Manual scenarios, edge cases, and QA steps.
*   [10. TRANSLATIONS-LOCALIZATION.md](10.TRANSLATIONS-LOCALIZATION.md) — Multi-language localization and translation strings.
*   [11. GRAPHIC-ASSETS-MANIFEST.md](11.GRAPHIC-ASSETS-MANIFEST.md) — Graphic dimensions, icon targets, and custom items.
*   [12. LOGGING-ANALYTICS.md](12.LOGGING-ANALYTICS.md) — Firebase tracker events and metrics rules.
*   [13. BACKLOG-TASKS.md](13.BACKLOG-TASKS.md) — The interactive checkbox backlog for progress tracking.
```
---
**Status**: Ready for scaffolding. All configuration keys must pull from the root blueprints.
``
---
## ☁️ GCP & Firebase API Setup & SOP
```
### 1. Required Cloud API Category
- **Category:** Level 2 (Secure Sync & Cloud Storage backups)
- **Core APIs:** \irestore.googleapis.com\, \storage.googleapis.com\`n- **SOP Implementation:** Firestore DB sync utilizing user-isolated security rules defined in \CLOUD-BLUEPRINTS.md\.\
```
### 2. Credentials & Config Mapping
- Place the downloaded \google-services.json\ config inside the \pp/\ directory.
- Production credentials are dynamically configured on launch and kept out of Git repository logs.
```