import streamlit as st

usuario = {"user": "abc", "senha": "123"}

def login():
    if usuario["user"] == st.session_state.user and usuario["senha"] == st.session_state.senha:
        st.session_state.login = True
    else:
        st.session_state.login = False
    return st.session_state.login

def logout():
    st.session_state.login = False