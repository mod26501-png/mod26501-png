# Launch Antigravity Agent Streamlit App
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $ScriptDir) { $ScriptDir = Get-Location }

$VenvStreamlit = Join-Path $ScriptDir ".venv\Scripts\streamlit.exe"
$VenvPython = Join-Path $ScriptDir ".venv\Scripts\python.exe"

if (Test-Path $VenvStreamlit) {
    Write-Host "⚔️ Summoning Antigravity Agent via local virtualenv..." -ForegroundColor DarkRed
    & $VenvStreamlit run (Join-Path $ScriptDir "app.py")
} elseif (Get-Command uv -ErrorAction SilentlyContinue) {
    Write-Host "⚔️ Summoning Antigravity Agent via uv..." -ForegroundColor DarkRed
    uv run --with streamlit --with google-genai streamlit run (Join-Path $ScriptDir "app.py")
} elseif (Test-Path $VenvPython) {
    Write-Host "⚔️ Summoning Antigravity Agent via python in .venv..." -ForegroundColor DarkRed
    & $VenvPython -m streamlit run (Join-Path $ScriptDir "app.py")
} else {
    Write-Host "❌ Could not find .venv or uv. Run: uv venv && uv pip install -r requirements.txt" -ForegroundColor Red
}
