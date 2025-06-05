import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.command_parser import parse_and_execute

# Streamlit app UI
st.set_page_config(page_title="Quant Finance AI Agent")
st.title("Quant Finance AI Agent")

user_input = st.text_input("Enter a finance command:")
if st.button("Run"):
    result = parse_and_execute(user_input)
    st.write(result)
