# Smart Age & BD Date — Master Index
`
Welcome to the design and development blueprint directory for **Smart Age & BD Date**. This is a documentation-first repository designed to instruct developers and AI agents on building this application from scratch.
`
---
`
## 🎨 App Icon Showcase
`
![Smart Age & BD Date App Icon](smart_age_icon.png)
`
---
`
## 📂 Documentation Directory Map
Click on any of the sections below to navigate to the specific blueprint:
`
*   [01. Product Requirement Document](01.PRD-REQUIREMENTS.md) — Feature list, user stories, and target personas.
*   [02. UI/UX Design System](02.UI-UX-DESIGN-SYSTEM.md) — Accent colors, layout, and dynamic typography sets.
*   [03. Functional Flows](03.FUNCTIONAL-FLOWS.md) — Screen transitions, backstack routing, and user flows.
*   [04. Technical Architecture](04.TECHNICAL-ARCHITECTURE.md) — MVVM directory mappings and clean state controls.
*   [05. Database Schema](05.DATABASE-SCHEMA.md) — Room tables, DAO query blueprints, and shared keys.
*   [06. AdMob Monetization Map](06.ADMOB-MONETIZATION-MAP.md) — Ad formats, triggers, and the 180s cooldown settings.
*   [07. ASO & Play Store Listing](07.ASO-PLAY-STORE-LISTING.md) — Prepared titles, descriptions, and keywords.
*   [08. Play Policy & Data Safety](08.PLAY-POLICY-SAFETY.md) — Permission checks, data declarations, and privacy rules.
*   [09. Testing & Quality Assurance](09.TESTING-ASSURANCE-PLAN.md) — Manual scenarios, edge cases, and QA steps.
*   [10. Translations & Localization](10.TRANSLATIONS-LOCALIZATION.md) — Multi-language localization and translation strings.
*   [11. Graphic Assets Manifest](11.GRAPHIC-ASSETS-MANIFEST.md) — Graphic dimensions, icon targets, and custom items.
*   [12. Logging & Analytics Schema](12.LOGGING-ANALYTICS.md) — Firebase tracker events and metrics rules.
*   [13. Development Backlog](13.BACKLOG-TASKS.md) — The interactive checkbox backlog for progress tracking.
`
---
`
## ☁️ GCP & Firebase API Setup & SOP
`
### 1. Required Cloud API Category
- **Category:** Level 1 (Telemetry, UMP Consent, and AdMob)
- **Core APIs:** `firebase.googleapis.com` (Free Tier)
- **SOP Implementation:** Log ASO conversion metrics, standard analytics telemetry, and initialize UMP consent logs.
`
### 2. Credentials & Config Mapping
- Place the downloaded `google-services.json` config inside the `app/` directory.
- Production credentials are dynamically configured on launch and kept out of Git repository logs.
`