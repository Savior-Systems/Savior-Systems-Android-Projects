# Guide: Firebase Integration Standard

This guide defines the standard setup for Firebase Analytics and Crashlytics across all Savior Systems apps.

---

## 1. Project Configuration
- **GCP Project**: `hopeful-breaker-426606-h9`
- **Firebase Console**: All 30 apps are registered under a single Firebase project for centralized monitoring.
- **Config File**: Each app's `google-services.json` is placed in its `app/` directory. Never commit this file to public repos.

---

## 2. Firebase BOM Setup (Gradle)

```kotlin
// libs.versions.toml
[versions]
firebase-bom = "33.0.0"

[libraries]
firebase-bom = { group = "com.google.firebase", name = "firebase-bom", version.ref = "firebase-bom" }
firebase-analytics = { group = "com.google.firebase", name = "firebase-analytics-ktx" }
firebase-crashlytics = { group = "com.google.firebase", name = "firebase-crashlytics-ktx" }
```

---

## 3. Custom Event Naming Convention

All custom events follow the snake_case convention:

```
<action>_<object>
```

Examples:
- `onboarding_completed`
- `water_logged`
- `alarm_configured`
- `goal_achieved`
- `streak_milestone`

---

## 4. PII Rules (Non-Negotiable)

These rules apply across ALL 30 apps:

| Rule | Enforcement |
| :--- | :--- |
| ❌ NEVER log user's name | No registration exists, so this is N/A. |
| ❌ NEVER log exact GPS coordinates | Only log country_code from geocoder. |
| ❌ NEVER log exact weight/height | Only log bucketed ranges (e.g., "60-70kg"). |
| ❌ NEVER log exact financial amounts | Only log bucketed ranges. |
| ✅ Log event names and buckets | Safe for analytics without privacy risk. |
| ✅ Log user properties (preferences) | E.g., "preferred_unit: ML", "calc_method: KARACHI". |

---

## 5. Crashlytics Context Keys Standard

Every app should set these standard Crashlytics keys on startup:

```kotlin
Firebase.crashlytics.setCustomKey("app_version", BuildConfig.VERSION_NAME)
Firebase.crashlytics.setCustomKey("dark_mode", isSystemDarkMode)
Firebase.crashlytics.setCustomKey("locale", Locale.getDefault().language)
```

App-specific keys (e.g., sensor availability, alarm permissions) are defined in each app's `12.LOGGING-ANALYTICS.md`.
