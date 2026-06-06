# add_firebase.ps1
# Savior Systems: Add Firebase to GCP Project REST API utility

$token = gcloud auth print-access-token
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}
$url = "https://firebase.googleapis.com/v1beta1/projects/hopeful-breaker-426606-h9:addFirebase"
Write-Host "[*] Adding Firebase to project hopeful-breaker-426606-h9..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body "{}" -ErrorAction Stop
    Write-Host "[+] Firebase successfully added to your project!" -ForegroundColor Green
    $response | ConvertTo-Json | Write-Host
} catch {
    Write-Host "[-] Failed to add Firebase: $_" -ForegroundColor Red
}
