import streamlit as st

def auth_menu():
    st.sidebar.page_link("app.py", label="Cambiar cuenta")
    st.sidebar.page_link("pages/chatbot.py", label="Pregúntale a ClaudIA", icon='🤖')

    if st.session_state.role in ["journalist"]:
        st.sidebar.page_link("pages/dashboard.py", label="Temas de la semana", icon='📊')
        st.sidebar.page_link("pages/newsletter.py", label="Mi boletín diario", icon='📥')

def unauth_menu():
    st.sidebar.page_link("app.py", label="Infórmate con ClaudIA", icon='📣')

def menu():
    if "role" not in st.session_state or st.session_state.role is None:
        unauth_menu()
        return
    auth_menu()

def menu_with_redirect():
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()