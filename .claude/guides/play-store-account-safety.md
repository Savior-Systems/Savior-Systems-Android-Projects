# Guide: Play Store Account Safety & Policy Compliance

This guide details the strict guardrails required to keep the Savior Systems Play Console publisher account secure while deploying multiple utility apps quickly.

---

## 1. Preventing "Repetitive Content" (Spam Policy) Rejections

Google Play Store automatically detects template-cloned applications. To prevent account bans:
- **Visual Isolation**: Every app must have a unique color palette registered in `context/portfolio-context.md`. Never reuse the same base color setups.
- **Icon Originality**: Icons must be individually generated utilizing distinct visual symbols. Never use the same template icon or copy visual layouts.
- **Codebase Structural Isolation**:
  - Package names must be distinct (e.g. `com.saviorsystems.focuspulse`, `com.saviorsystems.pdfcompressor`).
  - Resource names (colors, themes, layouts, XML vectors) must use unique prefixes (e.g. `@style/FocusPulseTheme`, `@style/CompressPdfTheme`) to prevent asset merge compilation overlaps.
- **Store Listing Descriptions**: Descriptions and titles must be fully custom and rewritten. Never use search-replaced description boilerplate.

---

## 2. Preventing AdMob "Accidental Clicks" & Ad Limits

*   **Zero-Ad input zones**: Never load Banner or Native ads adjacent to active editing keyboards, input text fields, or navigation tabs.
*   **Cooldown Gates**: Instants/Interstitials must follow a strict 180-second minimum timer per user. Showing ads on back-to-back actions triggers Google's "Disruptive Ads" policy suspension.
*   **App Open Ad (AOA) Suppressions**: Do not trigger AOA on cold boot if the splash screen has been visible for less than 1.5 seconds. If the user briefly switches out of the app and returns, suppress the AOA.

---

## 3. Data Safety & Privacy Form Auditing

*   **100% Offline Integrity**: Unless AdMob/Firebase require connection, no user data (e.g., CV history, profiles, tasks, calculated values) should ever cross the device boundary.
*   **Data Safety Declarations**:
    - **No Data Shared**: Always declare "No user data is shared with third parties."
    - **No Data Collected**: Declare "No user data is collected" for app calculations, as Room databases stay sandboxed on-device.

---

## 4. Dangerous System Permissions (Google Play Checks)

*   **Exact Alarms (`SCHEDULE_EXACT_ALARM`)**: Only request if the core functionality depends on precise timing (e.g. birthday countdown notifications or daily trackers). Always provide a fallback to WorkManager.
*   **Storage Access Framework (SAF)**: Always prefer SAF pickers over dangerous runtime permissions like `READ_EXTERNAL_STORAGE` or `WRITE_EXTERNAL_STORAGE`.
