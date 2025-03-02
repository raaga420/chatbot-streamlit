import streamlit as st
import backe as demo  # ✅ Correct import of backend module

# Set chatbot title and style
st.title("🤖 This is a Chatbot")
st.markdown("### _This_ is :blue[a demo]")

# Initialize LangChain memory in Streamlit session state
if "memory" not in st.session_state:
    st.session_state.memory = demo.chat_memory()  # ✅ Ensure function exists in `backe.py`

# Initialize chat history if it doesn’t exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Input box for user query
input_text = st.chat_input("Ask me anything...")

if input_text:
    # Display user input in chat
    with st.chat_message("user"):
        st.markdown(input_text)

    # Append user input to chat history
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Generate chatbot response using memory
    chat_response = demo.demo_talk(input_text=input_text, memory=st.session_state.memory)

    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(chat_response)

    # Append chatbot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
