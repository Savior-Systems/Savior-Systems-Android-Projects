# update_all_docs.ps1
# Savior Systems: Bulk Documentation Updater and Link Repair Tool
#
# Usage:
#   .\update_all_docs.ps1

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host " Savior Systems: Document Path & API Setup Automation    " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan

# 1. Define App Levels for custom blueprint injections
$level3Apps = @("08. Resume PDF Maker", "14. English-Bangla Vocab", "18. Daily Quotes Maker", "27. Offline Voice Note", "28. Social Bio & Status Captions")
$level2Apps = @("03. MicroHabit Tracker", "04. Expense Diary Local", "10. Routine Widget", "26. Offline Vault & Pass")

# Get all markdown files in the workspace (excluding .git and .claude)
$mdFiles = Get-ChildItem -Path "." -Filter "*.md" -Recurse | Where-Object { $_.FullName -notmatch "\\\.git\\" -and $_.FullName -notmatch "\\\.claude\\" }

Write-Host "[*] Processing $($mdFiles.Count) markdown files..." -ForegroundColor Yellow

foreach ($file in $mdFiles) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # 2. Fix the broken workspace paths in links (case-insensitive replace)
    $oldPath = "file:///c:/Users/cibdh/Desktop/Savior-Systems-Android-Projects/"
    $oldPathCaps = "file:///C:/Users/cibdh/Desktop/Savior-Systems-Android-Projects/"
    $newPath = "file:///f:/Savior-Systems-Android-Projects/"
    
    $modified = $false
    if ($content -like "*$oldPath*") {
        $content = $content -replace [regex]::Escape($oldPath), $newPath
        $modified = $true
    }
    if ($content -like "*$oldPathCaps*") {
        $content = $content -replace [regex]::Escape($oldPathCaps), $newPath
        $modified = $true
    }

    # 3. If it is a README.md file inside an App directory, append the GCP/Firebase Integration SOP
    if ($file.Name -eq "README.md" -and $file.Directory.Name -ne "Savior-Systems-Android-Projects") {
        $appName = $file.Directory.Name
        
        # Check if already appended to avoid duplicate injections
        if ($content -notlike "*## ☁️ GCP & Firebase API Setup & SOP*") {
            $sopContent = "`n`n---`n## ☁️ GCP & Firebase API Setup & SOP`n`n"
            $sopContent += "### 1. Required Cloud API Category`n"
            
            if ($level3Apps -contains $appName) {
                $sopContent += "- **Category:** Level 3 (AI-Powered with Vertex AI Gemini 1.5 Flash)`n"
                $sopContent += "- **Core APIs:** \`aiplatform.googleapis.com\`, \`firebase.googleapis.com\``n"
                $sopContent += "- **SOP Implementation:** Integrate the Vertex AI in Firebase SDK in client. Prompts are defined in \`CLOUD-BLUEPRINTS.md\`.\`n"
            } elseif ($level2Apps -contains $appName) {
                $sopContent += "- **Category:** Level 2 (Secure Sync & Cloud Storage backups)`n"
                $sopContent += "- **Core APIs:** \`firestore.googleapis.com\`, \`storage.googleapis.com\``n"
                $sopContent += "- **SOP Implementation:** Firestore DB sync utilizing user-isolated security rules defined in \`CLOUD-BLUEPRINTS.md\`.\`n"
            } else {
                $sopContent += "- **Category:** Level 1 (Telemetry, UMP Consent, and AdMob)`n"
                $sopContent += "- **Core APIs:** \`firebase.googleapis.com\` (Free Tier)`n"
                $sopContent += "- **SOP Implementation:** Log ASO conversion metrics, standard analytics telemetry, and initialize UMP consent logs.\`n"
            }
            
            $sopContent += "`n### 2. Credentials & Config Mapping`n"
            $sopContent += "- Place the downloaded \`google-services.json\` config inside the \`app/\` directory.`n"
            $sopContent += "- Production credentials are dynamically configured on launch and kept out of Git repository logs.`n"
            
            $content += $sopContent
            $modified = $true
        }
    }

    # Save changes if modified
    if ($modified) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "  [+] Updated: $($file.FullName -replace [regex]::Escape($pwd.Path), '')" -ForegroundColor Green
    }
}

Write-Host "[+] Documentation update and path-repair complete!" -ForegroundColor Green

Write-Host "[*] Running Quality Assurance Audit..." -ForegroundColor Yellow
python scripts/audit_workspace.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "[X] Audit Failed! Please fix the errors above before committing." -ForegroundColor Red
    exit 1
}
Write-Host "[+] Quality Assurance Audit Passed!" -ForegroundColor Green
