import streamlit as st
from agent.command_parser import parse_and_execute

st.title("Quant Finance AI Agent")

user_input = st.text_input("Enter a finance command:")
if st.button("Run"):
    result = parse_and_execute(user_input)
    st.write(result)
