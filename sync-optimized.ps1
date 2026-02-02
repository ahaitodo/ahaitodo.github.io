# Git Quick Sync Push Script (Optimized Version)
# Usage: .\sync-optimized.ps1 "commit message"

param(
    [string]$message = "Update content"
)

# Ensure UTF-8 encoding
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Check if current directory is a Git repository
if (-not (Test-Path ".git")) {
    Write-Host "Error: Current directory is not a Git repository" -ForegroundColor Red
    exit 1
}

# Check for uncommitted changes
$hasChanges = $(git status --porcelain 2>$null)
if ($hasChanges) {
    Write-Host "[INFO] Changes detected, adding all files..." -ForegroundColor Cyan
    git add -A
    
    Write-Host "[INFO] Committing changes..." -ForegroundColor Cyan
    git commit -m $message
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[WARN] No changes to commit" -ForegroundColor Yellow
        exit 0
    }
} else {
    Write-Host "[INFO] No changes to commit" -ForegroundColor Green
}

Write-Host "[INFO] Syncing with remote repository..." -ForegroundColor Cyan

# Check network connection
try {
    $response = Invoke-WebRequest -Uri "https://github.com" -TimeoutSec 10 -UseBasicParsing
    if ($response.StatusCode -eq 200) {
        Write-Host "[INFO] Network connection normal" -ForegroundColor Green
        
        # Pull latest changes
        Write-Host "[INFO] Pulling latest changes from remote..." -ForegroundColor Cyan
        git pull origin main --rebase

        if ($LASTEXITCODE -ne 0) {
            Write-Host "[ERROR] Pull failed, please check conflicts" -ForegroundColor Red
            exit 1
        }

        Write-Host "[INFO] Pushing to GitHub..." -ForegroundColor Cyan
        git push origin main

        if ($LASTEXITCODE -eq 0) {
            Write-Host "[SUCCESS] Push successful!" -ForegroundColor Green
        } else {
            Write-Host "[ERROR] Push failed" -ForegroundColor Red
            exit 1
        }
    }
} catch {
    Write-Host "[WARN] Network connection error, please check network and retry" -ForegroundColor Yellow
    Write-Host "[TIP] Possible reasons:" -ForegroundColor Yellow
    Write-Host "   - Unstable network" -ForegroundColor Yellow
    Write-Host "   - GitHub server temporarily unavailable" -ForegroundColor Yellow
    Write-Host "   - Firewall or proxy settings issue" -ForegroundColor Yellow
    Write-Host "[TIP] Suggested manual commands:" -ForegroundColor Yellow
    Write-Host "   git pull origin main" -ForegroundColor Yellow
    Write-Host "   git push origin main" -ForegroundColor Yellow
    exit 1
}

Write-Host "[INFO] Operation completed" -ForegroundColor Green