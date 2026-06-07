# Savior Systems: AI Agent Operating System
```
This guide outlines the rules, templates, and procedures for AI Coding Agents (such as Cursor, Antigravity, or Claude) when tasked with generating code or updating applications within this portfolio.
```
---
```
## 1. Operating Rules for AI Agents
```
1.  **Strict Isolation**: Every app must remain fully independent. Never import libraries or code artifacts from other application folders.
2.  **No Placeholders**: Never write placeholder methods, empty interfaces, or leave `// TODO` comments inside code generated for release. All features must be fully implemented.
3.  **Modern Code standards**:
    *   Language: Kotlin.
    *   UI: Jetpack Compose + Material 3.
    *   State: MVVM pattern exposing state using `StateFlow`.
    *   AdManager: Copy-paste the standard implementation from `REUSABLE-ANDROID-COMPONENTS.md`.
```
---
```
## 2. Directory Layout Rule
```
All code and assets for a specific application must reside strictly within its designated folder.
```
```
01. FocusPulse Timer/
├── README.md               <-- Application specs and design criteria
├── app/                    <-- Standard Android project directory
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/saviorsystems/...
│   │   │   └── res/
│   └── build.gradle.kts
└── build.gradle.kts
```
```
---
```
## 3. Dependency Configuration
```
Always use the Kotlin DSL (`.gradle.kts`) configuration. Ensure dependencies use Google Version Catalogs (`libs.versions.toml`) to keep core frameworks aligned across all apps.
```