import streamlit as st
from groq import Groq

# ✅ Connection (already working!)
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="Quick AI", page_icon="⚡")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🎨 Professional Header + Logo Effect
st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(90deg, #4b6cb7, #182848); 
                color: white; border-radius: 20px; margin: 20px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);'>
        <h1 style='font-size: 3.5em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>⚡ Quick AI</h1>
        <p style='font-size: 1.4em; opacity: 0.95;'>Super Fast AI Assistant |</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Info
with st.sidebar:
    st.markdown("### 🚀 Quick AI")
    st.markdown("**Status:** ✅ LIVE")
    st.markdown("**Model:** Llama3.1 8B Instant")
    st.markdown("**Speed:** Lightning Fast ⚡")
    st.markdown("---")
    st.markdown("[⭐ Star on GitHub](https://github.com/rounakofficial111-cmd/QUICK-AI)")

# Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
user_input = st.chat_input("💭 Ask anything... (Hindi/English)")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI Response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("**Thinking... ⚡**")
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are Quick AI. Super fast, friendly AI assistant. Answer in simple Hindi-English mix. Be helpful and conversational."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=500
        )
        answer = response.choices[0].message.content
        placeholder.markdown(answer)

    # Save AI message
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666; font-size: 0.9em;'>Made with ❤️ by <a href='https://github.com/rounakofficial111-cmd'>rounakofficial111-cmd</a> | Powered by Groq & Streamlit</p>", unsafe_allow_html=True)





