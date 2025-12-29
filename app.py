import streamlit as st
from groq import Groq

# Safe secrets loading
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    if not GROQ_API_KEY:
        raise ValueError("API key missing")
    client = Groq(api_key=GROQ_API_KEY)
    st.success("✅ Quick AI Ready!")
except Exception as e:
    st.error(f"🚫 API Error: {str(e)}")
    st.stop()

st.set_page_config(page_title="Quick AI", page_icon="⚡")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Professional Header
st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(90deg, #4b6cb7, #182848); 
                color: white; border-radius: 20px; margin: 20px 0;'>
        <h1 style='font-size: 3em; margin: 0;'>⚡ Quick AI</h1>
        <p style='font-size: 1.2em; opacity: 0.9;'>Super Fast AI Assistant</p>
    </div>
""", unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("ASK ANY QUESTIONS...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("Thinking... ⚡")

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are Quick AI. Answer shortly in simple Hindi-English mix."},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            placeholder.markdown(answer)
        except Exception as e:
            answer = f"Error: {str(e)}"
            placeholder.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})



