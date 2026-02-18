import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Groq AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Load Environment Variables
# ---------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.title("⚙️ Settings")

    model = st.selectbox(
        "Choose Model",
        [
            "llama-3.1-8b-instant",
            "llama-3.1-70b-versatile",
            "mixtral-8x7b-32768",
            "gemma2-9b-it"
        ]
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 📌 About")
    st.markdown("🚀 Powered by Groq LLM")
    st.markdown("👩‍💻 Developed by Dharshini")

# ---------------------------
# Header
# ---------------------------
st.markdown(
    "<h1 style='text-align: center;'>🤖 Groq AI Chatbot</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray;'>Fast AI responses using Groq Large Language Models</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------
# Session State for Chat Memory
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Display Chat History
# ---------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------
# Chat Input
# ---------------------------
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=st.session_state.messages
                )

                ai_reply = response.choices[0].message.content
                st.markdown(ai_reply)

                # Store AI reply
                st.session_state.messages.append(
                    {"role": "assistant", "content": ai_reply}
                )

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>Built using Streamlit & Groq API</p>",
    unsafe_allow_html=True
)
