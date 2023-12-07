import streamlit as st
import requests
from PIL import Image
import datetime as time

st.title("Bhasha Bun Language Learning Chatbot")

img = Image.open(r'../images/background01.png')
st.image(img)
key_prompt = st.text_input("Prompt: ")

if st.button("Ask to ChatGPT.."):
    # The execution time limit for an AWS Lambda function is approximately 60 seconds,
    # and if the function takes longer than that to process a request,
    # it will not be able to provide a response.
    if len(key_prompt) > 250:
        st.error("Try more shorter prompt")
    else:
        with st.spinner("Your answer is currently being generated..."):
            time.sleep(5)
        url = "/base"

        responsegpt = requests.get(url, params={"prompt": key_prompt})

        st.success(responsegpt.json())
