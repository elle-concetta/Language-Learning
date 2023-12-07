import streamlit as st
from PIL import Image
import requests

st.title("Gujarati Language Tutor")

# Load and display images
img = Image.open(r'./images/jolly01.png')
st.sidebar.image(img, caption='Jolly')

gptimg = Image.open(r'./images/background01.png')
st.image(gptimg)

# Initialize the chat messages history with a welcome message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Welcome to the Gujarati Language Tutor. How can I assist you today?"}]

# Prompt for user input
user_prompt = st.text_input("Enter your message:", key="chat_input")
if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Call your API Gateway URL
    url = "/base"
    response = requests.get(url, params={"prompt": user_prompt})

    if response.status_code == 200:
        lambda_response = response.json() # Parse response from Lambda
        st.session_state.messages.append({"role": "assistant", "content": lambda_response['message']})
    else:
        st.error("Failed to get response from Lambda function")

# Display chat messages
for message in st.session_state.messages:
    with st.container():
        st.write(f"{message['role'].title()}: {message['content']}")
