# Skill: Play Store Policy Auditor

## Purpose
Executes a strict audit of the app's documentation or codebase against Google Play Store policies to prevent rejections or suspensions.

## When to Use
- Before finalizing `08.PLAY-POLICY-SAFETY.md`.
- Before generating the final app bundle (AAB) for release.
- When the user asks to "check for policy violations".

## Audit Execution Steps

### 1. Permissions Audit
- Scan `AndroidManifest.xml` (or `08.PLAY-POLICY-SAFETY.md`).
- Flag `ACCESS_BACKGROUND_LOCATION`. (Reject unless strictly required and justified).
- Flag `SCHEDULE_EXACT_ALARM`. (Recommend moving to WorkManager/inexact alarms if possible).
- Flag `READ_EXTERNAL_STORAGE` / `WRITE_EXTERNAL_STORAGE` on Android 13+. (Must use PhotoPicker or MediaStore instead).

### 2. Ad Policy Audit
- Scan `06.ADMOB-MONETIZATION-MAP.md` or AdMob implementation code.
- Check: Are interstitials shown on app open? (Reject).
- Check: Are interstitials shown when the user clicks a back button? (Reject).
- Check: Is there a cooldown mechanism? (Require at least 3 minutes).

### 3. Metadata Audit
- Scan `07.ASO-PLAY-STORE-LISTING.md`.
- Check: Does the title contain "Free", "Best", "Top", or "#1"? (Reject).
- Check: Are emojis used excessively? (Warn).
- Check: Are there repetitive keyword lists? (Reject as keyword stuffing).

## Output
Generate a clear, bulleted report of PASSED, WARNING, and FAILED checks. If FAILED, provide the exact code or markdown changes needed to resolve the violation.
