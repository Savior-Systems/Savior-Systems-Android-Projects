# Prompt: Play Store Policy Risk Audit

Use this prompt to audit an app's codebase, permissions, and store listing against Google Play policies before submission.

---

## Prompt

```
Act as a Google Play Store Policy Compliance Analyst.

Audit the following app against the latest Google Play Developer Program Policies:

App: [APP_NAME]
Directory: [APP_DIRECTORY]

Perform the following checks:

1. **Permissions Audit**: Review `08.PLAY-POLICY-SAFETY.md`. Flag any permissions that are:
   - Not justified by a core feature.
   - Dangerous permissions (location, camera, microphone) without a runtime rationale string.
   - Background permissions (ACCESS_BACKGROUND_LOCATION) — these are almost always rejected.

2. **Data Safety Form**: Verify the Data Safety table in `08.PLAY-POLICY-SAFETY.md`:
   - Is all collected data accurately declared?
   - Is the "Can users request deletion?" question answered?
   - Are third-party SDKs (AdMob, Firebase) properly disclosed?

3. **Store Listing Compliance**: Review `07.ASO-PLAY-STORE-LISTING.md`:
   - Does the title contain misleading claims (e.g., "Best", "#1", "Free")?
   - Is the description keyword-stuffed?
   - Does the description make medical/health claims without a proper disclaimer?

4. **Repetitive Content / Spam Risk**: Compare the app's color palette, icon design, and description against other apps in the portfolio. Flag any similarity that could trigger Google's "Repetitive Content" policy.

5. **Ad Placement Compliance**: Review `06.ADMOB-MONETIZATION-MAP.md`:
   - Are interstitials triggered on app open? (Violation)
   - Do ads cover interactive elements? (Violation)
   - Is there a frequency cap defined? (Required)

Output a structured compliance report with:
- ✅ PASS items
- ⚠️ WARNING items (review recommended)
- ❌ FAIL items (must fix before submission)
```
