# frontend.py

import streamlit as st
import requests

# --- Page Configuration ---
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🧠 Mental Health Support Chatbot")
st.write("This is a safe space to share your feelings. I'm here to listen without judgment.")
st.write("---")

# --- Session State for History ---
# We use Streamlit's session state to keep the conversation history.
if 'history' not in st.session_state:
    st.session_state['history'] = [] # Stores pairs of (user_message, bot_response)
if 'chat_history_ids' not in st.session_state:
    st.session_state['chat_history_ids'] = None # Stores the model's internal tensor history

# In a real deployment, this URL would point to your running Flask API.
# We will set this up properly in the next step on Replit.
API_URL = "http://127.0.0.1:8080/chat"

# --- Display Chat History ---
for user_msg, bot_msg in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

# --- User Input Handling ---
prompt = st.chat_input("How are you feeling today?")

if prompt:
    # Add user message to the display
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare data for the API request
    api_data = {
        'message': prompt,
        'history': st.session_state.chat_history_ids
    }
    
    # Show a spinner while waiting for the response
    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL, json=api_data)
            response.raise_for_status() # Raise an error for bad status codes
            
            result = response.json()
            bot_response = result['response']
            
            # Display the bot's response
            with st.chat_message("assistant"):
                st.markdown(bot_response)

            # Update the history in session state
            st.session_state.history.append((prompt, bot_response))
            st.session_state.chat_history_ids = result['history']

        except requests.exceptions.RequestException as e:
            st.error(f"API Error: Could not connect to the chatbot service. Please ensure the backend is running and the API_URL is correct. Details: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")