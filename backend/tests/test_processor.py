def test_pdf_processing():
    from backend.services.processor import DocumentProcessor
    
    docs = DocumentProcessor.process("data/uploads/test.pdf")
    assert len(docs) > 0
    assert "content" in docs[0].model_dump()