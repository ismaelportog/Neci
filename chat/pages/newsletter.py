import streamlit as st
from menu import menu_with_redirect

menu_with_redirect()

st.title("This page is available to journalist")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")