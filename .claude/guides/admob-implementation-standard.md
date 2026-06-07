# Guide: AdMob Implementation Standard

This guide defines the exact rules for implementing Google Mobile Ads across all Savior Systems apps.

---

## 1. SDK Initialization

```kotlin
// In Application class or MainActivity.onCreate()
MobileAds.initialize(this) { initStatus ->
    // Ad SDK is ready. Now safe to load ads.
}
```

**CRITICAL**: Never load an ad before `MobileAds.initialize()` completes. Doing so causes silent failures and zero fill rates.

---

## 2. UMP Consent Flow (GDPR)

For EU users, you MUST resolve consent before loading any ads:

```kotlin
val consentInfo = UserMessagingPlatform.getConsentInformation(activity)
val params = ConsentRequestParameters.Builder()
    .setTagForUnderAgeOfConsent(false)
    .build()

consentInfo.requestConsentInfoUpdate(activity, params, {
    if (consentInfo.canRequestAds()) {
        loadAds()
    }
}, { error -> /* Handle error */ })
```

---

## 3. Ad Format Rules

### Banners
- Use `AdaptiveBannerAdSize` (NOT fixed size banners — they waste screen space or overflow).
- Place at the bottom of the screen, above the bottom navigation bar.
- Never place banners that overlap interactive elements.

### Interstitials
- Every app MUST define a minimum cooldown timer (typically 3–4 hours).
- NEVER show interstitials on app open.
- NEVER show interstitials immediately after a user completes a positive action (e.g., logging water, completing a habit). Wait for a natural transition (e.g., exiting settings).
- Pre-load the next interstitial immediately after showing one.

### Rewarded (If Used)
- Only use in apps where a natural "reward" exists (e.g., unlocking a premium theme).
- Always clearly communicate what the user gets before they watch.

---

## 4. Test Ad Unit IDs (Development Only)

| Format | Test ID |
| :--- | :--- |
| Banner | `ca-app-pub-3940256099942544/6300978111` |
| Interstitial | `ca-app-pub-3940256099942544/1033173712` |
| Rewarded | `ca-app-pub-3940256099942544/5224354917` |

**CRITICAL**: Never ship production builds with test IDs. Use `BuildConfig` fields injected from `local.properties`.

---

## 5. Content Category Blocks

Block the following sensitive ad categories across ALL apps:
- Gambling & Betting
- Dating & Relationships
- Alcohol & Tobacco
- Political Content
- Cryptocurrency

For health-focused apps (Water Tracker, BMI, Breathing Pacer), also block:
- Fast Food & Junk Food ads
