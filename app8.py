import streamlit as st
import google.generativeai as genai

# ---------- CONFIG ----------
st.set_page_config(page_title="PRASH-BOT", page_icon="🤖")

genai.configure(api_key="AIzaSyBqxeHLy-cgOesCOK3aEphzG-B5hCGRNuo")

model = genai.GenerativeModel("models/gemini-2.5-flash")

# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- SIDEBAR ----------
st.sidebar.title("PRASH-BOT Settings")

personality = st.sidebar.selectbox(
    "Choose Bot Style",
    ["Helpful", "Teacher", "Friend", "Coder", "Motivator"]
)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("### 💡 Try asking")
st.sidebar.write("• Explain Python loops")
st.sidebar.write("• Motivate me to study")
st.sidebar.write("• How to build website")
st.sidebar.write("• Tell me a joke")

# ---------- HEADER ----------
col1, col2 = st.columns([1,4])
with col1:
    st.image("bot.png", width=70)
with col2:
    st.title("PRASH-BOT")
    st.caption("Your AI Chat Companion")

st.divider()

# ---------- PERSONALITY PROMPT ----------
styles = {
    "Helpful": "You are a helpful assistant.",
    "Teacher": "Explain like a teacher.",
    "Friend": "Talk casually like a friend.",
    "Coder": "Answer like a programming expert.",
    "Motivator": "Be motivational."
}

system_prompt = styles[personality]

# ---------- CHAT HISTORY ----------
for msg in st.session_state.messages:
    avatar = "🤖" if msg["role"]=="assistant" else "🙂"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# ---------- INPUT ----------
user = st.chat_input("Ask me anything...")

if user:
    st.session_state.messages.append({"role":"user","content":user})

    with st.chat_message("user", avatar="🙂"):
        st.write(user)

    prompt = system_prompt + "\nUser: " + user

    response = model.generate_content(prompt)
    reply = response.text

    with st.chat_message("assistant", avatar="🤖"):
        st.write(reply)

    st.session_state.messages.append({"role":"assistant","content":reply})