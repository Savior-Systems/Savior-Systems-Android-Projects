# Savior Systems: Play Console Policy Guardrails

Compliance is the foundation of our portfolio business model. A single suspension can terminate the entire Savior Systems developer account. This document defines the compliance rules that developers must follow.

---

## 1. Repetitive Content Policy (The Multi-App Risk)

Google Play Console prohibits publishing multiple apps with highly similar features, layouts, or metadata.

```
┌────────────────────────────────────────────────────────┐
│             Repetitive Content Policy Checklist        │
├────────────────────────────────────────────────────────┤
│ 1. Unique Package Names (different package groups)     │
│ 2. Completely customized Color Themes per app          │
│ 3. Distinct Play Store Listing Descriptions            │
│ 4. Unique Icon designs & generated screenshots         │
│ 5. App-specific localized configurations               │
└────────────────────────────────────────────────────────┘
```

### Mandated Isolation Strategy
1.  **Codebase Customization**: While core modules (like database configuration or settings views) can share design patterns, their specific styling, navigation, and class configurations must be customized. No code cloning across apps is permitted.
2.  **Unique Package Groups**: Distribute apps across package groups based on type:
    *   Health/Loggers: `com.saviorsystems.health.dailywater`
    *   Productivity: `com.saviorsystems.prod.focuspulse`
    *   Utilities: `com.saviorsystems.utils.unitconverter`
3.  **UI Brand Splitting**: Every application must use a unique accent color and typography configuration. Avoid using the default Material 3 color schemes across multiple apps.

---

## 2. Metadata Compliance

*   **App Title**: Maximum 30 characters. Do not use keyword-stuffed strings (e.g., "FocusPulse Pomodoro Timer Task Manager Pro"). Use short, branded names: "FocusPulse Timer".
*   **Descriptions**: Do not include lists of keywords. Write readable, user-centric paragraphs describing the features.
*   **Screenshots**: Must display the actual user interface of the running application. Mockups showing devices that do not run Android are prohibited.
*   **Trademarks**: Never reference competitor names, brand names, or registered trademarks in your listings (e.g., do not say "Similar to Forest App or Pomofocus").

---

## 3. Privacy & Data Safety Form

Every application must link to a valid Privacy Policy and complete the Google Play Data Safety Questionnaire.

### Standard Privacy Policy Framework
*   **Location**: Host each app's privacy policy at:
    `https://savior-systems.github.io/privacy-policies/[app-package-name].html`
*   **Scope**: State clearly that the app is "offline-first" and does not transmit personal data, save for logs collected by AdMob or Firebase.

### Data Safety Declarations
If the app includes AdMob and Firebase Analytics, you **MUST** declare collection of:
1.  **Device or Other IDs**: (Collected by AdMob/Firebase for advertising).
2.  **Crash Logs**: (Collected by Firebase Crashlytics for quality control).
3.  **Diagnostics**: (Performance metrics).

---

## 4. Permissions Policy

To maximize conversion rate and reduce user friction, Savior Systems apps default to a **Zero-Permission Policy**.

| App Type | Permitted Permissions | Rationale |
| :--- | :--- | :--- |
| **Utilities** (Age Calc, Converter) | None | Must run entirely offline. |
| **Breathing Pacer** | None | No camera or sensors needed. |
| **Step Counter** | `activity_recognition` | Required to query step sensor API. |
| **Simple Alarm Clock** | `schedule_exact_alarm` | Required to fire alarms at precise times (Target SDK 35 compliance). |

---

## 5. Ad Policy Guardrails

*   **No Accidental Clicks**: Do not place banner ads directly below or above interactive buttons (e.g., a "Save" button should be separated by at least 24dp of space from a banner).
*   **No Deceptive Loading**: Never show an interstitial ad during a loading screen unless the user has been shown a count-down warning.
*   **Splash Screen Ads**: App Open ads must not be shown during splash screens that take less than 1.5 seconds to load.

---

## 6. Closed Testing Compliance

All new applications must undergo a **14-day closed testing track** before production launch:
*   At least **20 testers** must opt-in to the release.
*   Testers must actively interact with the application. The Play Console tracks active installs and app launches.
*   Do not request production access until the 14th day of testing is fully complete.
