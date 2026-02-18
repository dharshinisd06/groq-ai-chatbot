import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="Groq AI Chatbot")
st.title("🤖 Simple AI Chatbot using Groq LLM")

user_input = st.text_input("Enter your question:")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Generating..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant", # You can change model
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            
            answer = response.choices[0].message.content
            st.success("Response:")
            st.write(answer)
    else:
        st.warning("Please enter a question.")
