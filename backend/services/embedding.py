
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
from backend.models.document import ProcessedDocument
class EmbeddingService:
    def __init__(self):
        
        self.model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def generate_embeddings(self, chunks: List[ProcessedDocument]) -> List[List[float]]:
        texts = [chunk.content for chunk in chunks]
        
        batch_size = 32
        embeddings = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            embeddings.extend(self.model.embed_documents(batch))
        return embeddings