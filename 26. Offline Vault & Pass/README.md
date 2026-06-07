# Encrypted Password Vault

**Encrypted Password Vault** is a highly optimized, offline-first application targeting the "Tools" category.

## App Overview
100% offline AES-256 encrypted password manager with biometric unlock.

## Architecture
This app utilizes standard Savior Systems Android blueprints:
- Jetpack Compose
- Kotlin Coroutines & Flow
- MVI Architecture
- Room / DataStore for offline persistence

## Project Documentation
Please refer to the numeric blueprint files (`01` through `13`) for detailed architectural, UI/UX, and monetization strategies.


---
## ☁️ GCP & Firebase API Setup & SOP

### 1. Required Cloud API Category
- **Category:** Level 2 (Secure Sync & Cloud Storage backups)
- **Core APIs:** \irestore.googleapis.com\, \storage.googleapis.com\`n- **SOP Implementation:** Firestore DB sync utilizing user-isolated security rules defined in \CLOUD-BLUEPRINTS.md\.\

### 2. Credentials & Config Mapping
- Place the downloaded \google-services.json\ config inside the \pp/\ directory.
- Production credentials are dynamically configured on launch and kept out of Git repository logs.
