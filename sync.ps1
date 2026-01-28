# Git 快速同步推送脚本
# 使用方法: .\sync.ps1 "提交信息"

param(
    [string]$message = "更新内容"
)

Write-Host "🔄 正在同步远程仓库..." -ForegroundColor Cyan
git pull origin main --rebase

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 拉取失败，请检查冲突" -ForegroundColor Red
    exit 1
}

Write-Host "📦 正在添加所有更改..." -ForegroundColor Cyan
git add -A

Write-Host "💾 正在提交更改..." -ForegroundColor Cyan
git commit -m $message

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  没有需要提交的更改" -ForegroundColor Yellow
    exit 0
}

Write-Host "🚀 正在推送到 GitHub..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 推送成功！" -ForegroundColor Green
} else {
    Write-Host "❌ 推送失败" -ForegroundColor Red
    exit 1
}
