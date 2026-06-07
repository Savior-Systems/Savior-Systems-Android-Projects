# Skill: Permissions & Data Safety Form Generator

## Purpose
Generates a pre-filled Google Play Data Safety form declaration based on the permissions and SDK integrations declared in an app's `08.PLAY-POLICY-SAFETY.md`.

## When to Use
- Before submitting an app to the Google Play Console.
- When the user asks to generate Data Safety form responses.
- During the Play Policy audit workflow.

## Data Safety Categories

### Standard Declarations (Present in ALL Savior Systems Apps)

| Category | Data Type | Collected | Shared | Purpose | Encryption | Deletable |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **App Activity** | App interactions | Yes | No | Analytics (Firebase) | Yes (HTTPS) | Yes (Clear App Data) |
| **Device IDs** | Device or other IDs | Yes | Yes (AdMob, Firebase) | Advertising, Analytics | Yes (HTTPS) | Yes |

### Conditional Declarations

| Trigger | Category | Data Type | When to Declare |
| :--- | :--- | :--- | :--- |
| Uses GPS location | **Location** | Approximate location | If `ACCESS_COARSE_LOCATION` is in manifest |
| User inputs weight/height | **Health & Fitness** | Fitness info | If app calculates BMI, hydration goals, etc. |
| User inputs financial data | **Financial Info** | Financial info | If app tracks expenses, income, taxes |
| User creates text content | **Personal Info** | Name, email | If app stores user profile data |

### Data NOT Collected (Declare "No" for ALL apps)
- ❌ Messages
- ❌ Photos & Videos
- ❌ Audio files
- ❌ Files & docs (unless explicitly needed like PDF apps)
- ❌ Calendar
- ❌ Contacts
- ❌ Web browsing data

## Questionnaire Responses

### Q: "Does your app collect or share any of the required user data types?"
**A**: Yes — Device IDs (for AdMob/Firebase).

### Q: "Is all of the user data collected by your app encrypted in transit?"
**A**: Yes — All SDK communication uses HTTPS/TLS.

### Q: "Do you provide a way for users to request that their data is deleted?"
**A**: Yes — Users can clear all data by clearing app storage in Android Settings. In-app "Reset Data" option is also available in Settings screen.

### Q: "Is your app a game?"
**A**: No.

## Agent Instructions
1. Read the app's `08.PLAY-POLICY-SAFETY.md` to identify all declared permissions and SDKs.
2. Map each permission to the appropriate Data Safety category from the tables above.
3. Generate a filled-out Data Safety declaration table.
4. Flag any permissions that are missing from `08.PLAY-POLICY-SAFETY.md` but are present in the manifest.
