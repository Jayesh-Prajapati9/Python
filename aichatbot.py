import streamlit as st
from conversation_manager import ConversationManager  # Assuming this is in a separate file

# App title
st.title("AI Chatbot")

# Initialize session state for conversation manager
if "conversation_manager" not in st.session_state:
    st.session_state.conversation_manager = ConversationManager()

chat_manager = st.session_state.conversation_manager

# Sidebar controls
with st.sidebar:
    # Temperature slider
    temperature = st.slider("Chat Temperature", 0.0, 2.0, 0.7, 0.1)
    
    # Token budget sliders
    max_tokens = st.slider("Max Tokens per Message", 100, 2000, 500, 50)
    history_tokens = st.slider("Max History Tokens", 1000, 4000, 2000, 100)
    
    # Persona selector
    persona = st.selectbox(
        "Select Chatbot Persona",
        ["Default", "Professional", "Casual", "Custom"]
    )
    
    # Handle persona selection
    if persona == "Custom":
        custom_message = st.text_area("Enter custom system message")
        if st.button("Set Custom Message") and custom_message:
            chat_manager.set_custom_system_message(custom_message)
    else:
        chat_manager.set_persona(persona.lower())
    
    # Reset button
    if st.button("Reset Chat History"):
        chat_manager.reset_conversation_history()
        st.rerun()

# Initialize conversation history in session state
if "messages" not in st.session_state:
    st.session_state.messages = chat_manager.conversation_history

# Chat interface
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input
if user_input := st.chat_input("Type your message here..."):
    # Add user message to chat
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get bot response
    response = chat_manager.chat_completion(
        user_input,
        max_tokens=max_tokens,
        temperature=temperature,
        history_token_limit=history_tokens
    )
    
    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)
