from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(question,image_data,input_prompt):
    response=model.generate_content([question,image_data[0],input_prompt])
    return response.text

def input_image_details(upload_file):
    if upload_file is not None:
        bytes_data=upload_file.getvalue()
        image_parts = [{
            "mime_type":upload_file.type,
            "data":bytes_data}
        ]
        return image_parts
    else:
        raise FileNotFoundError("NO image uploaded") 


st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.header("Invoice Extracter")


input = st.text_input("Prompt:", key="input")
upload_file = st.file_uploader("choose an image..", type=["jpg","jpeg","png"])

if upload_file is not None:
    image= Image.open(upload_file)

input_prompt = """You are an expert in understanding invoices. We will upload a image as invoice and you will have to answer 
any questions based on the uploaded invoice image"""

submit=st.button("Ask the question")

if submit:
    image_data = input_image_details(upload_file)
    response=get_gemini_response(input,image_data,input_prompt)
    st.subheader("The response is")
    st.write(response)
