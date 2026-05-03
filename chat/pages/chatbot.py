import streamlit as st
from menu import menu
from services.llm import chat as llm_chat
from services.transcripts import get_transcript

menu()

st.title("Neci")
st.caption("Infórmate por ti mismo")

if "transcripts" not in st.session_state:
    st.session_state.transcripts = []

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("📝 Cargar Transcripciones")
    
    url = st.text_input("URL de la mañanera", placeholder="https://...")
    
    if st.button("Agregar", type="primary"):
        if url:
            try:
                content = get_transcript(url)
                st.session_state.transcripts.append({
                    "url": url,
                    "content": content
                })
                st.success("Transcripción cargada")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Ingresa una URL")
    
    if st.session_state.transcripts:
        st.divider()
        st.subheader("Cargadas")
        for i, t in enumerate(st.session_state.transcripts):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.text(t["url"][:40] + "..." if len(t["url"]) > 40 else t["url"])
            with col2:
                if st.button("🗑️", key=f"remove_{i}"):
                    st.session_state.transcripts.pop(i)
                    st.rerun()
        
        if st.button("Limpiar todo"):
            st.session_state.transcripts = []
            st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Qué deseas saber de la mañanera?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    messages_for_llm = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
    transcripts = st.session_state.transcripts

    with st.chat_message("assistant"):
        response = st.write_stream(llm_chat(messages_for_llm, transcripts))
    
    st.session_state.messages.append({"role": "assistant", "content": response})