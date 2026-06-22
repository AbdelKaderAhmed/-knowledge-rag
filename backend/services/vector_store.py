import chromadb
from chromadb.config import Settings
from backend.models.document import ProcessedDocument

class VectorStoreService:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./data/chroma")
        self.collection = self.client.get_or_create_collection(
            name="knowledge_base",
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, chunks: list[ProcessedDocument], embeddings: list[list[float]]):
        ids = [f"doc_{i}" for i in range(len(chunks))]
        metadatas = [chunk.metadata for chunk in chunks]
        documents = [chunk.content for chunk in chunks]
        
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )