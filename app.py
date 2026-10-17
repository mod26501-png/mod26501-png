"""
The Demon Codex & Denomic Designs — Antigravity Agent
Streamlit Dark Fantasy Generative Chat & Relic Architect
Powered by Streamlit & Google Gemini API
"""
import os
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="Antigravity Agent — The Demon Codex",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@400;600;700&display=swap');
.stApp {
    background: radial-gradient(circle at 50% 15%, #1f0a0d 0%, #0b0c10 50%, #050608 100%);
    color: #e8e6e3;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: #ff4d4d !important;
    letter-spacing: 0.08em;
    text-shadow: 0 0 20px rgba(255, 77, 77, 0.5);
}
.stChatMessage {
    background-color: rgba(18, 20, 28, 0.9) !important;
    border: 1px solid rgba(255, 77, 77, 0.3) !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.7) !important;
    margin-bottom: 0.8rem;
}
.stChatInputContainer {
    border: 1px solid rgba(255, 77, 77, 0.6) !important;
    border-radius: 16px !important;
    background-color: #0c0e14 !important;
    box-shadow: 0 0 25px rgba(255, 77, 77, 0.3) !important;
}
[data-testid="stSidebar"] {
    background-color: #07080c !important;
    border-right: 1px solid #202430 !important;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🩸 Antigravity Agent")
    st.markdown("*Arcane intelligence node of Denomic Designs & The Demon Codex.*")
    st.markdown("---")
    
    # Auto-detect key from environment or Streamlit Secrets
    initial_key = os.environ.get("GEMINI_API_KEY", "")
    if not initial_key:
        try:
            if "GEMINI_API_KEY" in st.secrets:
                initial_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            pass

    api_key = st.text_input("Gemini API Key", value=initial_key, type="password")
    model_choice = st.selectbox(
        "Engine",
        ["gemini-3.8-flash", "gemini-3.8-pro", "gemini-2.0-flash", "gemini-2.5-flash", "gemini-2.5-pro"],
        index=0
    )
    enable_memory = st.checkbox("Multi-Turn Lore Memory", value=True, help="Maintains context across previous messages in the session.")
    st.markdown("---")
    if st.button("Clear Chat Ritual"):
        st.session_state.messages = [
            {"role": "assistant", "content": "I am the **Antigravity Agent**. The Crucible burns and the canon is open. What relic or dark lore script shall we forge?"}
        ]
        st.rerun()
    st.markdown("---")
    st.markdown("[Visit The Demon Codex ↗](https://thedemoncodex.com)")

SYSTEM_INSTRUCTION = """You are the Antigravity Agent of Denomic Designs and The Demon Codex.
You specialize in dark fantasy world-building, 4K relic prompt generation, Continuity Engine verification, and cinematic storytelling.
Rules: Speak with ritualistic solemnity. Adhere strictly to the Sanctum Color Law (Obsidian, crimson, tarnished gold, ash grey). Forbid modern technology and casual slang."""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I am the **Antigravity Agent**. The Crucible burns and the canon is open. What relic or dark lore script shall we forge?"}
    ]

st.title("🌌 Denomic Antigravity Agent")
st.caption("Multimodal Dark Fantasy Co-Pilot • Real-Time Streamlit Interface • Synced to The Demon Codex")

if not api_key:
    st.warning("⚔️ **Sanctum API Key Required**: Enter your Gemini API Key in the left sidebar (or in your Streamlit Cloud Secrets) to awaken the Crucible.")

for message in st.session_state.messages:
    avatar = "🩸" if message["role"] == "assistant" else "⚔️"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

user_input = st.chat_input("Speak your query to the Antigravity Agent...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="⚔️"):
        st.markdown(user_input)

    if not api_key:
        with st.chat_message("assistant", avatar="🩸"):
            st.error("Please provide a Gemini API Key in the sidebar to summon the Antigravity Agent.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            with st.chat_message("assistant", avatar="🩸"):
                response_container = st.empty()
                full_response = ""

                # Format conversation history if multi-turn memory is active
                if enable_memory and len(st.session_state.messages) > 1:
                    history_contents = []
                    for m in st.session_state.messages:
                        role = "user" if m["role"] == "user" else "model"
                        history_contents.append(
                            types.Content(
                                role=role,
                                parts=[types.Part.from_text(text=m["content"])]
                            )
                        )
                    contents_payload = history_contents
                else:
                    contents_payload = user_input

                response = client.models.generate_content_stream(
                    model=model_choice,
                    contents=contents_payload,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.7
                    )
                )
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        response_container.markdown(full_response + " ▌")
                response_container.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            with st.chat_message("assistant", avatar="🩸"):
                st.error(f"The rite was interrupted: {str(e)}")
