# setup_firebase_sa.ps1
# Savior Systems: Service Account Setup & Firebase Auth Automation

$ProjectId = "hopeful-breaker-426606-h9"
$SAName = "firebase-admin-sa"
$SAEmail = "$SAName@$ProjectId.iam.gserviceaccount.com"
$KeyPath = "f:\Savior-Systems-Android-Projects\firebase_sa_key.json"

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host " Savior Systems: Firebase CLI Authentication Automation  " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan

# 1. Create the Service Account
Write-Host "[*] Creating Service Account: $SAName..." -ForegroundColor Yellow
gcloud iam service-accounts create $SAName --display-name="Firebase Admin Service Account" --project=$ProjectId

# 2. Grant roles/owner to the Service Account
Write-Host "[*] Granting Owner role to $SAEmail..." -ForegroundColor Yellow
gcloud projects add-iam-policy-binding $ProjectId --member="serviceAccount:$SAEmail" --role="roles/owner"

# 3. Grant roles/firebase.admin to the Service Account
Write-Host "[*] Granting Firebase Admin role to $SAEmail..." -ForegroundColor Yellow
gcloud projects add-iam-policy-binding $ProjectId --member="serviceAccount:$SAEmail" --role="roles/firebase.admin"

# 4. Create and download the key file
Write-Host "[*] Downloading Service Account Key to $KeyPath..." -ForegroundColor Yellow
gcloud iam service-accounts keys create $KeyPath --iam-account=$SAEmail --project=$ProjectId

# 5. Initialize Firebase on GCP project using the Service Account
Write-Host "[*] Authenticating Firebase CLI and linking Firebase project resources..." -ForegroundColor Yellow
$env:GOOGLE_APPLICATION_CREDENTIALS = $KeyPath

# Link Firebase to the GCP Project
npx -y firebase-tools projects:addfirebase $ProjectId

# 6. Run the Android App Onboarding registrations
Write-Host "[*] Registering 30 Android Apps using authenticated Firebase CLI..." -ForegroundColor Yellow
powershell -ExecutionPolicy Bypass -File .\register_apps_firebase.ps1
