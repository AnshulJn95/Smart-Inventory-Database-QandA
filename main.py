import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Smart Inventory Database Q&A 🏪")

question = st.text_input("Question: ")

if question:
    try:
        chain = get_few_shot_db_chain()
        # Use invoke instead of deprecated run method
        response = chain.invoke({"query": question})

        st.header("Answer")
        # Handle both old and new response formats
        if isinstance(response, dict):
            st.write(response.get('result', response))
        else:
            st.write(response)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please check your database connection and API key.")
