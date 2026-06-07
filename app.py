from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&n Demo")
st.header("gemini llm app")

input = st.text_input("Input:", key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)
