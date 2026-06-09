from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response_data(question):
    return chat.send_message(question, stream=True)



st.set_page_config(page_title="Chat Bot")
st.header("gemini llm app")

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:", key="input")
submit=st.button("Ask the question")

if submit and input:
    try:
        response=get_gemini_response_data(input)
        st.session_state['chat_history'].append(("you",input))
        st.subheader("The response is")
        full_response = ""

        for chunk in response:
            if hasattr(chunk, "text") and chunk.text:
                full_response += chunk.text
                st.write(chunk.text)

        st.session_state["chat_history"].append(("bot", full_response))
    except Exception as e:
        print(e)

st.subheader("Chat History")
for (role,chat) in st.session_state["chat_history"]:
    st.write(f"{role}:{chat}")