# InstaGrid Splitter 9 Grid

**InstaGrid Splitter 9 Grid** is a highly optimized, offline-first application targeting the "Art & Design" category.

## App Overview
Split high-resolution images into 3x3 grids for seamless Instagram profiles.

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
- **Category:** Level 1 (Telemetry, UMP Consent, and AdMob)
- **Core APIs:** \irebase.googleapis.com\ (Free Tier)
- **SOP Implementation:** Log ASO conversion metrics, standard analytics telemetry, and initialize UMP consent logs.\

### 2. Credentials & Config Mapping
- Place the downloaded \google-services.json\ config inside the \pp/\ directory.
- Production credentials are dynamically configured on launch and kept out of Git repository logs.
