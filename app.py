import streamlit as st
from groq import Groq

st.title("🔧 Quick AI Setup Check")

# Check secrets
api_key = st.secrets.get("GROQ_API_KEY", "")
st.write(f"**API Key Length:** {len(api_key)} chars")
st.write(f"**API Key Starts With:** {api_key[:10]}..." if api_key else "**NO API KEY**")

if len(api_key) < 20:
    st.error("❌ **FIX: Add GROQ_API_KEY in Streamlit Secrets!**")
    st.info("""
    **How to fix:**
    1. Go to [share.streamlit.io](https://share.streamlit.io)
    2. Manage app → Settings → Secrets
    3. Paste: `GROQ_API_KEY=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`
    4. Save + Reboot
    """)
    st.stop()

st.success("✅ **API Key OK!**")

# Test Groq connection
if st.button("🧪 Test AI Connection"):
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say 'Quick AI is working!'"}]
        )
        st.success("🚀 **Quick AI LIVE!**")
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"❌ Connection failed: {str(e)}")

st.balloons()




