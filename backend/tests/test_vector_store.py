def test_chroma_collection():
    from backend.services.vector_store import VectorStoreService
    service = VectorStoreService()
    assert service.collection.name == "knowledge_base"