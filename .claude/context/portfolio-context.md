# Portfolio Context: Savior Systems

## Organization
- **Publisher**: Savior Systems
- **GCP Project ID**: `hopeful-breaker-426606-h9`
- **GitHub Repo**: `Savior-Systems/Savior-Systems-Android-Projects`
- **Total Apps**: 30 isolated Android utilities.
- **Documentation Standard**: 14 blueprint files per app (PRD → Backlog + README).

---

## Region eCPM Reference (AdMob Estimates)

| Region | Banner eCPM | Interstitial eCPM | Rewarded eCPM | Primary Apps |
| :--- | :--- | :--- | :--- | :--- |
| **US/UK/CA/AU** (Tier-1) | $1.00–$2.00 | $6.00–$12.00 | $15.00–$25.00 | Water Tracker, Breathing Pacer, BMI Target, Resume Maker |
| **BD/IN/PK** (High-Volume) | $0.10–$0.20 | $0.50–$1.00 | $1.50–$3.00 | Prayer Time, Exam Countdown BD, BD Tax Calc, Bangla Vocab |
| **EU (GDPR)** | $0.80–$1.50 | $5.00–$10.00 | $12.00–$20.00 | Expense Diary, Fuel Mileage, Color Picker |

---

## Reusable Library & SDK Versions

| Dependency | Min Version | Notes |
| :--- | :--- | :--- |
| Kotlin | 2.0+ | Use K2 compiler. |
| Compose BOM | 2024.06+ | Always use BOM for version alignment. |
| Hilt | 2.51+ | Required for all DI. |
| Room | 2.6+ | Required for all local DB. |
| DataStore | 1.1+ | Use Preferences DataStore, not Proto. |
| Google Mobile Ads | 23.0+ | Always initialize via `MobileAds.initialize()`. |
| Firebase BOM | 33.0+ | For Analytics + Crashlytics. |
| UMP SDK | 3.0+ | IAB TCF v2.3 GDPR consent. |

---

## Cross-App Color Uniqueness Matrix

To prevent Play Store "Repetitive Content" rejections, every app must use a distinct primary palette:

| App # | App Name | Primary Color | Hex |
| :--- | :--- | :--- | :--- |
| 01 | FocusPulse Timer | Warm Amber | `#FF8F00` |
| 02 | English-Bangla Vocab | Deep Indigo | `#283593` |
| 03 | MicroHabit Tracker | Vibrant Teal | `#00897B` |
| 04 | Expense Diary Local | Rich Purple | `#6A1B9A` |
| 05 | Prayer Time Helper | Deep Emerald Green | `#00695C` |
| 06 | Water Log & Remind | Clear Ocean Blue | `#0288D1` |
| 07 | Smart Age & BD Date | Warm Rose | `#AD1457` |
| 08 | Resume PDF Maker | Corporate Navy | `#1A237E` |
| 09 | PDF Compress Lite | Crimson Red | `#C62828` |
| 10 | Routine Widget | Sunset Orange | `#E65100` |
| 11 | BD Tax & VAT Calc | Forest Green | `#2E7D32` |
| 12 | Minimalist To-Do | Charcoal Gray | `#37474F` |
| 13 | Fuel Mileage Log | Petroleum Blue | `#01579B` |
| 14 | English-Bangla Vocab | Deep Indigo | `#283593` |
| 15 | Breathing Pacer | Lavender Calm | `#7E57C2` |
| 16 | WiFi QR Sharer | Electric Cyan | `#00ACC1` |
| 17 | Exam Countdown BD | Academic Maroon | `#880E4F` |
| 18 | Daily Quotes Maker | Marigold Gold | `#F9A825` |
| 19 | Device Info Specs | Steel Blue | `#455A64` |
| 20 | Outfit Canvas | Blush Pink | `#EC407A` |

*Note: Apps 21–30 will be assigned unique palettes during their blueprint phase.*
