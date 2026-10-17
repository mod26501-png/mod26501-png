# Launch Antigravity Agent Streamlit App
# Using uv (installed) or fallback to python
if (Get-Command uv -ErrorAction SilentlyContinue) {
    Write-Host "⚔️ Summoning Antigravity Agent via uv..." -ForegroundColor DarkRed
    uv run --with streamlit --with google-genai streamlit run app.py
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "⚔️ Summoning Antigravity Agent via python..." -ForegroundColor DarkRed
    python -m streamlit run app.py
} else {
    Write-Host "❌ Neither uv nor python was detected in PATH." -ForegroundColor Red
}
