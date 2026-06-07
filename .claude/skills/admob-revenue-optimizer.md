# Skill: AdMob Revenue Optimizer

## Purpose
Analyzes and recommends optimizations for AdMob placements, ad formats, and mediation configurations to maximize eCPM without severely degrading the user experience.

## When to Use
- When generating `06.ADMOB-MONETIZATION-MAP.md`.
- When the user asks to "improve revenue" or "optimize ads".

## Execution Strategy

### 1. Format Selection
- **App Open Ads**: Only recommend for high-engagement apps (e.g., VPNs, tools opened daily). Do NOT recommend for quick utility apps where users expect instant interaction.
- **Adaptive Banners**: Always specify `AdaptiveBannerAdSize` to maximize fill rate and screen real estate.
- **Native Advanced**: Recommend placing Native Ads inside RecyclerViews (lists, timelines) as they have 2-3x higher CTR than banners.
- **Rewarded Interstitials**: Introduce gated premium features (e.g., unlocking a PDF template) behind a rewarded video.

### 2. Frequency Capping
- Define strict capping based on the app category.
- High-utility (e.g., calculators): 1 interstitial per hour.
- Content-heavy (e.g., quotes): 1 interstitial per 5 minutes.

### 3. Floor eCPM Configuration
- Recommend setting up eCPM floors (e.g., High, Medium, All Prices) in the AdMob console for Tier-1 regions to prevent low-value ads from degrading UX.

## Output
Produce the content structured exactly as required by the 14-document standard for `06.ADMOB-MONETIZATION-MAP.md` or provide a standalone optimization report.
