import streamlit as st
from dotenv import load_dotenv
import os
from adaptive_tutoring_system_py.config.agents import agents

load_dotenv()

# Load your interactive tutor agent
tutor = agents["interactive_tutor"]

st.set_page_config(page_title="AI Tutor", page_icon="📚")
st.title("📚 Adaptive AI Tutor")
st.markdown("Ask the tutor anything and receive a clear, personalized explanation.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Input box
if prompt := st.chat_input("Ask your tutor a question..."):
    # Add user's message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Construct system message from agent's role and backstory
    system_msg = f"{tutor.role}: {tutor.backstory}"

    # Use the agent's LLM directly
    response = tutor.llm.invoke([
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt}
    ])

    # Extract and show response
    reply = response.content.strip()
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
