# Savior Systems gotchas

Common traps and solutions for developer awareness:

- **AdMob SDK Crash**: Initializing the AdMob SDK without registering `<meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="..."/>` in `AndroidManifest.xml` triggers an instant crash on start.
- **GDPR Consent Rejection**: Displaying a banner or loading an interstitial *before* resolving the UMP Consent loop violates EU regulations and results in ad serving limitations.
- **Background Broadcast Limits**: Triggering background services or alarms on Android 14+ without explicitly declaring permission types (e.g. `USE_EXACT_ALARM`) will fail silently.
- **Duplicate Resource Compilation**: Copying themes or layout files without renaming XML elements or Compose configurations creates Gradle compilation conflicts.
