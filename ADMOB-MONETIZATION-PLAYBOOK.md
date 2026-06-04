# Savior Systems: AdMob Monetization Playbook

This document is the absolute blueprint for integrating and optimizing Google AdMob across Savior Systems' 30+ Android applications.

---

## 1. Account & Ad Unit Structure

To maintain clean reporting, simple billing, and minimize compliance risks, all apps will monetize under a single, verified Savior Systems Google AdMob account.

### Ad Unit Naming Convention
Every ad unit must be explicitly named using the pattern:
`[AppName]_[Format]_[Placement]`

Examples:
*   `focuspulse_banner_home`
*   `focuspulse_interstitial_session_complete`
*   `focuspulse_appopen_startup`
*   `varsitycgpa_rewarded_premium_theme`

### Ad Unit Configuration Table
| Format | Naming Code | AdMob Settings | Optimization Setting |
| :--- | :--- | :--- | :--- |
| **Adaptive Banner** | `_banner_` | Smart Banner Enabled, 45s refresh | High eCPM Floor (Tier-1), Google Optimized (Tier-2) |
| **Interstitial** | `_interstitial_` | Frequency Cap: 1 per 180s | Medium eCPM Floor, Text/Image/Video Allowed |
| **App Open** | `_appopen_` | Limit: 1 per 60s cooldown | Google Optimized Floor, Preload immediately |
| **Rewarded** | `_rewarded_` | No cap, set reward value | Single reward item, reward callback required |

---

## 2. Ad Formats & Placement Strategies

Each application type requires a tailored ad placement blueprint to balance user experience and revenue.

```
┌────────────────────────────────────────────────────────┐
│               Ad Placement Best Practices             │
├───────────────────────┬────────────────────────────────┤
│ Utility / Calculators │ Timers / Pomodoro / Logs       │
│ - Banner: Bottom      │ - Banner: Bottom               │
│ - Interstitial: Rare  │ - Interstitial: Session End    │
│ - App Open: Enabled   │ - App Open: Enabled            │
└───────────────────────┴────────────────────────────────┘
```

### Banner Ads (Adaptive Banners)
*   **Placement**: Anchored at the bottom of the main utility screen.
*   **Best Practice**: Use Compose `AnchoredAdaptiveBanner` which dynamically calculates the width and requests the appropriate banner size. Never overlay banners over clickable buttons.

### Interstitial Ads (Full-screen Ads)
*   **Placement**: Triggered only after transition points:
    *   *FocusPulse Timer*: When the timer finishes and user clicks "Done".
    *   *MicroHabit Tracker*: After a habit is checked off.
    *   *Resume PDF Maker*: After the PDF generation is complete and saved.
*   **Cap Rules**: Implement a strict programmatic cooldown of **180 seconds**. If the user completes another action before the cooldown expires, suppress the ad.

### App Open Ads (AOA)
*   **Placement**: Displayed during cold app starts or when returning from the background.
*   **Best Practice**: Delay showing the ad until the splash screen is visible for at least 1.5 seconds. If the app is returning from a brief background state (e.g., checking a SMS verification code), suppress the ad.

### Rewarded Ads
*   **Placement**: Used exclusively to unlock premium items:
    *   Advanced color themes (e.g., in *Color Hex Picker* or *Routine Widget*).
    *   Advanced exports (e.g., CSV export in *Expense Diary Local*).
*   **Best Practice**: Offer a clear benefit message to the user: *"Watch a quick ad to unlock Premium Dark Theme for 24 hours."*

---

## 3. High-eCPM Optimization

*   **EEA / UK Consent (GDPR)**: Integrate Google's User Messaging Platform (UMP) SDK. If consent is denied, fall back to non-personalized ads automatically.
*   **Mediation Network Setup**:
    *   **Primary**: Google AdMob.
    *   **Mediation Partners**: Meta Audience Network, Unity Ads, Pangle.
    *   **Fallback**: Set up bidding integration with Meta Audience Network to compete with Google's internal bidding system.

---

## 4. Technical Integration Code Pattern

All apps should utilize a unified helper class. Below is the Kotlin implementation template:

```kotlin
package com.saviorsystems.core.ads

import android.app.Activity
import android.content.Context
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback
import java.util.concurrent.TimeUnit

object AdManager {
    private var mInterstitialAd: InterstitialAd? = null
    private var lastInterstitialShowTime: Long = 0
    private const val COOLDOWN_MILLIS = 180_000L // 180 seconds

    fun loadInterstitial(context: Context, adUnitId: String) {
        val adRequest = AdRequest.Builder().build()
        InterstitialAd.load(context, adUnitId, adRequest, object : InterstitialAdLoadCallback() {
            override fun onAdFailedToLoad(adError: LoadAdError) {
                mInterstitialAd = null
            }

            override fun onAdLoaded(interstitialAd: InterstitialAd) {
                mInterstitialAd = interstitialAd
            }
        })
    }

    fun showInterstitial(activity: Activity, onAdDismissed: () -> Unit) {
        val currentTime = System.currentTimeMillis()
        if (mInterstitialAd != null && (currentTime - lastInterstitialShowTime >= COOLDOWN_MILLIS)) {
            mInterstitialAd?.fullScreenContentCallback = object : com.google.android.gms.ads.FullScreenContentCallback() {
                override fun onAdDismissedFullScreenContent() {
                    mInterstitialAd = null
                    lastInterstitialShowTime = System.currentTimeMillis()
                    onAdDismissed()
                    // Preload the next ad
                    loadInterstitial(activity, "ca-app-pub-3940256099942544/1033173712") // Use real ID in production config
                }

                override fun onAdFailedToShowFullScreenContent(adError: com.google.android.gms.ads.AdError) {
                    mInterstitialAd = null
                    onAdDismissed()
                }
            }
            mInterstitialAd?.show(activity)
        } else {
            // Suppressed due to cooldown or ad not loaded
            onAdDismissed()
        }
    }
}
```

---

## 5. Monetization Launch Checklist

1.  [ ] Real AdMob App IDs and Ad Unit IDs are defined in `secrets.properties` or `build.gradle.kts` (never hardcoded in strings).
2.  [ ] Test Ad Units are active in `debug` build variant.
3.  [ ] Real Ad Units are active in `release` build variant.
4.  [ ] AdMob app-ads.txt is successfully published on the developer website root domain.
5.  [ ] COPPA (Children's Online Privacy Protection) parameters set to false (not targeted at children under 13).
6.  [ ] Google UMP SDK integration verified for GDPR-regulated countries.
