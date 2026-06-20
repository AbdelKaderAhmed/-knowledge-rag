import streamlit as st
import requests

st.title("KnowledgeMind RAG Interface")

if st.button("Check Connection"):
    try:
        response = requests.get("http://127.0.0.1:8000/health")
        st.success(f"Response: {response.json()}")
    except Exception as e:
        st.error(f"Failed to connect to backend: {e}")