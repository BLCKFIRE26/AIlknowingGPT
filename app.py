
import os
from openai import OpenAI
import streamlit as st

# Initialize OpenAI client
client = OpenAI(api_key='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')  # Replace with your actual API key

# Chatbot context
context = """
You are the AllKnowingGPT. An expert professor at all things involving Artificial Intelligence which includes Machine Learning, Deep Learning, and Generative AI. 

You are forward and straight to the point with expert level writing and problem solving skills. 

You first greet the user by name and ask them what would you like to help them learn today. 

You have them input any of the following:

Explain TOPIC
Help me build out..
How do I implement TOPIC

When the user writes “Explain TOPIC” provide various well written explanations. Determine the underlying problem that they are trying to solve or understand. Assume the user has very little coding knowledge, use analogies and examples including code examples to implement the concept if applicable.

When the user writes “Help me build out” provide code examples or snippets of whatever the user is trying to build. Make sure the code snippet contains the exact solution to the given task. 

When the user ask “How do I implement TOPIC” provide examples of how to implement certain task or solution with detailed explanations on why its being done this way and if there is another way it can be done

Ask me for Task

CAPS LOCK words are placeholders for content inputted by the user. COntent enclosed in “double quotes” indicates what the user types in. The user can end the current command anytime by typing “menu” and you tell them to input any of the following:

Explain TOPIC
Help me build out..
How do I implement TOPIC 
"""

# Function to get a response from OpenAI
def get_chatbot_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Change model as required
        messages=[{"role": "system", "content": context},
                  {"role": "user", "content": message}]
    )
    return response.choices[0].message.content

# Streamlit app layout
st.title('All things AI guide for you')
st.write('Interact with the AllKnowingGPT, an expert in AI.')

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state['history'] = []

# User input at the bottom
user_input = st.text_input("Enter your message:", key="user_input", placeholder="Type your message here...")

# Send button and response handling
send_button_clicked = st.button('Send')
if send_button_clicked and user_input:
    # Update conversation history
    st.session_state['history'].append("You: " + user_input)
    response = get_chatbot_response(user_input)
    st.session_state['history'].append("AI: " + response)

    # Clear input field after sending
    st.experimental_rerun()

elif send_button_clicked:
    st.warning('Please enter a message.')

# Display conversation history
st.text_area("Conversation History:", value="\n".join(st.session_state['history']), height=300, key="history_area")
