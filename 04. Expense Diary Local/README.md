# Expense Diary Local — Master Index

Welcome to the design and development blueprint directory for **Expense Diary Local**. This is a documentation-first repository designed to instruct human developers or AI agents on building this application from scratch.

---

## 🎯 App Overview

| Attribute | Value |
| :--- | :--- |
| **App Name** | Expense Diary Local |
| **Package** | `com.saviorsystems.expensediarylocal` |
| **Category** | Finance |
| **Architecture** | Clean MVVM + Jetpack Compose + Room (SQLCipher) |
| **Privacy Model** | 100% Offline-First, AES-256 Encrypted Database |
| **Primary Color** | `#F1C40F` (Sunflower Gold) |
| **Secondary Color** | `#7F8C8D` (Concrete Gray) |
| **Target Keywords** | expense tracker, money manager, budget planner |

---

## 📂 Documentation Directory Map

Click on any of the sections below to navigate to the specific blueprint:

| # | Document | Description |
| :--- | :--- | :--- |
| 01 | [PRD-REQUIREMENTS.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/01.PRD-REQUIREMENTS.md) | Feature list, user stories, personas, and success metrics. |
| 02 | [UI-UX-DESIGN-SYSTEM.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/02.UI-UX-DESIGN-SYSTEM.md) | Gold/gray palette, typography, component tokens, and animations. |
| 03 | [FUNCTIONAL-FLOWS.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/03.FUNCTIONAL-FLOWS.md) | Navigation diagram, user journeys, and state management rules. |
| 04 | [TECHNICAL-ARCHITECTURE.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/04.TECHNICAL-ARCHITECTURE.md) | Full directory tree, tech stack, DI modules, and encryption flow. |
| 05 | [DATABASE-SCHEMA.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/05.DATABASE-SCHEMA.md) | Room tables, indices, DAO queries, and DataStore preferences. |
| 06 | [ADMOB-MONETIZATION-MAP.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/06.ADMOB-MONETIZATION-MAP.md) | Ad formats, frequency caps, UX-safe zones, and revenue model. |
| 07 | [ASO-PLAY-STORE-LISTING.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/07.ASO-PLAY-STORE-LISTING.md) | Store title, full description, keyword strategy, and assets. |
| 08 | [PLAY-POLICY-SAFETY.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/08.PLAY-POLICY-SAFETY.md) | Permissions, Data Safety form, financial declaration, and policies. |
| 09 | [TESTING-ASSURANCE-PLAN.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/09.TESTING-ASSURANCE-PLAN.md) | Unit/integration/UI tests, QA checklist, and performance targets. |
| 10 | [TRANSLATIONS-LOCALIZATION.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/10.TRANSLATIONS-LOCALIZATION.md) | Full strings.xml, localization targets, and RTL support rules. |
| 11 | [GRAPHIC-ASSETS-MANIFEST.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/11.GRAPHIC-ASSETS-MANIFEST.md) | Icon specs, screenshot designs, and feature graphic blueprint. |
| 12 | [LOGGING-ANALYTICS.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/12.LOGGING-ANALYTICS.md) | 9 custom Firebase events, Crashlytics config, and privacy rules. |
| 13 | [BACKLOG-TASKS.md](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/13.BACKLOG-TASKS.md) | Phased development backlog with 50+ tasks across 6 phases. |

---

## 🖼️ App Icon

![Expense Diary Local Icon](file:///f:/Savior-Systems-Android-Projects/04.%20Expense%20Diary%20Local/expense_diary_local_icon.png)

---

## 🔑 Key Differentiators

| Feature | Description |
| :--- | :--- |
| **100% Offline** | Zero network dependency for core functionality |
| **AES-256 Encryption** | SQLCipher-encrypted Room database with Android Keystore keys |
| **5-Second Entry** | Streamlined FAB → keypad → category → save workflow |
| **Budget Alerts** | Local push notifications at 80% and 100% thresholds |
| **Visual Analytics** | Interactive donut charts and monthly trend bars (Vico) |
| **Biometric Lock** | PIN + fingerprint/face authentication gate |
| **Export Anywhere** | CSV, PDF, and encrypted JSON backup/restore |
| **Privacy Screen** | Auto-blur when app enters background |

---

## ☁️ GCP & Firebase API Setup & SOP

### 1. Required Cloud API Category
- **Category:** Level 2 (Secure Sync & Cloud Storage backups)
- **Core APIs:** `firebaseanalytics.googleapis.com`, `crashlytics.googleapis.com`, `admob.googleapis.com`
- **SOP Implementation:** Firebase Analytics for anonymous telemetry, Crashlytics for crash reporting, AdMob for monetization.

### 2. Credentials & Config Mapping
- Place the downloaded `google-services.json` config inside the `app/` directory.
- Production AdMob Unit IDs are stored in `local.properties` and injected via `buildConfigField`.
- Production credentials are dynamically configured on launch and kept out of Git repository logs.

### 3. Firebase Project
- **Project ID:** `hopeful-breaker-426606-h9`
- **App ID:** Registered in Firebase Console under the Savior Systems portfolio.
- **SHA-1/SHA-256:** Debug and release keystores registered for API access.

---

## 📊 Status

**Documentation**: ✅ Complete (14/14 files)  
**Assets**: ✅ App icon generated  
**Phase**: Ready for Phase 1 scaffolding  
**Last Updated**: June 2026
