import streamlit as st
import requests

st.title("KnowledgeMind - Document Ingestion")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    if st.button("Upload to Backend"):
        
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        
        try:
            
            response = requests.post("http://localhost:8000/api/v1/upload", files=files)
            
            if response.status_code == 200:
                st.success(f"File uploaded successfully! Path: {response.json()['path']}")
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        except Exception as e:
            st.error(f"Connection error: {e}")