import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import time
import os

# =====================================================
# 🔑 GROQ API KEY
# =====================================================
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)
MODEL_NAME = "llama-3.1-8b-instant"

# =====================================================
# 🎨 PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="BuddyBot",
    page_icon="🤖",
    layout="centered"
)

# =====================================================
# 🌑 DARK + LIQUID GLASS UI
# =====================================================
st.markdown("""
<style>
html, body, .stApp {
    background: linear-gradient(180deg, #020617, #000000);
    color: #e5e7eb;
}

h1 {
    text-align: center;
    color: #7dd3fc;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 20px;
    font-size: 14px;
}

.glass {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.12);
}

.chat-row {
    display: flex;
    margin-bottom: 12px;
}

.chat-row.user {
    justify-content: flex-end;
    margin-top: 10px;
}

.chat-row.bot {
    justify-content: flex-start;
}

.chat {
    max-width: 75%;
    padding: 12px 16px;
    border-radius: 16px;
    line-height: 1.6;
    font-size: 15px;
}

.chat.user {
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-bottom-right-radius: 4px;
}

.chat.bot {
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.3);
    border-bottom-left-radius: 4px;
}

.typing {
    font-style: italic;
    color: #94a3b8;
    font-size: 14px;
    padding-left: 6px;
}

.stTextInput input {
    background: rgba(255, 255, 255, 0.07);
    color: black;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.stButton button {
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    color: black;
    border-radius: 12px;
    padding: 8px 20px;
    border: none;
    font-size: 15px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# 🧠 HEADER
# =====================================================
st.markdown("<h1>🤖 BlaBlaBot</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI Friendly Chatbot</div>",
    unsafe_allow_html=True
)

# =====================================================
# 💬 SESSION STATE
# =====================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "typing" not in st.session_state:
    st.session_state.typing = False

# =====================================================
# 🧊 CHAT DISPLAY
# =====================================================
st.markdown("<div class='glass'>", unsafe_allow_html=True)

for role, text in st.session_state.messages:
    if role == "user":
        st.markdown(
            f"""
            <div class='chat-row user'>
                <div class='chat user'>{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class='chat-row bot'>
                <div class='chat bot'>{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# 👇 Typing indicator
if st.session_state.typing:
    st.markdown(
        """
        <div class='chat-row bot'>
            <div class='typing'>🤖 Buddy is typing...</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# ✍️ INPUT ROW
# =====================================================
col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "Message",
        placeholder="Talk here?",
        label_visibility="collapsed"
    )

with col2:
    send = st.button("Send 🚀")

# =====================================================
# 🧠 CHAT LOGIC WITH TYPING EFFECT
# =====================================================
if send and user_input.strip():
    st.session_state.messages.append(("user", user_input))
    st.session_state.typing = True
    st.rerun()

# =====================================================
# 🤖 BOT RESPONSE
# =====================================================
if st.session_state.typing:
    SYSTEM_PROMPT = """
You are a friendly AI chatbot.
Speak in clean Tamil-English slang (Tanglish).
Be polite and supportive.
No bad words. No offensive language.
Give responses in related to the user's query only.
Speak properly without spelling mistakes.
Give short and concise answers.
"""

    with st.spinner(""):
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": st.session_state.messages[-1][1]}
            ],
            temperature=0.7,
            max_tokens=512
        )

    reply = response.choices[0].message.content

    time.sleep(0.6)  # 👈 makes typing feel real
    st.session_state.messages.append(("bot", reply))
    st.session_state.typing = False
    st.rerun()


