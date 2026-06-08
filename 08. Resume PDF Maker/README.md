# 📄 Resume PDF Maker — Master Index

> **Package:** `com.saviorsystems.resumemaker`  
> **Category:** Productivity / Tools · **Target Market:** Global (Tier-1)  
> **Complexity:** 3/5 · **Est. Build:** 9 Days · **Offline:** 100%

---

## 🎨 App Icon Showcase

![Resume PDF Maker App Icon](resume_pdf_maker_icon.png)

---

Welcome to the design and development blueprint directory for **Resume PDF Maker** — a high-performance, 100% offline-first application that enables users to compile, customize, and export professional, ATS-compliant, selectable-text PDFs in minutes. The application runs entirely offline, allowing users to configure margins, fonts, and corporate colors, export backups to local JSON files, and open generated files directly inside external productivity applications (like Canva, Adobe, and Google Docs).

---

## 🎯 Key Differentiators
* **Selectable Vector PDFs:** Draws text as native vector font glyphs (never flat bitmaps) to ensure 100% ATS search compliance and editability.
* **Page-Break Partitioning Engine:** Programmatic height-budgeting algorithm to automatically calculate page boundaries without splitting lines of text.
* **Template Branding Customization:** Customize layout margins (Compact, Normal, Wide), font pairings, and professional color presets.
* **Canva & Productivity Integration:** Action View/Send intent triggers on export completion to seamlessly open resumes in Canva, Google Drive, or email.
* **Local JSON Backups:** Export and import raw CV profile configurations to backup files locally with zero network reliance.
* **Zero Storage Permissions:** Utilizes Scoped Storage to save files directly to `/Downloads` without demanding broad storage read/write permissions.

---

## 📂 Documentation Directory Map
Click on any of the sections below to navigate to the specific blueprint:

```infographic
infographic list-grid-badge-card
data
  title Blueprints Directory Map
  items
    - label 01. PRD Requirements
      desc Core features, user stories, target personas & offline scope.
    - label 02. UI-UX Design
      desc A4 margins, spacing tokens, typography & dynamic themes.
    - label 03. Functional Flows
      desc SAF export flows, JSON share & external Canva Open Intents.
    - label 04. Tech Architecture
      desc Clean MVVM layouts, PdfGenerator contract & page budgeting code.
    - label 05. Database Schema
      desc Room DB tables, entities, cascading relations & details POJO.
    - label 06. AdMonetization Map
      desc Rewarded ad unlocks, native list units & 180s cooldown cap.
    - label 07. ASO Store Listing
      desc Keyword targeting clusters, US/ES/BN localized listings.
    - label 08. Play Policy Safety
      desc Storage Access Framework & zero data collection safety declaration.
    - label 09. Testing Assurance
      desc Pagination unit tests, selectable text checks & SAF choosers.
    - label 10. Translations
      desc Localization resource XML files for English, Spanish, and Bengali.
    - label 11. Graphic Assets
      desc App icon designs, vector illustrations & template previews.
    - label 12. Logging & Analytics
      desc Non-PII Firebase analytics tracking & non-fatal Crashlytics.
    - label 13. Backlog Tasks
      desc 5-phase structured roadmap checklist for the developer.
```

*   [01. Product Requirement Document](01.PRD-REQUIREMENTS.md) — Feature list, user stories, and target personas.
*   [02. UI-UX Design System](02.UI-UX-DESIGN-SYSTEM.md) — Accent colors, layout, and dynamic typography sets.
*   [03. Functional Flows](03.FUNCTIONAL-FLOWS.md) — Screen transitions, backstack routing, and user flows.
*   [04. Technical Architecture](04.TECHNICAL-ARCHITECTURE.md) — MVVM directory mappings and clean state controls.
*   [05. Database Schema](05.DATABASE-SCHEMA.md) — Room tables, DAO query blueprints, and shared keys.
*   [06. AdMob Monetization Map](06.ADMOB-MONETIZATION-MAP.md) — Ad formats, triggers, and the 180s cooldown settings.
*   [07. ASO & Play Store Listing](07.ASO-PLAY-STORE-LISTING.md) — Prepared titles, descriptions, and keywords.
*   [08. Play Policy & Data Safety](08.PLAY-POLICY-SAFETY.md) — Permission checks, data declarations, and privacy rules.
*   [09. Testing & Quality Assurance](09.TESTING-ASSURANCE-PLAN.md) — Manual scenarios, edge cases, and QA steps.
*   [10. Translations & Localization](10.TRANSLATIONS-LOCALIZATION.md) — Multi-language localization and translation strings.
*   [11. Graphic Asset Manifest](11.GRAPHIC-ASSETS-MANIFEST.md) — Graphics, icons, vectors, and screen preview designs.
*   [12. Logging & Analytics](12.LOGGING-ANALYTICS.md) — Firebase events schema and performance logger keys.
*   [13. Backlog Tasks](13.BACKLOG-TASKS.md) — The interactive developer backlog tracker.

---

**Status:** ✅ Documentation complete. Upgraded to high-scale offline specification.
All configuration keys must pull from the root blueprints: [DEVELOPER-GUIDE.md](../DEVELOPER-GUIDE.md) · [REUSABLE-ANDROID-COMPONENTS.md](../REUSABLE-ANDROID-COMPONENTS.md) · [MASTER-CHECKLIST.md](../MASTER-CHECKLIST.md)
