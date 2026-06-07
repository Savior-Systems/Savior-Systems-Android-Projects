# 📐 Savior Systems: Cloud Blueprints & Database Schemas
```
This document provides technical design blueprints, prompt engineering templates, Firestore collections, and security rules for the Level 3 (AI) and Level 2 (Sync) applications.
```
---
```
## 1. Level 3: AI-Powered Apps (Vertex AI Prompts)
```
All prompts utilize **Gemini 1.5 Flash** for optimal token cost, low latency, and high efficiency.
```
### APP-08: Resume PDF Maker
* **System Instructions:** You are a professional CV optimizer. Enhance the developer resume summary for maximum impact, retaining all technical terms while improving tone and syntax. Limit output to under 150 words.
* **Prompt Template:**
```
Optimize this raw resume text:
"${user_raw_text}"
Return the response as a valid JSON object matching this schema:
{
  "summary": "enhanced professional summary string",
  "bullet_points": ["bullet point 1", "bullet point 2"]
}
```
```
### APP-14: English-Bangla Vocab
* **System Instructions:** You are a bilingual English-Bangla lexicographer. Generate contextual sentences to explain vocabulary nuances.
* **Prompt Template:**
```
Word: "${target_word}"
Generate 3 distinct contextual sentences in English, each followed by its natural translation in Bangla.
Output JSON schema:
[
  {
    "english": "sentence...",
    "bangla": "translation..."
  }
]
```
```
### APP-18: Daily Quotes Maker
* **System Instructions:** Generate high-impact motivational quotes tailored to user preferences.
* **Prompt Template:**
```
Generate 3 quotes matching the mood "${mood}" and style "${style}".
Output JSON schema:
[
  {
    "quote": "text...",
    "author": "name..."
  }
]
```
```
### APP-27: Offline Voice Note
* **System Instructions:** You are a summary generator. Extract the key action items and main points from the provided note transcript.
* **Prompt Template:**
```
Transcript: "${transcript_text}"
Return the key points and action items.
Output JSON schema:
{
  "summary": "overall summary...",
  "action_items": ["item 1", "item 2"]
}
```
```
---
```
## 2. Level 2: Sync & Storage (Firestore & Rules)
```
### APP-03: MicroHabit Tracker
* **Firestore Schema:**
  - `users/{userId}/habits/{habitId}`
    - `name`: string
    - `frequency`: string (daily/weekly)
    - `currentStreak`: integer
    - `lastCompleted`: timestamp
    - `history`: array [timestamp]
```
* **Firestore Security Rules:**
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId}/habits/{habitId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```
```
### APP-04: Expense Diary Local
* **Storage Backup Path:**
  - `users/{userId}/backups/expense_diary_backup.csv.enc` (Encrypted locally on device with AES-GCM before upload)
```
* **Cloud Storage Security Rules:**
```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{userId}/backups/{allPaths=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```
```