# Savior Systems: Master Submission Checklist
`
This is the pre-flight quality check that every app in our portfolio must pass before it is pushed to the Google Play Console for internal testing, closed testing, or production tracks.
`
---
`
## 📂 Navigation Index
Before submitting an application, refer to:
*   [Main README](README.md) — Master listing and roadmap of the 30-app portfolio.
*   [Developer Guide](DEVELOPER-GUIDE.md) — Technical tech stack specifications and guidelines.
*   [Contributing Guidelines](CONTRIBUTING.md) — Conventional Commits rules and Git workflows.
*   [AI Agent Operating System](AI-AGENT-OPERATING-SYSTEM.md) — Guidelines for AI developers.
`
---
`
## 1. Code Quality & Compilation
`
*   [ ] App compiles with zero compilation errors and zero compiler warnings under release build configuration.
*   [ ] Android Lint check reports zero errors (severity: error). All warnings reviewed and marked as clean.
*   [ ] ProGuard/R8 rules configured (`proguard-rules.pro` included and active).
*   [ ] Verify that no API keys or AdMob unit IDs are committed to the public Git repository. Use `secrets.properties` mapping instead.
*   [ ] Ensure `minifyEnabled` and `shrinkResources` are set to `true` in `build.gradle.kts` release config.
*   [ ] Verify application APK or AAB file size is optimized and remains under **15 MB**.
*   [ ] Remove all obsolete testing logs, raw comments, or temporary console outputs (`println()`, `Log.d()`).
*   [ ] Ensure no unused resources (layouts, drawables, assets) are left in the package. Run `Analyze > Run Inspection by Name > Unused resources`.
*   [ ] Confirm Kotlin compiler compatibility flags match the Target SDK dependencies.
*   [ ] Verify that the app starts up from cold state in less than **2.0 seconds** on standard test devices.
`
---
`
## 2. Architecture & MVVM Standard
`
*   [ ] Application follows MVVM (Model-View-ViewModel) architecture.
*   [ ] Views contain only UI elements and no logical expressions or operations.
*   [ ] ViewModels expose data state using Kotlin read-only StateFlow (i.e. `StateFlow<UiState>`). Do not expose MutableStateFlow.
*   [ ] ViewModels are free from imports pointing to Android framework resources (e.g. `android.content.Context`). Use Hilt or application context mapping where necessary.
*   [ ] Core data logic encapsulated in Repository classes.
*   [ ] Room databases use structured DAO layers. Query structures run on background Coroutine dispatchers (e.g. `Dispatchers.IO`).
*   [ ] Screen transitions and arguments utilize navigation compose structures.
`
---
`
## 3. UI/UX & Design Isolation
`
*   [ ] App theme uses a unique color configuration (e.g. Custom light/dark themes mapped in color sets).
*   [ ] Dark mode support verified on all screens. No text colors are hardcoded to black or white.
*   [ ] All user-facing strings are defined in `strings.xml`. Hardcoded text is banned.
*   [ ] Loading indicators are rendered during slow asynchronous database operations.
*   [ ] Empty states are rendered cleanly with a message and icon if user databases are empty (e.g., no items in To-Do list).
*   [ ] Navigation back-stack operates properly. Back actions do not lead to white screens or empty view stacks.
*   [ ] Text sizing uses `sp` instead of `dp`. Layout spacing utilizes standardized dynamic layouts.
*   [ ] Input screens support clean text validation (e.g., show error on negative inputs or empty values).
*   [ ] Adaptive Android app icon is verified on stock launchers.
*   [ ] UI conforms to the Material 3 components guide.
`
---
`
## 4. AdMob Monetization Checks
`
*   [ ] AdMob SDK initialized inside Application context on startup.
*   [ ] Verification test ad unit IDs (`ca-app-pub-3940256099942544/...`) are strictly active during debug configuration.
*   [ ] Production ad unit IDs are configured to load inside the release version only.
*   [ ] The interstitial 180-second cooldown is enforced by `AdManager`.
*   [ ] Ads do not load immediately over clickable elements (e.g., separated from navigation or action keys).
*   [ ] Confirm app-ads.txt links match the hosting domain.
*   [ ] Google UMP (User Messaging Platform) GDPR dialog triggers in European regions.
`
---
`
## 5. Policy & Testing Compliance
`
*   [ ] Application has an independent Privacy Policy URL active.
*   [ ] Target SDK set to 35, Minimum SDK set to 24.
*   [ ] Google Play Console Data Safety form maps to exactly what SDK modules are embedded (e.g., Firebase, AdMob ID collection).
*   [ ] The application requires zero permissions unless explicitly needed and approved by strategy.
*   [ ] App tested on real devices running Android 10, 12, 14, and 15.
*   [ ] App tested under slow network simulations to ensure crash-free execution.
*   [ ] Final App Bundle (`.aab`) signed using upload key prior to testing upload.
`