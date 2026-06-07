# 🍅 FocusPulse Timer — Developer Index
`
FocusPulse Timer is a premium, minimalist Pomodoro timer application built using Jetpack Compose, Room Database, Kotlin Coroutines, and Google AdMob. This index serves as the developer blueprint for building, testing, and releasing this application.
`
---
`
## 📂 Navigation & Directory Map
Click on any of the sections below to navigate to the specific blueprint:
`
*   [01. PRD-REQUIREMENTS.md](01.PRD-REQUIREMENTS.md) — Product Requirements Document: Features, settings, target audience, and user stories.
*   [02. UI-UX-DESIGN-SYSTEM.md](02.UI-UX-DESIGN-SYSTEM.md) — Custom styling rules, colors (0xFFE74C3C & 0xFF2C3E50), dark mode specifications, and typography.
*   [03. FUNCTIONAL-FLOWS.md](03.FUNCTIONAL-FLOWS.md) — Screen navigation transitions, backstack management, and dialog rules.
*   [04. TECHNICAL-ARCHITECTURE.md](04.TECHNICAL-ARCHITECTURE.md) — Clean MVVM folder bindings, Hilt dependency mapping, and state controls.
*   [05. DATABASE-SCHEMA.md](05.DATABASE-SCHEMA.md) — Room DB entities, SQL queries, preference stores, and DAO parameters.
*   [06. ADMOB-MONETIZATION-MAP.md](06.ADMOB-MONETIZATION-MAP.md) — Banner, interstitial, and rewarded ad placements with safety cooldown limits.
*   [07. ASO-PLAY-STORE-LISTING.md](07.ASO-PLAY-STORE-LISTING.md) — Ready-to-publish Google Play titles, descriptions, and ASO targeting.
*   [08. PLAY-POLICY-SAFETY.md](08.PLAY-POLICY-SAFETY.md) — Compliance strategies, permissions minimization, and data declarations.
*   [09. TESTING-ASSURANCE-PLAN.md](09.TESTING-ASSURANCE-PLAN.md) — Edge cases, battery optimizations, QA scripts, and verification metrics.
*   [10. TRANSLATIONS-LOCALIZATION.md](10.TRANSLATIONS-LOCALIZATION.md) — Language resource strings (English, Bengali, Spanish).
*   [11. GRAPHIC-ASSETS-MANIFEST.md](11.GRAPHIC-ASSETS-MANIFEST.md) — Launcher icons, vectors, and device screenshot structures.
*   [12. LOGGING-ANALYTICS.md](12.LOGGING-ANALYTICS.md) — Firebase events schema and performance logger keys.
*   [13. BACKLOG-TASKS.md](13.BACKLOG-TASKS.md) — The interactive developer backlog tracker.
`
---
## 🛠️ Step-by-Step Developer Setup
1.  **Clone / Initialize**: Ensure you are in the isolated 1. FocusPulse Timer directory.
2.  **Gradle Configurations**: Create secrets.properties in the project root to load AdMob Unit IDs.
3.  **Handoff Check**: Read [DEVELOPER-GUIDE.md](..%5CDEVELOPER-GUIDE.md) in the repository root for template rules.
``
---
## ☁️ GCP & Firebase API Setup & SOP
`
### 1. Required Cloud API Category
- **Category:** Level 1 (Telemetry, UMP Consent, and AdMob)
- **Core APIs:** \irebase.googleapis.com\ (Free Tier)
- **SOP Implementation:** Log ASO conversion metrics, standard analytics telemetry, and initialize UMP consent logs.\
`
### 2. Credentials & Config Mapping
- Place the downloaded \google-services.json\ config inside the \pp/\ directory.
- Production credentials are dynamically configured on launch and kept out of Git repository logs.
`