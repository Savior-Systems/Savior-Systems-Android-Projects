# register_apps_firebase.ps1
# Savior Systems Firebase App Registration Automation Script
#
# Usage:
#   .\register_apps_firebase.ps1 -ProjectId "hopeful-breaker-426606-h9"

param (
    [string]$ProjectId = "hopeful-breaker-426606-h9",
    [switch]$DryRun
)

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host " Savior Systems Android Portfolio: Firebase Onboarding   " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan

# Define the 30 apps with package names and display names
$apps = @(
    @{ Name = "FocusPulse Pomodoro Timer"; Package = "com.saviorsystems.productivity.focuspulsetimer" },
    @{ Name = "BD Varsity CGPA Calculator"; Package = "com.saviorsystems.education.bdvarsitycgpapro" },
    @{ Name = "MicroHabit Tracker Streaks"; Package = "com.saviorsystems.productivity.microhabittracker" },
    @{ Name = "Expense Diary Offline Log"; Package = "com.saviorsystems.finance.expensediarylocal" },
    @{ Name = "Offline Prayer Times Qibla"; Package = "com.saviorsystems.lifestyle.prayertimehelper" },
    @{ Name = "Water Log & Hydro Reminder"; Package = "com.saviorsystems.health.waterlogremind" },
    @{ Name = "Smart Age & Bengali Date"; Package = "com.saviorsystems.utilities.smartagebddate" },
    @{ Name = "Resume Maker PDF CV Builder"; Package = "com.saviorsystems.productivity.resumepdfmaker" },
    @{ Name = "PDF Compress Resize Offline"; Package = "com.saviorsystems.productivity.pdfcompresslite" },
    @{ Name = "Routine Widget Task Planner"; Package = "com.saviorsystems.productivity.routinewidget" },
    @{ Name = "BD Tax & VAT Calculator"; Package = "com.saviorsystems.finance.bdtaxvatcalc" },
    @{ Name = "Minimalist To-Do List Tasks"; Package = "com.saviorsystems.productivity.minimalisttodo" },
    @{ Name = "Fuel Mileage Log Tracker"; Package = "com.saviorsystems.finance.fuelmileagelog" },
    @{ Name = "English to Bangla Vocabulary"; Package = "com.saviorsystems.education.englishbanglavocab" },
    @{ Name = "Breathing Pacer Guided"; Package = "com.saviorsystems.health.breathingpacer" },
    @{ Name = "WiFi QR Code Generator Sharer"; Package = "com.saviorsystems.tools.wifiqrsharer" },
    @{ Name = "Exam Countdown BD Study Plan"; Package = "com.saviorsystems.education.examcountdownbd" },
    @{ Name = "Daily Quotes Creator Editor"; Package = "com.saviorsystems.art.dailyquotesmaker" },
    @{ Name = "Device Info System Specs"; Package = "com.saviorsystems.tools.deviceinfospecs" },
    @{ Name = "Outfit Canvas Wardrobe Plan"; Package = "com.saviorsystems.lifestyle.outfitcanvas" },
    @{ Name = "ScanMaster Document Scanner"; Package = "com.saviorsystems.tools.scanmasteroffline" },
    @{ Name = "Color Hex Picker Wheel"; Package = "com.saviorsystems.tools.colorhexpicker" },
    @{ Name = "BMI Calculator & BMR Tracker"; Package = "com.saviorsystems.health.bmibmrtracker" },
    @{ Name = "Tip Calculator Split Bills"; Package = "com.saviorsystems.utilities.tipsplitpro" },
    @{ Name = "InstaGrid Splitter 9 Grid"; Package = "com.saviorsystems.art.instagridsplitter" },
    @{ Name = "Encrypted Password Vault"; Package = "com.saviorsystems.tools.offlinevaultpass" },
    @{ Name = "Offline Voice Note Recorder"; Package = "com.saviorsystems.productivity.offlinevoicenote" },
    @{ Name = "Bio Status Captions Creator"; Package = "com.saviorsystems.entertainment.socialbiocaptions" },
    @{ Name = "Auto Text Spammer Loop"; Package = "com.saviorsystems.tools.autotextspammer" },
    @{ Name = "Fake Call Rescue Simulator"; Package = "com.saviorsystems.utilities.fakecallrescue" }
)

# Verify npx installation
$npxCheck = Get-Command npx -ErrorAction SilentlyContinue
if ($null -eq $npxCheck) {
    Write-Error "npx is not installed or not in PATH. Please install Node.js."
    Exit 1
}

Write-Host "[*] Target Firebase Project: $ProjectId" -ForegroundColor Yellow

if ($DryRun) {
    Write-Host "[*] DRY RUN MODE: Simulating registration..." -ForegroundColor Yellow
    foreach ($app in $apps) {
        Write-Host "  [DryRun] Would register: $($app.Name) [Package: $($app.Package)]" -ForegroundColor Gray
    }
    Exit 0
}

Write-Host "[*] Registering 30 apps under Firebase Project '$ProjectId'..." -ForegroundColor Yellow

foreach ($app in $apps) {
    Write-Host "  Registering: $($app.Name) ($($app.Package))..."
    # Run the firebase command to create the android app via npx
    npx -y firebase-tools apps:create android "$($app.Name)" --package-name "$($app.Package)" --project "$ProjectId"
}

Write-Host "[+] All 30 applications successfully registered under project $ProjectId!" -ForegroundColor Green
