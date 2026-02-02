# Git 蹇€熷悓姝ユ帹閫佽剼鏈?
# 浣跨敤鏂规硶: .\sync.ps1 "鎻愪氦淇℃伅"
param(
    [string]$message = "鏇存柊鍐呭"
)
# 寮哄埗璁剧疆杈撳嚭缂栫爜涓篣TF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
# 妫€鏌ユ槸鍚︽湁鏈殏瀛樼殑鏇存敼
$hasChanges = $(git status --porcelain 2>$null)
if ($hasChanges) {
    Write-Host "妫€娴嬪埌鏇存敼锛屾鍦ㄦ坊鍔犳墍鏈夋枃浠?.." -ForegroundColor Cyan
    git add -A
    
    Write-Host "姝ｅ湪鎻愪氦鏇存敼..." -ForegroundColor Cyan
    git commit -m $message
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "娌℃湁闇€瑕佹彁浜ょ殑鏇存敼" -ForegroundColor Yellow
        exit 0
    }
} else {
    Write-Host "娌℃湁鏇存敼闇€瑕佹彁浜? -ForegroundColor Green
}
Write-Host "姝ｅ湪鍚屾杩滅▼浠撳簱..." -ForegroundColor Cyan
# 妫€鏌ョ綉缁滆繛鎺?
try {
    $response = Invoke-WebRequest -Uri "https://github.com" -TimeoutSec 10 -UseBasicParsing
    if ($response.StatusCode -eq 200) {
        Write-Host "缃戠粶杩炴帴姝ｅ父" -ForegroundColor Green
        
        # 鎵ц鎷夊彇鎿嶄綔
        git pull origin main --rebase
        if ($LASTEXITCODE -ne 0) {
            Write-Host "鎷夊彇澶辫触锛岃妫€鏌ュ啿绐? -ForegroundColor Red
            exit 1
        }
        Write-Host "姝ｅ湪鎺ㄩ€佸埌 GitHub..." -ForegroundColor Cyan
        git push origin main
        if ($LASTEXITCODE -eq 0) {
            Write-Host "鎺ㄩ€佹垚鍔燂紒" -ForegroundColor Green
        } else {
            Write-Host "鎺ㄩ€佸け璐? -ForegroundColor Red
            exit 1
        }
    }
} catch {
    Write-Host "缃戠粶杩炴帴寮傚父锛岃妫€鏌ョ綉缁滆繛鎺ュ悗閲嶈瘯" -ForegroundColor Yellow
    Write-Host "鍙兘鐨勫師鍥狅細" -ForegroundColor Yellow
    Write-Host "   - 缃戠粶涓嶇ǔ瀹? -ForegroundColor Yellow
    Write-Host "   - GitHub 鏈嶅姟鍣ㄦ殏鏃朵笉鍙揪" -ForegroundColor Yellow
    Write-Host "   - 闃茬伀澧欐垨浠ｇ悊璁剧疆闂" -ForegroundColor Yellow
    Write-Host "寤鸿绋嶅悗閲嶈瘯鎴栨墜鍔ㄦ墽琛岋細" -ForegroundColor Yellow
    Write-Host "   git pull origin main" -ForegroundColor Yellow
    Write-Host "   git push origin main" -ForegroundColor Yellow
    exit 1
}