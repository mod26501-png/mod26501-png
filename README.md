# Antigravity Agent — The Demon Codex & Denomic Designs

> **Streamlit Dark Fantasy Generative Chat & Relic Architect**  
> Multimodal Dark Fantasy Co-Pilot powered by Streamlit and the Google Gemini API (`google-genai` SDK).

---

## 🩸 Sanctum Features

- **Dark Fantasy Aesthetic**: Sanctum Color Law styling (Obsidian, Crimson `#ff4d4d`, Tarnished Gold, Ash Grey) with gothic Cinzel typography.
- **Multimodal Gemini Integration**: Connects via Google's `google-genai` Python SDK to high-performance reasoning models (`gemini-2.5-flash`, `gemini-2.5-pro`, `gemini-2.0-flash`).
- **Multi-Turn Lore Memory**: Remembers previous relic descriptions, dark lore scripts, and world-building continuity within each session.
- **Real-Time Streaming**: Live streaming token output with cursor animation.
- **Ritual Reset**: Clear lore sessions at any time with a single click.

---

## 🚀 Quick Start

### 1. Launching via PowerShell (`run.ps1`)
From PowerShell:
```powershell
.\run.ps1
```

### 2. Launching via `uv`
```powershell
uv run --with streamlit --with google-genai streamlit run app.py
```

### 3. Setting your Gemini API Key
You can pass your API key directly in the sidebar inside the app, or set it in your environment:
```powershell
$env:GEMINI_API_KEY = "your-api-key-here"
```

---

## 🌌 Canon & Sanctum Law
Adheres strictly to the canon of [The Demon Codex](https://thedemoncodex.com).
