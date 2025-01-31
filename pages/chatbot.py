import streamlit as st
from rag.call import generate_answer
import random
import time

st.set_page_config(layout='centered')
# Streamed response emulator
def response_generator(prompt):
    response = generate_answer(query = prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("My Personalized Chatbot🤖")
st.markdown("""
This chatbot is created using **Retrieval-Augmented Generation (RAG)**, a cutting-edge approach that combines the power of **retrieving relevant information** from a custom dataset with **generating human-like responses** based on that data.

I have personalized this chatbot with my own data, allowing it to provide context-aware answers and respond intelligently to specific queries about me!
""")
st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello👋! Ask me any queries you have about Valentino Ong👦!"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt = st.chat_input("What is up?")
if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})