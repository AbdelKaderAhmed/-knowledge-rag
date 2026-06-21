import streamlit as st
import requests

st.title("KnowledgeMind - Document Ingestion")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    if st.button("Upload and Process"):
        # 1. Upload
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        
        try:
            with st.spinner('Uploading...'):
                response = requests.post("http://localhost:8000/api/v1/upload", files=files)
            
            if response.status_code == 200:
                st.success("File uploaded successfully!")
                
                # 2. Process
                with st.spinner('Extracting text and processing...'):
                    process_response = requests.post(f"http://localhost:8000/api/v1/process/{uploaded_file.name}")
                    
                    if process_response.status_code == 200:
                        stats = process_response.json()
                        st.success(f"Processing Complete! Extracted chunks: {stats['chunks']}")
                    else:
                        st.error("Upload succeeded, but processing failed.")
            else:
                st.error(f"Upload Error: {response.json().get('detail')}")
                
        except Exception as e:
            st.error(f"System Error: {e}")