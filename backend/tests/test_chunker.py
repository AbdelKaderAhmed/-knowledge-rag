def test_chunker_logic():
    from backend.services.chunker import ChunkingService
    from backend.models.document import ProcessedDocument
    
    doc = ProcessedDocument(content="A" * 1200, metadata={"source": "test"})
    service = ChunkingService(chunk_size=500, chunk_overlap=50)
    chunks = service.chunk_document(doc)
    
    assert len(chunks) > 1
    assert "chunk_index" in chunks[0].metadata