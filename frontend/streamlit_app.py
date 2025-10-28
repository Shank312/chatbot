

# frontend/streamlit_app.py
import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"  # change if needed

st.set_page_config(page_title="Chatbot MVP", layout="centered")
st.title("💬 Chatbot (MVP)")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "Hello — I'm your chatbot. Type a message and press Send."}]

def send_message(user_text: str):
    payload = {"session_id": "default", "message": user_text}
    try:
        r = requests.post(f"{BACKEND_URL}/chat", json=payload, timeout=30)
        r.raise_for_status()
        reply = r.json().get("reply", "<no-reply>")
    except Exception as e:
        reply = f"[error contacting backend: {e}]"
    st.session_state.messages.append({"role":"user", "content": user_text})
    st.session_state.messages.append({"role":"bot", "content": reply})

# message list
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# input area
with st.form("msg_form", clear_on_submit=True):
    user_input = st.text_input("Your message", "")
    submitted = st.form_submit_button("Send")
    if submitted and user_input.strip():
        send_message(user_input.strip())
        st.experimental_rerun()

