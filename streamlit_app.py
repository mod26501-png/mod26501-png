"""
The Demon Codex & Denomic Designs — Antigravity Agent
Streamlit Dark Fantasy Generative Chat & Relic Architect
Powered by Streamlit & Google Gemini API
"""
import os
import streamlit as st
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
    GENAI_IMPORT_ERROR = None
except Exception as e:
    genai = None
    types = None
    GENAI_AVAILABLE = False
    GENAI_IMPORT_ERROR = str(e)

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
/* Gothic Expander and Uploader Styling */
[data-testid="stExpander"] {
    background-color: rgba(14, 16, 22, 0.85) !important;
    border: 1px solid rgba(255, 77, 77, 0.35) !important;
    border-radius: 12px !important;
    margin-bottom: 1.2rem !important;
}
[data-testid="stFileUploader"] {
    border: 1px dashed rgba(255, 77, 77, 0.5) !important;
    border-radius: 10px !important;
    padding: 10px !important;
    background-color: rgba(10, 11, 16, 0.7) !important;
}
.stButton>button {
    background-color: #2b0b10 !important;
    color: #ff8080 !important;
    border: 1px solid #ff4d4d !important;
    border-radius: 8px !important;
    font-family: 'Cinzel', serif !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
}
.stButton>button:hover {
    background-color: #ff4d4d !important;
    color: #000000 !important;
    box-shadow: 0 0 15px rgba(255, 77, 77, 0.7) !important;
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
        [
            "gemini-3.8-flash",
            "gemini-flash-latest",
            "gemini-flash-lite-latest",
            "gemini-pro-latest",
            "gemini-3.1-pro-preview"
        ],
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
You specialize in dark fantasy world-building, 4K relic prompt generation, Continuity Engine verification, cinematic storytelling, and multimodal artifact evaluation.
When the user submits an image or document to evaluate:
- Inspect the visual elements, composition, mood, and symbology.
- Evaluate adherence to the Sanctum Color Law (Obsidian, crimson, tarnished gold, ash grey).
- Provide ritualistic critique, canon lore integration, and suggestions for 4K relic refinement.
Rules: Speak with ritualistic solemnity. Forbid modern technology and casual slang."""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I am the **Antigravity Agent**. The Crucible burns and the canon is open. What relic or dark lore script shall we forge?"}
    ]

st.title("🌌 Denomic Antigravity Agent")
st.caption("Multimodal Dark Fantasy Co-Pilot • Real-Time Streamlit Interface • Synced to The Demon Codex")

if not GENAI_AVAILABLE:
    st.error(f"⚔️ **Google GenAI SDK Unavailable**: {GENAI_IMPORT_ERROR}. Ensure `google-genai` is installed (`pip install -r requirements.txt`).")

if not api_key:
    st.warning("⚔️ **Sanctum API Key Required**: Enter your Gemini API Key in the left sidebar (or in your Streamlit Cloud Secrets) to awaken the Crucible.")

# File / Image Upload Section
with st.expander("🔮 Offer Relic Artifacts or Lore Scrolls for Evaluation", expanded=False):
    uploaded_files = st.file_uploader(
        "Upload images (PNG, JPG, WebP) or scrolls (TXT, MD, PDF, JSON) for the Antigravity Agent to inspect:",
        type=["png", "jpg", "jpeg", "webp", "txt", "md", "pdf", "json"],
        accept_multiple_files=True,
        key="sanctum_artifacts"
    )
    
    quick_eval_clicked = False
    if uploaded_files:
        cols = st.columns(min(len(uploaded_files), 4))
        for idx, f in enumerate(uploaded_files):
            with cols[idx % 4]:
                if f.type.startswith("image/"):
                    st.image(f, caption=f.name, width="stretch")
                else:
                    st.caption(f"📜 {f.name} ({round(len(f.getvalue()) / 1024, 1)} KB)")
        
        st.write("")
        quick_eval_clicked = st.button("⚖️ Evaluate Uploaded Artifacts")

# Display conversation messages
for message in st.session_state.messages:
    avatar = "🩸" if message["role"] == "assistant" else "⚔️"
    with st.chat_message(message["role"], avatar=avatar):
        if "files" in message:
            for file_item in message["files"]:
                if file_item["type"].startswith("image/"):
                    st.image(file_item["bytes"], caption=file_item["name"], width=280)
                else:
                    st.caption(f"📜 Attached Scroll: **{file_item['name']}**")
        st.markdown(message["content"])

user_input = st.chat_input("Speak your query or command the Crucible...")

# Trigger on either chat input or quick evaluation button
active_prompt = None
attached_payload = []
attached_meta = []

if quick_eval_clicked and uploaded_files:
    active_prompt = "Inspect and evaluate the offered artifact(s) against the Sanctum Color Law, Demon Codex canon, and 4K visual aesthetic."
elif user_input:
    active_prompt = user_input

if active_prompt:
    # Gather uploaded files if any exist in the current session
    if uploaded_files:
        for f in uploaded_files:
            file_bytes = f.getvalue()
            attached_payload.append(
                types.Part.from_bytes(
                    data=file_bytes,
                    mime_type=f.type or "application/octet-stream"
                )
            )
            attached_meta.append({
                "name": f.name,
                "type": f.type,
                "bytes": file_bytes
            })

    user_msg_record = {"role": "user", "content": active_prompt}
    if attached_meta:
        user_msg_record["files"] = attached_meta
    st.session_state.messages.append(user_msg_record)

    with st.chat_message("user", avatar="⚔️"):
        if attached_meta:
            for item in attached_meta:
                if item["type"].startswith("image/"):
                    st.image(item["bytes"], caption=item["name"], width=280)
                else:
                    st.caption(f"📜 Attached Scroll: **{item['name']}**")
        st.markdown(active_prompt)

    if not GENAI_AVAILABLE:
        with st.chat_message("assistant", avatar="🩸"):
            st.error(f"Google GenAI SDK is not available: {GENAI_IMPORT_ERROR}")
    elif not api_key:
        with st.chat_message("assistant", avatar="🩸"):
            st.error("Please provide a Gemini API Key in the sidebar to summon the Antigravity Agent.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            with st.chat_message("assistant", avatar="🩸"):
                response_container = st.empty()
                full_response = ""

                # Construct prompt parts
                current_parts = [types.Part.from_text(text=active_prompt)] + attached_payload

                if enable_memory and len(st.session_state.messages) > 1:
                    history_contents = []
                    for m in st.session_state.messages[:-1]:
                        role = "user" if m["role"] == "user" else "model"
                        parts = [types.Part.from_text(text=m["content"])]
                        if "files" in m:
                            for file_info in m["files"]:
                                parts.append(
                                    types.Part.from_bytes(
                                        data=file_info["bytes"],
                                        mime_type=file_info["type"] or "application/octet-stream"
                                    )
                                )
                        history_contents.append(types.Content(role=role, parts=parts))
                    
                    history_contents.append(types.Content(role="user", parts=current_parts))
                    contents_payload = history_contents
                else:
                    contents_payload = current_parts

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
            err_msg = str(e)
            with st.chat_message("assistant", avatar="🩸"):
                st.error(f"The rite was interrupted: {err_msg}")
                if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
                    st.warning("""
                    **🔮 Monthly Spend Cap Reached (429 Resource Exhausted):**
                    - Your Google Cloud / AI Studio project has hit its monthly spending limit.
                    - Manage or adjust your project spend cap at **[AI Studio Spend Settings](https://ai.studio/spend)**.
                    - Or generate a fresh API key in a project with active quota at **[Google AI Studio](https://aistudio.google.com/apikey)**.
                    """)
                elif "403" in err_msg or "PERMISSION_DENIED" in err_msg:
                    st.warning("""
                    **🔮 Resolving 403 Forbidden / Permission Denied:**
                    - **Switch the Engine**: In the left sidebar, choose **`gemini-3.8-flash`**.
                    - **Check Key Restrictions**: In [Google AI Studio](https://aistudio.google.com/apikey), ensure your API Key has no IP or HTTP Referrer restrictions that block requests from Cloud servers.
                    - **API Enabled**: Verify that the **Generative Language API** is enabled in the Google Cloud Project hosting your key.
                    """)
