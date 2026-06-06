# configure_gcp_portfolio.ps1
# Savior Systems GCP Portfolio Setup & Scaling Automation Script
#
# Usage:
#   .\configure_gcp_portfolio.ps1 -BillingAccountId "XXXXXX-XXXXXX-XXXXXX" -ProjectId "hopeful-breaker-426606-h9"

param (
    [string]$BillingAccountId,
    [string]$ProjectId = "hopeful-breaker-426606-h9",
    [switch]$VerifyOnly
)

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host " Savior Systems Android Portfolio: GCP Setup Automation " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan

# 1. Verify GCloud Installation
$gcloudCheck = Get-Command gcloud -ErrorAction SilentlyContinue
if ($null -eq $gcloudCheck) {
    Write-Error "gcloud CLI is not installed or not in PATH. Please install Google Cloud SDK."
    Exit 1
}

Write-Host "[*] Configuring active project to: $ProjectId" -ForegroundColor Yellow
gcloud config set project $ProjectId

# 2. Check Authentication
$activeAccount = gcloud config get-value core/account
if ($null -eq $activeAccount -or $activeAccount -eq "") {
    Write-Error "No active gcloud session found. Please run 'gcloud auth login' first."
    Exit 1
}
Write-Host "[+] Active Account: $activeAccount" -ForegroundColor Green

# 3. Handle Billing Account Association
if ($VerifyOnly) {
    Write-Host "[*] Running verification checks..." -ForegroundColor Yellow
    
    Write-Host "[*] Checking enabled APIs..." -ForegroundColor Yellow
    $enabledServices = gcloud services list --enabled --format="value(config.name)"
    
    $requiredAPIs = @(
        "firebase.googleapis.com",
        "firestore.googleapis.com",
        "aiplatform.googleapis.com",
        "cloudresourcemanager.googleapis.com"
    )

    foreach ($api in $requiredAPIs) {
        if ($enabledServices -contains $api) {
            Write-Host "  [+] $api is ENABLED" -ForegroundColor Green
        } else {
            Write-Host "  [-] $api is NOT ENABLED" -ForegroundColor Red
        }
    }
    
    Write-Host "[+] Verification completed." -ForegroundColor Green
    Exit 0
}

if ($null -eq $BillingAccountId -or $BillingAccountId -eq "") {
    Write-Host "[!] Billing Account ID not provided. Skipping billing configuration." -ForegroundColor Yellow
    Write-Host "[*] To configure billing, run: .\configure_gcp_portfolio.ps1 -BillingAccountId 'YOUR_ID'" -ForegroundColor Gray
} else {
    Write-Host "[*] Linking Project $ProjectId to Billing Account $BillingAccountId..." -ForegroundColor Yellow
    gcloud billing projects link $ProjectId --billing-account=$BillingAccountId
}

# 4. Enable Required GCP and Firebase APIs
Write-Host "[*] Enabling required APIs (this may take a few minutes)..." -ForegroundColor Yellow
$apisToEnable = @(
    "cloudresourcemanager.googleapis.com",
    "firebase.googleapis.com",
    "firestore.googleapis.com",
    "aiplatform.googleapis.com",
    "cloudapis.googleapis.com"
)

foreach ($api in $apisToEnable) {
    Write-Host "  Enabling $api..."
    gcloud services enable $api
}

Write-Host "[+] All required APIs are enabled successfully!" -ForegroundColor Green
Write-Host "[*] Ready to integrate Vertex AI and Firebase inside Savior Systems apps." -ForegroundColor Cyan
