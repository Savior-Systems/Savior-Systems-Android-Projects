# Savior Systems — Known Gotchas & Anti-Patterns

Common traps and their solutions. Every agent MUST review this file before modifying code.

---

## 1. AdMob SDK Crashes
- **Trap**: Initializing the AdMob SDK without registering `<meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="..."/>` in `AndroidManifest.xml` triggers an instant crash on start.
- **Fix**: Always declare the meta-data tag. Use `BuildConfig` fields injected from `local.properties` so AdMob IDs are never hardcoded.

## 2. GDPR Consent Race Condition
- **Trap**: Displaying a banner or loading an interstitial *before* the UMP Consent dialog resolves violates EU regulations and throttles ad revenue.
- **Fix**: Wrap all ad-loading logic behind a `consentManager.canRequestAds()` gate. Load ads only after UMP returns.

## 3. Background Broadcast Limits (Android 12-14+)
- **Trap**: Triggering background services or exact alarms on Android 12+ without `SCHEDULE_EXACT_ALARM` or Android 14+ without `USE_EXACT_ALARM` will silently fail. No crash, no log — just silent failure.
- **Fix**: Always check `alarmManager.canScheduleExactAlarms()` before calling `setExactAndAllowWhileIdle`. Provide a graceful fallback to `WorkManager` with inexact timing.

## 4. Duplicate Resource Compilation
- **Trap**: Copy-pasting themes, layouts, or Compose color files between projects without renaming XML resource names causes Gradle merge conflicts.
- **Fix**: Every app MUST have a unique theme name prefix (e.g., `FocusPulseTheme`, `WaterLogTheme`).

## 5. Room Migration Crashes
- **Trap**: Adding a column to a Room entity without providing a `Migration` or setting `fallbackToDestructiveMigration()` will crash on app updates.
- **Fix**: During V1 development, always use `fallbackToDestructiveMigration()`. Switch to explicit `Migration` objects before the first production release.

## 6. Jetpack Glance Widget Silent Failures
- **Trap**: `GlanceAppWidget.updateAll(context)` can silently fail if the widget provider is not registered in the manifest or if the `appwidget-provider` XML is malformed.
- **Fix**: Always verify `<receiver>` and `<meta-data>` declarations in `AndroidManifest.xml`. Test widget updates on a physical device; emulators can behave differently.

## 7. POST_NOTIFICATIONS Permission (Android 13+)
- **Trap**: Targeting SDK 33+ and firing a notification without first requesting `POST_NOTIFICATIONS` permission results in the notification being silently dropped. Users will never see it and the app appears broken.
- **Fix**: Request the permission during onboarding using `ActivityCompat.requestPermissions()`. If denied, show a Snackbar explaining the impact and deep-link to system settings.

## 8. DataStore Concurrent Write Corruption
- **Trap**: Multiple coroutines writing to the same `DataStore<Preferences>` simultaneously can cause `IOException`. This is common when a Widget callback and the main app UI both try to update preferences at the same time.
- **Fix**: Ensure all DataStore writes go through a single `Repository` with a `Mutex` lock or use `DataStore`'s built-in `updateData {}` which handles atomic transactions.

## 9. Compose Recomposition Performance Killers
- **Trap**: Passing unstable lambdas or non-stable data classes to Composables causes infinite recomposition loops, tanking performance.
- **Fix**: Mark data classes with `@Immutable` or `@Stable`. Hoist lambda definitions using `remember`. Profile with Layout Inspector.

## 10. Play Store "Spam" Rejection for Similar Apps
- **Trap**: Publishing multiple apps with identical UI templates, color schemes, and boilerplate descriptions triggers Google's "Repetitive Content / Spam" policy.
- **Fix**: Every app MUST have a unique primary color palette, unique app icon design language, and a fully original store description. Cross-reference `02.UI-UX-DESIGN-SYSTEM.md` across apps to prevent overlap.

## 11. Global Regex Replacements & Markdown Corruption
- **Trap**: Running global python/bash scripts using loose or unanchored Regular Expressions (e.g., trying to fix missing backticks via regex) across the entire workspace can unintentionally match valid blank lines or partial lines, injecting garbage characters (like \`\`\`) and permanently corrupting hundreds of markdown files simultaneously.
- **Fix**: NEVER run a global regex string replacement script on the whole repository without explicitly anchoring it, validating it on a dry-run, and reviewing the exact diff. If you only need to fix a few specific formatting errors, use specific tools (like `multi_replace_file_content`) on those specific files manually. Never automate workspace-wide formatting corrections unless explicitly ordered to.
