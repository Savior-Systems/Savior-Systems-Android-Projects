# ☁️ GCP & Firebase API Integration Guide — Savior Systems
`
This guide maps out the specific Google Cloud Platform (GCP) and Firebase APIs required by each of the 30 apps in the Savior Systems portfolio, providing direct setup patterns and budget controls to maximize the utility of your $170 credits.
`
---
`
## 1. API Mapping Matrix
`
To maximize value and stay within the $170 limit, apps are grouped by their cloud requirement levels:
`
### Level 3: AI-Powered Apps (High Credit Priority)
These apps use **Vertex AI in Firebase** to call Gemini models directly from client code.
`
| # | App Name | Primary API | Gemini Use Case | Estimated Daily Cost |
| :--- | :--- | :--- | :--- | :--- |
| **08** | Resume PDF Maker | Vertex AI, Firebase Storage | Resume polisher, formatting suggestions, cover letter generation. | $0.10 - $0.20 |
| **14** | English-Bangla Vocab | Vertex AI | Sentence context generation, Bangla meaning nuances, pronunciation tips. | $0.05 - $0.15 |
| **18** | Daily Quotes Maker | Vertex AI | Personalized motivational quotes generation based on user moods. | $0.05 - $0.10 |
| **27** | Offline Voice Note | Vertex AI | On-device voice-to-text transcript summary and actionable todo extractor. | $0.10 - $0.20 |
| **28** | Social Bio Captions | Vertex AI | Custom bio and caption generator optimized for IG, Facebook, and Twitter. | $0.05 - $0.10 |
`
### Level 2: Shared Sync & Storage (Medium Credit Priority)
These apps use **Firestore** and **Cloud Storage** for cloud syncing/backups (optional but enabled via Blaze).
`
| # | App Name | Primary API | Cloud Service | Estimated Daily Cost |
| :--- | :--- | :--- | :--- | :--- |
| **03** | MicroHabit Tracker | Cloud Firestore | Sync streak data across devices | $0.01 - $0.03 |
| **04** | Expense Diary Local | Cloud Storage (Encrypted) | Encrypted CSV backups to the cloud | $0.01 - $0.02 |
| **10** | Routine Widget | Cloud Firestore | Sync routine schedules across widgets | $0.01 - $0.02 |
| **26** | Offline Vault & Pass | Cloud Storage (SQLCipher) | Fully encrypted secure vault backup | $0.02 - $0.05 |
`
### Level 1: Standard ASO & Ads (Zero/Low Credit Priority)
All remaining 21 apps utilize **Firebase Analytics**, **Google UMP SDK**, and **AdMob**. Their active usage falls within the free tier thresholds and costs **$0.00** of your GCP credits.
`
---
`
## 2. Vertex AI in Firebase Setup (Kotlin)
`
For the Level 3 AI-Powered apps, we use the enterprise-grade **Vertex AI in Firebase SDK** with Firebase App Check to secure your API calls.
`
### Step 1: Add Dependencies (`libs.versions.toml`)
```toml
[versions]
firebase-vertexai = "16.0.0-beta01"
`
[libraries]
firebase-vertexai = { group = "com.google.firebase", name = "firebase-vertexai", version.ref = "firebase-vertexai" }
```
`
### Step 2: Initialize & Call Gemini in your ViewModel
```kotlin
package com.saviorsystems.core.ai
`
import com.google.firebase.Firebase
import com.google.firebase.vertexai.vertexAI
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
`
object AIClient {
    // We use gemini-1.5-flash for maximum cost efficiency and speed
    private val model = Firebase.vertexAI.generativeModel("gemini-1.5-flash")
`
    fun generateText(prompt: String): Flow<String> = flow {
        try {
            val response = model.generateContent(prompt)
            response.text?.let { emit(it) }
        } catch (e: Exception) {
            emit("Error generating content: ${e.localizedMessage}")
        }
    }
}
```
`
---
`
## 3. GCP Billing Alarms & Alert Safeguards
`
To ensure your $170 credits last through your launch, set up billing alerts using the `gcloud` CLI or GCP Console.
`
### Step 1: Create a Billing Budget
Run this command in the terminal to set a budget alert on your Billing Account (`YOUR_BILLING_ACCOUNT_ID` can be found via `gcloud billing accounts list`):
`
```bash
# Set a budget alert at 50%, 75%, and 90% of the $170 target budget
gcloud billing budgets create \
    --billing-account=YOUR_BILLING_ACCOUNT_ID \
    --display-name="Savior Systems 1-Month Scaling Budget" \
    --threshold-rule=percent=0.5,basis=current-spend \
    --threshold-rule=percent=0.75,basis=current-spend \
    --threshold-rule=percent=0.90,basis=current-spend \
    --all-updates-rule-pubsub-topic=projects/hopeful-breaker-426606-h9/topics/billing-alerts \
    --specified-amount=170USD
```
`
---
`
## 4. Portability & Optimization Tips
`
1. **Local Caching First:** Keep SQLite/Room as the source of truth. Do not make a Vertex AI request if local text can be processed.
2. **Compress Prompts:** Keep prompts short. Vertex AI billing is based on input/output token counts.
3. **App Check:** Always enable Firebase App Check inside the Firebase Console to prevent other developers from stealing your app's credentials and draining your Vertex AI quota.
`