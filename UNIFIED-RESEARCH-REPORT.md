# SAVIOR SYSTEMS ANDROID PORTFOLIO - UNIFIED MASTER RESEARCH REPORT
**The Ultimate Strategic Source of Truth for High-Velocity App Publishing & Monetization**
```
---
```
## 1. Executive Summary & McKinsey-Style Strategy
```
This document serves as the absolute **Source of Truth** for Savior Systems' Android app factory operations. The core objective is the rapid build-out, deployment, and programmatic monetization of a diverse portfolio of utilities, productivity tools, and localized South Asian applications. 
```
Mobile publishing in 2026/2027 operates under intense structural constraints:
1.  **Google Play Console Mandates**: Personal developer accounts must secure **12 opted-in testers for 14 continuous days** prior to production release. 
2.  **Algorithmic Spam & Repetitive Content Audits**: The removal of 1.75 million apps in 2025 indicates that traditional reskinning is obsolete.
3.  **Strict Verification Rollout**: Continuous verification demands strict operational security and distinct codebase namespaces to prevent cross-account contamination.
```
### The Savior Core-and-Clone Strategy
To bypass policy blocks while maintaining rapid publishing velocities, Savior Systems implements the **Hybrid Reusable Template (Option D)** approach:
*   A single, optimized foundational codebase contains shared modules (AdMob Wrapper, UMP GDPR Consent Flow, Local Room Helpers, WorkManager Alerts).
*   Each app is instantiated in its own isolated repository with a unique visual layout, contrasting color scheme, custom typography, distinct naming conventions, and standalone assets to bypass automated clone detection.
*   The portfolio is systematically balanced between **High-Yield Tier-1 Utilities** (targeting US, UK, CA, AU, JP, DE, Nordics for $5.00–$30.00+ eCPMs) and **Localized South Asian Dominators** (targeting Bangladesh and India for high organic volume, offsetting lower $0.20–$2.00 eCPMs).
```
---
```
## 2. Market & Monetization Intelligence: Where the Money Is
```
Mobile ad yields fragment heavily by country, session depth, and placement format. Success is driven by optimizing ARPDAU (Average Revenue Per Daily Active User) without provoking invalid traffic (IVT) limits:
```
*   **Tier-1 Markets (US, UK, CA, AU, JP, DE, Nordics)**: Yield eCPMs of **$5.00 to $30.00+** for full-screen ads. Interstitial and Rewarded formats drive 85% of this revenue. ASO focus must leverage long-tail keywords (e.g., "baking weight converter") rather than saturated terms.
*   **South Asian Markets (Bangladesh, India)**: Yield lower eCPMs of **$0.20 to $2.00**. High-density organic downloads and viral user shares compensate. In these regions, high impressions-per-session ratios from bottom banners and native layouts maintain consistent baseline revenue.
```
#### Yield Demarcations by Format:
1.  **App Open Ads**: eCPMs of $7.00–$10.00+ in Tier-1. Triggered on cold starts and background returns. Must be gated behind a 2–3 second splash screen.
2.  **Adaptive Collapsible Banners**: eCPMs of $0.50–$1.50. Best for persistent screens (calculators, text lists). Must use lifecycle-aware Compose wrappers to prevent memory leaks.
3.  **Interstitials**: eCPMs of $5.00–$8.00. Triggered exclusively at natural user transitions. 
    > [!WARNING]
    > **AdMob Invalid Traffic Protection**: A hard cap of **one Interstitial per 3 minutes (180 seconds)** must be enforced programmatically to protect account standing.
4.  **Rewarded Videos**: eCPMs of $15.00–$30.00+. Gates high-value offline operations (e.g., PDF exports >3 pages, custom font packs). Must provide a clear value-exchange dialogue.
```
---
```
## 3. Play Store Policy Guardrails & Risk Control
```
### 3.1 Zero-Permission Architecture
Heightened security reviews are avoided by enforcing a strict **Zero-Permission** layout by default:
*   **No File System Access**: Leverage Scoped Storage and system file pickers (`ActivityResultContracts.OpenDocument`).
*   **No GPS Location Access**: Use manual zip/city selectors or timezone configurations.
*   **No Mic/Camera Access**: Bypassed using system Intents (e.g., calling `ACTION_DIAL` for dialer utilities, system camera Intents for simple capture, or Google Code Scanner API for QR codes).
```
### 3.2 Metadata and ASO Originality Rules
*   **Unique Privacy Policies**: Each application must have a unique privacy policy hosted on a secure domain (e.g., distinct GitHub Pages paths) detailing the specific data scope. Do not reuse a single URL across multiple apps.
*   **Listing Distinctiveness**: Descriptions, short summaries, icons, and screenshot assets must be created from scratch. Keyword stuffing is prohibited.
```
---
```
## 4. Reusable Technical Architecture (Option D)
```
 Savior Systems uses a shared repository setup where core components are imported, and visual shells are customized:
```
```
app/
 ├── data/
 │    ├── local/
 │    │    ├── Database.kt        (Reusable Room Setup)
 │    │    └── Preferences.kt     (DataStore Settings & Consent Keys)
 ├── ui/
 │    ├── theme/
 │    │    ├── Theme.kt           (Modular Theme Color Configurations)
 │    │    ├── Color.kt
 │    │    └── Type.kt
 │    ├── components/
 │    │    ├── AdBanner.kt        (AdMob Wrapper Component)
 │    │    ├── ConsentFlow.kt     (UMP Consent Wrapper Dialog)
 │    │    └── AppLayout.kt       (Scaffold layout with built-in ad bounds)
 └── utils/
      ├── AdManager.kt            (Prefetch, Load, and Display Interstitial / App Open)
      └── Analytics.kt            (Firebase Wrapper Logging)
```
```
### Shared Code: AdManager Wrapper (with 180-second hard cap)
```kotlin
package com.saviorsystems.core.utils
```
import android.app.Activity
import android.content.Context
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback
```
object AdManager {
    private var mInterstitialAd: InterstitialAd? = null
    private var lastAdShowTime: Long = 0
    private const val AD_FREQUENCY_CAP_MS = 180_000 // 3 minutes (180s)
```
    fun loadInterstitial(context: Context, adUnitId: String) {
        if (mInterstitialAd != null) return
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
```
    fun showInterstitial(activity: Activity, adUnitId: String, onAdDismissed: () -> Unit) {
        val currentTime = System.currentTimeMillis()
        if (mInterstitialAd != null && (currentTime - lastAdShowTime >= AD_FREQUENCY_CAP_MS)) {
            mInterstitialAd?.fullScreenContentCallback = object : com.google.android.gms.ads.FullScreenContentCallback() {
                override fun onAdDismissedFullScreenContent() {
                    mInterstitialAd = null
                    lastAdShowTime = System.currentTimeMillis()
                    loadInterstitial(activity, adUnitId)
                    onAdDismissed()
                }
                override fun onAdFailedToShowFullScreenContent(adError: com.google.android.gms.ads.AdError) {
                    mInterstitialAd = null
                    onAdDismissed()
                }
            }
            mInterstitialAd?.show(activity)
        } else {
            onAdDismissed()
        }
    }
}
```
```
---
```
## 5. Master App Opportunity Matrix (Combined 50-Concept Database)
```
The following matrix integrates all app concepts proposed by ChatGPT, Gemini, and Antigravity, scored out of 10 across key strategic dimensions:
```
| ID | Concept / Suggestion Name | Primary Market | Build Time | Ad Formats | Policy Risk | Weighted Score | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | Bengali Quotes & Captions | South Asia (BD) | 2 Days | Banner + Interstitial + Rewarded | Low | **8.03** | **Selected (Top 1)** |
| **02** | Exam GPA / CGPA Calculator | South Asia (BD/IN)| 1.5 Days | Banner + Interstitial | Low | **7.78** | **Selected (Top 2)** |
| **03** | Text Art & Stylish Fonts | Global / SA | 2 Days | Banner + Interstitial + Rewarded | Low | **7.75** | **Selected (Top 3)** |
| **04** | Unit Converter: Baker's Helper | Global (Tier 1) | 2 Days | Banner + Interstitial | Low | **7.73** | **Selected (Top 4)** |
| **05** | Pomodoro Study & Break Timer | Global (Tier 1) | 2 Days | Banner + Interstitial + Custom Themes | Low | **7.68** | **Selected (Top 5)** |
| **06** | Micro-Habit Tracker | Global (Tier 1) | 3 Days | App Open + Banner + Interstitial | Low | **7.68** | **Selected (Top 6)** |
| **07** | Simple Expense & Budget Tracker | Global / SA | 3 Days | Banner + Interstitial + CSV Export | Low | **7.63** | **Selected (Top 7)** |
| **08** | Image Compressor & Resizer | Global (Tier 1) | 2.5 Days | Banner + Interstitial + Batch Convert | Low | **7.53** | **Selected (Top 8)** |
| **09** | Image to PDF Converter | Global (Tier 1) | 3 Days | Banner + Interstitial + Rewarded | Low | **7.45** | **Selected (Top 9)** |
| **10** | English-Bengali Flashcards | South Asia (BD) | 3 Days | Banner + Interstitial | Low | **7.45** | **Selected (Top 10)** |
| **11** | Local VAT & Tax Estimator | South Asia (BD) | 2 Days | Banner + Interstitial + Rewarded | Low | **7.43** | **Selected (Top 11)** |
| **12** | PDF Merger & Page Extractor | Global (Tier 1) | 3 Days | Banner + Interstitial + Rewarded | Low | **7.30** | **Selected (Top 12)** |
| **13** | Fuel Mileage & Trip Calculator | Global / SA | 4 Days | Banner + Interstitial | Low | **6.55** | Reserve (Top 13) |
| **14** | English-Bangla Vocab | South Asia (BD) | 3 Days | Banner + Interstitial | Low | **7.45** | Reserve (Top 14) |
| **15** | Breathing Pacer | Global (Tier 1) | 2 Days | Banner only | Low | **7.60** | Reserve (Top 15) |
| **16** | WiFi QR Sharer | Global | 2 Days | Banner + Interstitial | Low | **7.15** | Reserve (Top 16) |
| **17** | Exam Countdown BD | South Asia (BD) | 2 Days | Banner + Interstitial | Low | **7.00** | Reserve (Top 17) |
| **18** | Daily Quotes Maker | Global | 4 Days | Banner + Rewarded | Medium | **7.10** | Reserve (Top 18) |
| **19** | Device Info Specs | Global | 3 Days | Banner + Interstitial | Low | **6.80** | Reserve (Top 19) |
| **20** | Outfit Canvas | Global (Tier 1) | 7 Days | Banner + Interstitial | Low | **6.85** | Reserve (Top 20) |
| **21** | ScanMaster Offline | Global | 3 Days | Banner + Interstitial | Low | **7.08** | Reserve (Top 21) |
| **22** | Color Hex Picker | Global | 2 Days | Banner + Rewarded | Low | **6.93** | Reserve (Top 22) |
| **23** | BMI & BMR Target | Global | 2 Days | Banner + Interstitial | Low | **6.98** | Reserve (Top 23) |
| **24** | Tip & Split Pro | Global (Tier 1) | 2 Days | Banner only | Low | **6.05** | Reserve (Top 24) |
| **25** | InstaGrid Splitter | Global | 4 Days | Banner + Rewarded | Medium | **6.40** | Reserve (Top 25) |
| **26** | Offline Vault & Pass | Global | 3 Days | Banner only | Low | **5.80** | Reserve (Top 26) |
| **27** | Offline Voice Note | Global | 4 Days | Banner + Interstitial | Medium | **6.60** | Reserve (Top 27) |
| **28** | Social Bio & Status Captions | India / Global | 3 Days | Banner + Interstitial | High | **4.00** | Reserve (Top 28) |
| **29** | Auto Text Spammer | Global | 2 Days | Banner + Interstitial | High | **4.20** | Reserve (Top 29) |
| **30** | Fake Call Rescue | Global | 4 Days | Interstitial | High | **4.50** | Reserve (Top 30) |
| **31** | Smart Age & BD Date Utility | South Asia (BD) | 2 Days | Banner + Interstitial | Low | **7.40** | Reserve (Top 31) |
| **32** | Routine Timeline Widget | Global (Tier 1) | 5 Days | Banner + App Open | Low | **7.38** | Reserve (Top 32) |
| **33** | Water Log & Remind Express | Global (Tier 1) | 3 Days | Banner + App Open | Low | **7.35** | Reserve (Top 33) |
| **34** | Resume PDF Maker | Global / SA | 7 Days | Banner + Rewarded | Low | **7.20** | Reserve (Top 34) |
| **35** | PDF Compress Lite | Global (Tier 1) | 6 Days | Banner + Rewarded | Low | **7.15** | Reserve (Top 35) |
| **36** | Baby Name Finder & Meanings | Global / SA | 5 Days | Banner only | Low | **6.90** | Reserve (Top 36) |
| **37** | Outfit Canvas / Wardrobe Guide | Global (Tier 1) | 7 Days | Banner + Interstitial | Low | **6.85** | Reserve (Top 37) |
| **38** | Offline Voice Note Recorder | Global | 4 Days | Banner + Interstitial | Medium | **6.60** | Reserve (Top 38) |
| **39** | InstaGrid Slicing Helper | Global | 4 Days | Banner + Rewarded | Medium | **6.40** | Reserve (Top 39) |
| **40** | WiFi Signal Strength Grapher | Global | 4 Days | Banner + Interstitial | High | **5.90** | Rejected |
| **41** | Morse Code Translator | Global (Tier 1) | 3 Days | Banner + Interstitial | Low | **6.75** | Backup |
| **42** | Simple Packing Checklist | Global (Tier 1) | 2 Days | Banner only | Low | **7.18** | Backup |
| **43** | QR Code Generator & Wifi Connect | Global (Tier 1) | 3 Days | Banner + Interstitial | Low | **7.08** | Backup |
| **44** | Salary Splitter / Savings Planner | Global / SA | 3 Days | Banner + Interstitial | Low | **7.05** | Backup |
| **45** | Recipe Offline Box | Global (Tier 1) | 5 Days | Banner + Interstitial | Low | **6.20** | Backup |
| **46** | Wedding Checklist Countdown | Global (Tier 1) | 3 Days | Banner only | Low | **6.15** | Backup |
| **47** | Mobile Package Compare BD | South Asia (BD) | 4 Days | Banner + Interstitial | Low | **6.10** | Backup |
| **48** | Currency Converter Offline | Global | 3 Days | Banner + Interstitial | Low | **6.05** | Backup |
| **49** | Exam Countdown widget BD | South Asia (BD) | 2 Days | Banner + Interstitial | Low | **6.00** | Backup |
| **50** | Word Counter & Character Analyzer| Global (Tier 1) | 2 Days | Banner + Native | Low | **5.95** | Backup |
```
---
```
## 6. Top 12 Selected Apps Dossier (Detailed Execution Specs)
```
### 01. FocusPulse Timer
*   **Description**: A minimalist Pomodoro timer built with Compose and Room.
*   **Key Trigger**: On study session completion -> Interstitial (180s cap); Themes gated by Rewarded video.
*   **Competitors**: "Focusmeter" (4.6 stars, 500K+ downloads), "Pomocat" (4.5 stars, 100K+ downloads). Gaps: Heavy battery drain and complex configuration.
*   **ASO Keywords**: Pomodoro timer, study timer, ADHD focus tracker, study clock.
```
### 02. BD Varsity CGPA Pro
*   **Description**: Calculator for private/public universities in Bangladesh with custom grading tables.
*   **Key Trigger**: On calculation result -> Interstitial.
*   **Competitors**: "Green CGPA Calculator" (4.3 stars, 50K+ downloads). Gaps: Messy UI, out-of-date curves.
*   **ASO Keywords**: BD CGPA calculator, National University grading, CGPA pro BD.
```
### 03. MicroHabit Tracker
*   **Description**: Streak-based routine tracker with local notifications via WorkManager.
*   **Key Trigger**: App Open ad on startup; Banners at check-in.
*   **Competitors**: "Loop Habit Tracker" (4.7 stars, 1M+ downloads). Gaps: Loop lacks modern color customizations and is shifting to subscription constraints.
*   **ASO Keywords**: Habit tracker, streak calendar, micro routine, daily goal.
```
### 04. Expense Diary Local
*   **Description**: Ledger for expense tracking using Room DB and MPAndroidChart.
*   **Key Trigger**: On database export to CSV -> Rewarded ad; bottom Adaptive Banner.
*   **Competitors**: "Monefy" (4.5 stars, 5M+ downloads). Gaps: Saturated with cloud syncing requirements and paywalled charts.
*   **ASO Keywords**: Daily budget offline, local expense ledger, money diary.
```
### 05. Prayer Time Helper
*   **Description**: Time calculations using Astronomical Algorithms based on city selection (Zero-Permission).
*   **Key Trigger**: Adaptive bottom banner.
*   **Competitors**: "Muslim Pro" (4.4 stars, 100M+ downloads). Gaps: Massive background syncs, privacy scandals (selling location data).
*   **ASO Keywords**: Prayer times offline, Salat helper, Qibla compass city.
```
### 06. Water Log & Remind
*   **Description**: Glass logger tracking daily hydration metrics.
*   **Key Trigger**: Clicking "Log Glass" -> 180s-capped Interstitial.
*   **Competitors**: "Water Reminder" (4.6 stars, 10M+ downloads). Gaps: Irritating push alarms every 30 mins.
*   **ASO Keywords**: Water log reminder, drink water tracker, hydrate helper.
```
### 07. Smart Age & BD Date
*   **Description**: Gregoran-to-Bengali calendar and age matching.
*   **Key Trigger**: On calculation -> Interstitial.
*   **Competitors**: Bangladesh government utility apps (very poor UI, broken layouts).
*   **ASO Keywords**: Bengali age calculator, Gregorian date BD.
```
### 08. Resume PDF Maker
*   **Description**: PDF generator converting local input fields into structured layouts.
*   **Key Trigger**: On PDF creation -> Rewarded ad.
*   **Competitors**: "Resume Builder App" (4.5 stars, 1M+ downloads). Gaps: Puts heavy watermarks on free tiers.
*   **ASO Keywords**: Free CV builder, watermark-free resume, PDF CV maker.
```
### 09. PDF Compress Lite
*   **Description**: Multi-image compressor utilizing system bitmap compression matrices.
*   **Key Trigger**: PDF generation finished -> Rewarded ad.
*   **Competitors**: "iLovePDF" (4.4 stars, 5M+ downloads). Gaps: Requires remote upload.
*   **ASO Keywords**: Compress PDF offline, shrink image attachment.
```
### 10. Routine Widget
*   **Description**: Visual daily timeline widget using Jetpack Glance.
*   **Key Trigger**: Opening widget config -> App Open ad; bottom banner on settings.
*   **Competitors**: "Widgetopia" (4.3 stars, 500K+ downloads). Gaps: Saturated with complicated widgets; lack pure offline routine widgets.
*   **ASO Keywords**: Routine widget, home screen schedule.
```
### 11. BD Tax & VAT Calc
*   **Description**: Income tax/VAT estimator according to current national budget regulations.
*   **Key Trigger**: On calculation -> Interstitial; Premium PDF prints gated by Rewarded.
*   **Competitors**: Static government websites (non-responsive).
*   **ASO Keywords**: BD income tax calculator, VAT estimator Bangladesh.
```
### 12. Minimalist To-Do
*   **Description**: Swipe-based task card tracker.
*   **Key Trigger**: Completing task sets -> Interstitial (180s cap).
*   **Competitors**: "Todoist" (4.6 stars, 10M+ downloads). Gaps: Lock basic lists behind monthly subscriptions.
*   **ASO Keywords**: Minimalist todo, task list swipe, simple checklist.
```
---
```
## 7. AI Agent Operating System (OS) & Directory Setup
```
We synchronize Antigravity, Cursor, Codex, and GitHub Copilot by maintaining a strict hierarchy of context rules:
```
*   **Ultimate Authority (`.claude/CLAUDE.md`)**: Directs AI assistants to restrict architectures to MVVM, local Room caching, AdMob wrappers, and zero-permission setups. It explicitly forbids paid API dependencies.
*   **Rules Engine (`.claude/rules.md`)**: Houses standard conventions (Conventional Commits, Kotlin styles).
*   **Prompts Repository (`.claude/prompts/`)**: Includes templates for generating app-specific markdown suites.
```
---
```
## 8. Staggered Launch & closed-testing Roadmap
```
To fulfill Google's closed-testing tracks (12 testers for 14 continuous days):
```
```
Week 1 (Days 1-7): Savior-Core-Template Development (Consent SDK, AdManager)
Week 2 (Days 8-10): App 01 Build ──► Submit Closed Testing track (14-day hold starts)
Week 2-3 (Days 11-20): Build App 02, App 03, App 04 ──► Submit closed testing sequentially
Week 4 (Day 25+): App 01 closed-testing complete ──► Launch Production track
Week 4-5 (Day 28+): Launch App 02, App 03, App 04 on rolling cycles
```
```
---
```
## 9. App #1 Starter Pack: FocusPulse Timer
```
The folder `01. FocusPulse Timer` is fully generated and ready to receive code.
```
### 00-START-HERE.md
*   **Summary**: A minimalist Pomodoro timer.
*   **Key Hypotheses**: eCPM maximized by triggering Interstitials only on break transition cycles.
*   **Tech Stack**: Jetpack Compose, Room Database, ViewModel, Kotlin Coroutines, AdMob SDK.
```
---
```
## 10. Next Execution Prompt
```
Run the following prompt inside your IDE/Agent terminal to generate App #2 docs:
```
Agent, read the global PORTFOLIO-STRATEGY context. Generate the documentation suite for '02. BD Varsity CGPA Pro' inside its folder. Maintain a local-first offline storage concept, optimize ASO keywords for private and national universities in Bangladesh, and define ad triggers protecting high-frequency data inputs.
```
```