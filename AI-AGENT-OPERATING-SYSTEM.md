# Savior Systems: AI Agent Operating System

This guide outlines rules, prompts, directory conventions, and personas for AI Coding Agents (such as Cursor, Antigravity, or Claude) when generating code, updating blueprints, or editing applications within this portfolio.

---

## 📂 Navigation Index
Before performing code modifications, AI agents must reference:
*   [Main README](README.md) — Master listing and roadmap of the 30-app portfolio.
*   [Agent Personas](.claude/persona.md) — Persona descriptions (Mobile Architect, UI/UX Visionary, ASO Marketer) to adopt.
*   [Developer Guide](DEVELOPER-GUIDE.md) — Architectural patterns, Kotlin styles, and AdMob cooldown configurations.
*   [Master Submission Checklist](MASTER-CHECKLIST.md) — Pre-flight requirements every app must pass.

---

## 1. Operating Rules for AI Agents

1.  **Strict Isolation**: Every app must remain fully independent. Never import libraries or code files from other application folders.
2.  **No Placeholders**: Never write placeholder methods, empty interfaces, or leave `// TODO` comments inside code generated for release. All features must be fully implemented.
3.  **Modern Code Standards**:
    *   Language: Kotlin.
    *   UI: Jetpack Compose + Material 3.
    *   State: MVVM pattern exposing state using `StateFlow`.
    *   AdManager: Copy-paste the standard implementation from [REUSABLE-ANDROID-COMPONENTS.md](REUSABLE-ANDROID-COMPONENTS.md).
4.  **Relative Linking**: When referencing other files, always use relative Markdown paths. Never write absolute `file:///` paths, which break across developer platforms.

---

## 2. Directory Layout Rule

All code and assets for a specific application must reside strictly within its designated folder.

```
12. Minimalist To-Do/
├── 01.PRD-REQUIREMENTS.md       <-- Requirements & Personas
├── 02.UI-UX-DESIGN-SYSTEM.md     <-- Accent colors & typography scales
├── 03.FUNCTIONAL-FLOWS.md       <-- Screen flows & transitions
├── 04.TECHNICAL-ARCHITECTURE.md <-- ViewModel and implementation codes
├── 05.DATABASE-SCHEMA.md        <-- Database structures (Room / DataStore)
├── 06.ADMOB-MONETIZATION-MAP.md <-- Ad unit IDs & cooldown layouts
├── 07.ASO-PLAY-STORE-LISTING.md <-- Title, descriptions, and ASO keywords
├── 08.PLAY-POLICY-SAFETY.md     <-- Permission justifications & Play safety
├── 09.TESTING-ASSURANCE-PLAN.md <-- Automated unit tests & manual QA steps
├── 10.TRANSLATIONS-LOCALIZATION.md <-- String resource XML tags
├── 11.GRAPHIC-ASSETS-MANIFEST.md <-- App Icon and promotional asset dimensions
├── 12.LOGGING-ANALYTICS.md      <-- Non-PII Firebase event trackers
├── 13.BACKLOG-TASKS.md          <-- Sprint checklists
├── README.md                    <-- Master directory index
└── app/                         <-- Standard Android project directory
```

---

## 3. Persona Integration
AI agents must adopt the specialized personas detailed in [.claude/persona.md](.claude/persona.md). When generating blueprints or writing source code:
*   Use the **Lead Mobile Architect** persona to design Room databases, repositories, and ViewModels.
*   Use the **UI/UX Visionary** persona to configure premium theme palettes (like Charcoal Gray `#37474F` or Emerald Green `#2E7D32`) and Jetpack Compose gesture actions.
*   Use the **ASO & Growth Marketer** persona to draft Play Store titles and long descriptions.
*   Use the **Play Policy Enforcer** persona to audit permissions and review the Data Safety checklist.
