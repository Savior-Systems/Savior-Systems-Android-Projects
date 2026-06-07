# Offline Voice Note Recorder

**Offline Voice Note Recorder** is a highly optimized, offline-first application targeting the "Productivity" category.

## App Overview
Record audio memos, dictations, and voice notes fully offline without transcription tracking.

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
- **Category:** Level 3 (AI-Powered with Vertex AI Gemini 1.5 Flash)
- **Core APIs:** \iplatform.googleapis.com\, \irebase.googleapis.com\`n- **SOP Implementation:** Integrate the Vertex AI in Firebase SDK in client. Prompts are defined in \CLOUD-BLUEPRINTS.md\.\

### 2. Credentials & Config Mapping
- Place the downloaded \google-services.json\ config inside the \pp/\ directory.
- Production credentials are dynamically configured on launch and kept out of Git repository logs.
