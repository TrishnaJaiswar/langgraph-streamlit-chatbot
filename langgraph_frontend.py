import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

st.title("🤖 LangGraph Chatbot")

# Initialize Streamlit message history
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


# Display previous messages
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Type here")


if user_input:

    # Display user message
    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)


    # Invoke LangGraph
    config = {
        "configurable": {
            "thread_id": "1"
        }
    }

    response = chatbot.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config=config
    )

    # Get AI response
    ai_message = response["messages"][-1].content


    # Display AI response
    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })

    with st.chat_message("assistant"):
        st.write(ai_message)