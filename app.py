import streamlit as st
from groq import Groq

# Streamlit Secrets से key
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="Quick AI", page_icon="⚡")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Logo + Title (error safe)
try:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("quick_ai_logo.png", width=60)
    with col2:
        st.markdown("## Quick AI ⚡")
except:
    st.markdown("## Quick AI ⚡")

st.write("Quick AI will help you in your daily use!")

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("ASK ANY QUESTIONS...")

if user_input:
    # User message (सही role use किया)
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("Thinking... ⚡")

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are Quick AI, a super fast AI assistant. Answer shortly and helpfully in simple Hindi-English mix."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        placeholder.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})


