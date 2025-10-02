import streamlit as st
from query import ask
st.set_page_config(page_title="Asistente Extremeño", page_icon="🐂")
st.title("🧭 Asistente de Viaje de Extremadura")
if "messages" not in st.session_state:
  st.session_state.messages = []
for msg in st.session_state.messages:
  st.chat_message(msg["role"]).write(msg["content"])
  prompt = st.chat_input("Pregunta sobre Extremadura...")
if prompt:
  st.session_state.messages.append({"role": "user", "content": prompt})
  st.chat_message("user").write(prompt)
with st.spinner("Buscando..."):
  answer = ask(prompt)
  st.session_state.messages.append({"role": "assistant", "content": answer})
  st.chat_message("assistant").write(answer)
