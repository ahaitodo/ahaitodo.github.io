# Git 快速同步推送脚本
# 使用方法: .\sync.ps1 "提交信息"

param(
    [string]$message = "更新内容"
)

# 检查是否有未暂存的更改
$hasChanges = $(git status --porcelain 2>$null)
if ($hasChanges) {
    Write-Host "📦 检测到更改，正在添加所有文件..." -ForegroundColor Cyan
    git add -A
    
    Write-Host "💾 正在提交更改..." -ForegroundColor Cyan
    git commit -m $message
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠️  没有需要提交的更改" -ForegroundColor Yellow
        exit 0
    }
} else {
    Write-Host "✅ 没有更改需要提交" -ForegroundColor Green
}

Write-Host "🔄 正在同步远程仓库..." -ForegroundColor Cyan

# 检查网络连接
try {
    $response = Invoke-WebRequest -Uri "https://github.com" -TimeoutSec 10 -UseBasicParsing
    if ($response.StatusCode -eq 200) {
        Write-Host "🌐 网络连接正常" -ForegroundColor Green
        
        # 执行拉取操作
        git pull origin main --rebase

        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ 拉取失败，请检查冲突" -ForegroundColor Red
            exit 1
        }

        Write-Host "🚀 正在推送到 GitHub..." -ForegroundColor Cyan
        git push origin main

        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ 推送成功！" -ForegroundColor Green
        } else {
            Write-Host "❌ 推送失败" -ForegroundColor Red
            exit 1
        }
    }
} catch {
    Write-Host "⚠️  网络连接异常，请检查网络连接后重试" -ForegroundColor Yellow
    Write-Host "💡  可能的原因：" -ForegroundColor Yellow
    Write-Host "   - 网络不稳定" -ForegroundColor Yellow
    Write-Host "   - GitHub 服务器暂时不可达" -ForegroundColor Yellow
    Write-Host "   - 防火墙或代理设置问题" -ForegroundColor Yellow
    Write-Host "💡  建议稍后重试或手动执行：" -ForegroundColor Yellow
    Write-Host "   git pull origin main" -ForegroundColor Yellow
    Write-Host "   git push origin main" -ForegroundColor Yellow
    exit 1
}
