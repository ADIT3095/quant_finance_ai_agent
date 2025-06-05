import sys
import os
from agent.command_parser import parse_and_execute

import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.title("Quant Finance AI Agent")

user_input = st.text_input("Enter a finance command:")
if st.button("Run"):
    result = parse_and_execute(user_input)
    st.write(result)
