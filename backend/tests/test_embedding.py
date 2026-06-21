def test_embedding_dimension():
    from backend.services.embedding import EmbeddingService
    service = EmbeddingService()
    vector = service.generate_embeddings([ProcessedDocument(content="test", metadata={})])
    assert len(vector[0]) == 384  