# stress_test_vertex_ai.ps1
# Savior Systems: Vertex AI Gemini Stress Testing and Credit Burner Script
#
# Usage:
#   .\stress_test_vertex_ai.ps1 -Project "hopeful-breaker-426606-h9" -Iterations 10 -Model "gemini-1.5-flash"

param (
    [string]$Project = "hopeful-breaker-426606-h9",
    [string]$Location = "asia-southeast1",
    [string]$Model = "gemini-1.5-flash",
    [int]$Iterations = 5
)

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host " Savior Systems: Vertex AI Gemini Stress Testing Script  " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan

# 1. Fetch OAuth Access Token from gcloud
Write-Host "[*] Fetching access token via gcloud..." -ForegroundColor Yellow
$accessToken = gcloud auth print-access-token
if ($null -eq $accessToken -or $accessToken -eq "") {
    Write-Error "Failed to obtain access token. Please run 'gcloud auth login'."
    Exit 1
}

# Define test prompt templates for Savior Level 3 apps
$prompts = @(
    "Improve this resume summary for a software engineer: 'I write java code and build android apps. Looking for a job.' Make it highly professional and premium.",
    "Generate 5 contextual vocabulary sentences with explanations in Bangla for the English word 'Epiphany'.",
    "Create 3 unique motivational daily quotes focusing on persistence and productivity, output formatted as JSON.",
    "Summarize this audio note transcript into a bulleted action plan: 'Today we discussed adding dynamic coloring to the outfit canvas app. We need to define both light and dark ColorScheme. The minSdk is 24, targetSdk is 35.'",
    "Generate 5 premium Instagram bios for a creative designer showcasing design tools and minimal aesthetic."
)

$endpoint = "https://$($Location)-aiplatform.googleapis.com/v1/projects/$Project/locations/$Location/publishers/google/models/$($Model):generateContent"

Write-Host "[*] Target Endpoint: $endpoint" -ForegroundColor Yellow
Write-Host "[*] Executing $Iterations iterations of prompt stress tests..." -ForegroundColor Yellow

$headers = @{
    "Authorization" = "Bearer $accessToken"
    "Content-Type"  = "application/json"
}

for ($i = 1; $i -le $Iterations; $i++) {
    # Pick a random prompt from the list
    $promptIndex = ($i - 1) % $prompts.Length
    $selectedPrompt = $prompts[$promptIndex]
    
    Write-Host "[*] Iteration $i/$Iterations - Target App Theme: Prompt Index $promptIndex" -ForegroundColor Cyan
    Write-Host "  Prompt: $selectedPrompt" -ForegroundColor Gray
    
    $body = @{
        contents = @(
            @{
                role = "user"
                parts = @(
                    @{ text = $selectedPrompt }
                )
            }
        )
        generationConfig = @{
            temperature = 0.7
            maxOutputTokens = 500
        }
    } | ConvertTo-Json -Depth 10

    try {
        $startTime = Get-Date
        $response = Invoke-RestMethod -Uri $endpoint -Method Post -Headers $headers -Body $body -ErrorAction Stop
        $endTime = Get-Date
        $duration = ($endTime - $startTime).TotalSeconds

        $responseText = $response.candidates[0].content.parts[0].text
        Write-Host "  [+] Success! Latency: $($duration.ToString('F2')) seconds" -ForegroundColor Green
        Write-Host "  Response (Snippet): $($responseText.Substring(0, [Math]::Min(150, $responseText.Length)))...`n" -ForegroundColor DarkGreen
    }
    catch {
        Write-Host "  [-] Failed on iteration $i!" -ForegroundColor Red
        Write-Host "  Error: $_" -ForegroundColor Red
    }
}

Write-Host "[+] Stress test run complete." -ForegroundColor Green
